"""Install the portable roe-skill folder without editing agent settings.

Default is dry-run. --apply creates a new skill folder; any existing installation
is refused, never overwritten or merged. No downloads, package installs, secrets,
permission changes, or network calls. Run with python -I.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path

NAME = "roe-skill"
PROJECT_ROOTS = {"claude": ".claude/skills", "codex": ".agents/skills", "antigravity": ".agents/skills"}
USER_ROOTS = {"claude": ".claude/skills", "codex": ".agents/skills", "antigravity": ".gemini/config/skills"}


def targets(agent, scope, project=None, home=None):
    if agent not in {"claude", "codex", "antigravity", "all"}:
        raise ValueError("Unknown agent")
    if scope not in {"project", "user"}:
        raise ValueError("Scope must be project or user")
    agents = list(PROJECT_ROOTS) if agent == "all" else [agent]
    if scope == "project":
        if project is None:
            raise ValueError("Project installation requires --project with the actual workspace path")
        base = Path(project).expanduser().resolve()
        if not base.is_dir():
            raise ValueError("The project directory must already exist")
        roots = PROJECT_ROOTS
    else:
        base = Path(home).expanduser().resolve() if home is not None else Path.home()
        if not base.is_dir():
            raise ValueError("The home directory must exist")
        roots = USER_ROOTS
    grouped = {}
    for client in agents:
        destination = base / roots[client] / NAME
        grouped.setdefault(destination, []).append(client)
    return [{"path": destination, "agents": clients} for destination, clients in grouped.items()]


def source_inventory(source):
    source = Path(source).resolve()
    if not (source / "SKILL.md").is_file() or source.name != NAME:
        raise ValueError("Installer source must be the complete roe-skill folder")
    files = []
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if any(part in {".git", "__pycache__", "node_modules", ".github", "tests"} for part in relative.parts) or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError(f"Symlink in skill source is refused: {path.name}")
        if path.is_file():
            if path.name in {".env", "credentials.json"}:
                raise ValueError("Private credential files must not be part of a skill bundle")
            files.append({"relative": relative.as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    return source, files


def install(source, destinations, apply=False):
    source, files = source_inventory(source)
    # Validate every destination before creating any installation.
    for destination in destinations:
        target = Path(destination["path"])
        if os.path.lexists(target):
            raise FileExistsError(f"Existing installation refused: {target}. Inspect/remove it yourself before a replacement.")
        if target == source or source in target.parents:
            raise ValueError("Cannot install a skill into its own source tree")
    report = {"mode": "installed" if apply else "dry-run", "source": str(source), "files": len(files),
              "destinations": [{"path": str(item["path"]), "agents": item["agents"]} for item in destinations],
              "settings_changed": False, "network_used": False}
    if not apply:
        return report
    for destination in destinations:
        target = Path(destination["path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation prevents accidentally merging an existing skill.
        target.mkdir(exist_ok=False)
        for item in files:
            relative = Path(item["relative"])
            output = target / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open("xb") as stream:
                stream.write((source / relative).read_bytes())
            if hashlib.sha256(output.read_bytes()).hexdigest() != item["sha256"]:
                raise OSError(f"Copied file verification failed: {output}")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=["claude", "codex", "antigravity", "all"], required=True)
    parser.add_argument("--scope", choices=["project", "user"], default="project")
    parser.add_argument("--project", type=Path, help="Existing workspace, required for project scope")
    parser.add_argument("--apply", action="store_true", help="Create the proposed new skill folders; default is dry-run")
    args = parser.parse_args()
    try:
        if args.scope == "user" and args.project is not None:
            raise ValueError("--project is not used for user scope")
        source = Path(__file__).resolve().parents[1]
        result = install(source, targets(args.agent, args.scope, args.project), args.apply)
        print(json.dumps(result, indent=2))
        if not args.apply:
            print("No files changed. Add --apply only after reviewing the paths.")
        else:
            print("Installed. Verify the skill appears in your client; reload or restart if needed.")
    except (ValueError, OSError) as error:
        parser.exit(1, f"Skill installer: {error}\n")


if __name__ == "__main__":
    main()
