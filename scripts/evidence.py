"""Small evidence operations for one student's task. Standard library only.

No target code execution, grading, deployment, authentication, or paid calls.
Remote fetches must be public URLs; authenticated artifacts belong in the approved
browser session or local files. Run with python -I.
"""
import argparse
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import ipaddress
import json
from pathlib import Path
import socket
from urllib.error import HTTPError
from urllib.parse import parse_qsl, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

MAX_BYTES = 16 * 1024 * 1024
SECRET_QUERY_NAMES = {"email", "token", "accesstoken", "authorization", "key", "apikey", "quizsign", "signature", "launch_token", "password", "credential", "idtoken"}


def fnv1a32(data):
    value = 2166136261
    for byte in data:
        value = ((value ^ byte) * 16777619) & 0xffffffff
    return f"fnv1a32:{value:08x}"


def read_limited(path, maximum=MAX_BYTES):
    with Path(path).open("rb") as stream:
        data = stream.read(maximum + 1)
    if len(data) > maximum:
        raise ValueError(f"File exceeds {maximum} bytes; inspect it with a task-specific streaming reader")
    return data


def identity(data):
    kind = "unknown/text"
    for magic, label in [(b"\x89PNG\r\n\x1a\n", "PNG"), (b"PK\x03\x04", "ZIP"), (b"\x1f\x8b", "gzip"), (b"%PDF-", "PDF")]:
        if data.startswith(magic):
            kind = label
            break
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "utf8_bom": data.startswith(b"\xef\xbb\xbf"), "kind_hint": kind}


def strict_json(data):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key!r}")
            result[key] = value
        return result
    def reject(value):
        raise ValueError(f"Nonstandard JSON numeric constant: {value}")
    return json.loads(data.decode("utf-8-sig"), object_pairs_hook=pairs,
                      parse_float=Decimal, parse_constant=reject)


def json_summary(value):
    unsafe = []
    def walk(item, location="$", depth=0):
        if depth > 128:
            raise ValueError("JSON nesting exceeds this helper's 128-level limit")
        if isinstance(item, int) and not isinstance(item, bool) and abs(item) > 2 ** 53 - 1:
            if len(unsafe) < 20:
                unsafe.append(location)
        elif isinstance(item, dict):
            for key, child in item.items():
                walk(child, f"{location}[{json.dumps(key)}]", depth + 1)
        elif isinstance(item, list):
            for index, child in enumerate(item):
                walk(child, f"{location}[{index}]", depth + 1)
    walk(value)
    types = {dict: "object", list: "array", str: "string", int: "integer", Decimal: "decimal", bool: "boolean", type(None): "null"}
    result = {"root_type": types.get(type(value), type(value).__name__),
              "unsafe_js_integer_paths_first_20": unsafe,
              "note": "Decimal spelling is preserved for inspection; task-specific canonicalization is not guessed."}
    if isinstance(value, dict):
        result.update(key_count=len(value), keys=list(value)[:100])
    elif isinstance(value, list):
        result.update(length=len(value))
    return result


def validate_public_url(url, resolve_dns=True):
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or not parts.hostname:
        raise ValueError("Use an explicit public http:// or https:// URL")
    if parts.username or parts.password or parts.fragment:
        raise ValueError("Credentials and fragments are not accepted")
    for key, _ in parse_qsl(parts.query, keep_blank_values=True):
        normalized = key.lower().replace("-", "").replace("_", "")
        if normalized in {name.replace("_", "") for name in SECRET_QUERY_NAMES}:
            raise ValueError("Private identity/authentication query fields are refused; use an approved browser or local file")
    host = parts.hostname.lower().rstrip(".")
    if host == "localhost" or host.endswith(".localhost"):
        raise ValueError("This fetch helper accepts public targets only")
    try:
        addresses = [ipaddress.ip_address(host)]
    except ValueError:
        if "." not in host:
            raise ValueError("A public hostname is required")
        if not resolve_dns:
            return parts
        addresses = [ipaddress.ip_address(entry[4][0]) for entry in socket.getaddrinfo(host, parts.port or (443 if parts.scheme == "https" else 80), type=socket.SOCK_STREAM)]
    if not addresses or any(not address.is_global for address in addresses):
        raise ValueError("Private, loopback, link-local and reserved network addresses are refused")
    return parts


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, new_url):
        return None


def fetch_public(url, output, maximum=MAX_BYTES):
    validate_public_url(url)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    record = {"url": url, "observed_at": datetime.now(timezone.utc).isoformat(),
              "mode": "public read-only; no redirects or target execution"}
    request = Request(url, headers={"User-Agent": "ROE-Evidence/1.0"})
    try:
        with build_opener(NoRedirects).open(request, timeout=30) as response:
            data = response.read(maximum + 1)
            if len(data) > maximum:
                raise ValueError(f"Response exceeds {maximum} bytes")
            # Store as data, regardless of a server-supplied filename.
            target = output / "artifact.bin"
            target.write_bytes(data)
            record.update(status=response.status, content_type=response.headers.get("Content-Type"), path=str(target), **identity(data))
    except HTTPError as error:
        record.update(status=error.code, error=f"HTTP {error.code}; redirects are not followed" if 300 <= error.code < 400 else f"HTTP {error.code}")
        error.close()
    except Exception as error:
        record.update(status=None, error=str(error))
    (output / "manifest.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ["identify", "json", "hash"]:
        command = commands.add_parser(name)
        command.add_argument("file", type=Path)
        if name == "hash":
            command.add_argument("--algorithm", choices=["sha256", "fnv1a32"], default="sha256")
    fetch = commands.add_parser("fetch", help="Read a public URL into a NEW isolated directory")
    fetch.add_argument("url")
    fetch.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.command == "fetch":
            result = fetch_public(args.url, args.out)
            print(json.dumps(result, indent=2))
            if result.get("status") != 200:
                parser.exit(1)
        else:
            data = read_limited(args.file)
            if args.command == "identify":
                print(json.dumps(identity(data), indent=2))
            elif args.command == "json":
                print(json.dumps({**identity(data), **json_summary(strict_json(data))}, indent=2))
            else:
                print(hashlib.sha256(data).hexdigest() if args.algorithm == "sha256" else fnv1a32(data))
    except (ValueError, OSError, RecursionError) as error:
        parser.exit(1, f"Evidence helper: {error}\n")


if __name__ == "__main__":
    main()
