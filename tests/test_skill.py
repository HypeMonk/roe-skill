"""Offline checks for the skill package. Run: python -I -B tests/test_skill.py"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
E, I = load("evidence"), load("install")

class SkillTests(unittest.TestCase):
    def test_metadata(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        header = re.match(r"---\n(.*?)\n---\n", text, re.S)[1]
        self.assertEqual(re.search(r"^name: (.+)$", header, re.M)[1], "roe-skill")
        self.assertTrue(1 <= len(re.search(r"^description: (.+)$", header, re.M)[1]) <= 1024)
        self.assertLess(len(text.splitlines()), 500)
    def test_references(self):
        for file in ROOT.rglob("*.md"):
            if ".git" in file.parts: continue
            for target in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
                if not target.startswith(("https://", "http://", "#")):
                    self.assertTrue((file.parent / target.split("#")[0]).is_file(), target)
    def test_git_metadata_is_not_installable(self):
        _, files = I.source_inventory(ROOT)
        self.assertTrue(files)
        self.assertTrue(all(not set(item["relative"].split("/")) & {".git", "tests", "__pycache__"} for item in files))
    def test_hash_vectors(self):
        self.assertEqual(E.identity(b"hello")["sha256"], hashlib.sha256(b"hello").hexdigest())
        self.assertEqual(E.fnv1a32(b"hello"), "fnv1a32:4f9f2cab")
        self.assertEqual(E.fnv1a32(b""), "fnv1a32:811c9dc5")
    def test_strict_json(self):
        for data in [b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":', b'\xff']:
            with self.assertRaises(ValueError): E.strict_json(data)
    def test_lossless_json(self):
        data = E.strict_json(b'\xef\xbb\xbf{"n":9007199254740993,"a":124.50}')
        self.assertEqual(data["n"], 9007199254740993)
        self.assertEqual(str(data["a"]), "124.50")
        self.assertEqual(len(E.json_summary(data)["unsafe_js_integer_paths_first_20"]), 1)
    def test_boolean(self):
        self.assertEqual(E.json_summary([True])["unsafe_js_integer_paths_first_20"], [])
    def test_file_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "data"
            file.write_bytes(b"12345")
            with self.assertRaises(ValueError): E.read_limited(file, 4)
    def test_private_urls(self):
        for url in ["file:///x", "http://127.0.0.1/a", "http://localhost/a", "http://169.254.169.254/a", "https://u:p@example.org/a", "https://example.org/a?quizSign=x", "https://example.org/a?email=x", "https://example.org/a#x"]:
            with self.assertRaises(ValueError): E.validate_public_url(url, resolve_dns=False)
    def test_dns_private(self):
        with patch.object(E.socket, "getaddrinfo", return_value=[(2,1,6,"",("10.0.0.1",443))]):
            with self.assertRaises(ValueError): E.validate_public_url("https://example.org/a")
    def test_redirect(self):
        self.assertIsNone(E.NoRedirects().redirect_request(None,None,302,"Found",{},"https://example.org/a"))
    def test_public_bytes_not_executed(self):
        class Response:
            status=200; headers={"Content-Type":"text/javascript"}
            def __enter__(self): return self
            def __exit__(self,*args): return False
            def read(self,size): return b"throw new Error('data only')"
        class Opener:
            def open(self,*args,**kwargs): return Response()
        with tempfile.TemporaryDirectory() as tmp, patch.object(E,"validate_public_url"), patch.object(E,"build_opener",return_value=Opener()):
            out=Path(tmp)/"fresh"; result=E.fetch_public("https://example.org/a",out)
            self.assertEqual(result["status"],200)
            self.assertEqual((out/"artifact.bin").read_bytes(),b"throw new Error('data only')")
            with self.assertRaises(FileExistsError): E.fetch_public("https://example.org/a",out)
    def test_current_project_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths=I.targets("all","project",tmp)
            self.assertEqual(len(paths),2)
            self.assertEqual(paths[1]["agents"],["codex","antigravity"])
    def test_user_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths=I.targets("all","user",home=tmp)
            self.assertEqual(len(paths),3)
            self.assertEqual(paths[2]["path"],Path(tmp).resolve()/".gemini/config/skills/roe-skill")
    def test_missing_project(self):
        with self.assertRaises(ValueError): I.targets("claude","project")
    def test_unknown_agent(self):
        with self.assertRaises(ValueError): I.targets("bad","user")
    def test_dry_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            I.install(ROOT,I.targets("all","project",tmp))
            self.assertEqual(list(Path(tmp).iterdir()),[])
    def test_apply(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths=I.targets("claude","project",tmp); I.install(ROOT,paths,True)
            _,files=I.source_inventory(ROOT)
            for item in files:
                self.assertEqual(hashlib.sha256((paths[0]["path"]/item["relative"]).read_bytes()).hexdigest(),item["sha256"])
            self.assertFalse((paths[0]["path"]/".git").exists())
    def test_existing_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths=I.targets("all","project",tmp); paths[1]["path"].mkdir(parents=True)
            sentinel=paths[1]["path"]/"SKILL.md"; sentinel.write_text("keep")
            with self.assertRaises(FileExistsError): I.install(ROOT,paths,True)
            self.assertEqual(sentinel.read_text(),"keep")
            self.assertFalse(paths[0]["path"].exists())
    def test_self_install(self):
        with self.assertRaises(ValueError): I.install(ROOT,[{"path":ROOT/"nested","agents":["claude"]}],True)
    def test_no_settings_edits(self):
        with tempfile.TemporaryDirectory() as tmp:
            I.install(ROOT,I.targets("all","project",tmp),True)
            self.assertEqual(list(Path(tmp).rglob("settings.json")),[])
            self.assertEqual(list(Path(tmp).rglob("config.toml")),[])

if __name__ == "__main__": unittest.main(verbosity=2)
