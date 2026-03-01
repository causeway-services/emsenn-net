#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def resolve_library_root() -> Path:
    env_root = Path(os.environ.get("LIBRARY_ROOT", "library"))
    if env_root.is_absolute():
        return env_root.resolve()
    return (Path.cwd() / env_root).resolve()


def resolve_path(library_root: Path, raw_path: str) -> Path:
    raw = raw_path.strip()
    if raw.startswith("/"):
        raw = raw[1:]
    if raw.startswith("library/"):
        relative = Path(raw).relative_to("library")
    else:
        relative = Path(raw)
    candidate = (library_root / relative).resolve()
    if not candidate.is_relative_to(library_root):
        raise ValueError("path outside library root")
    return candidate


def append_log(script_dir: Path, payload: dict) -> None:
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    log_path = script_dir / "run-log.jsonl"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--skill-kind", required=True)
    parser.add_argument("--author", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        target_dir = resolve_path(library_root, args.path)
        skill_name = args.name.strip()
        authors = args.author or ["gpt-5.2-codex"]
        skill_md = target_dir / "SKILL.md"
        scripts_dir = target_dir / "scripts"
        frontmatter = "---\n" + "\n".join(
            [
                f"name: {skill_name}",
                f"description: {args.description}",
                "kind: agent-skill",
                f"skill-kind: {args.skill_kind}",
                "authors:",
                *[f"- {author}" for author in authors],
                f"date-created: {datetime.now(timezone.utc).date().isoformat()}",
                f"id: {skill_name}",
                "---\n",
            ]
        )
        body = f"# {skill_name}\n"
        result = {
            "path": str(target_dir.relative_to(library_root)),
            "skill_md": str(skill_md.relative_to(library_root)),
            "scripts_dir": str(scripts_dir.relative_to(library_root)),
            "dry_run": args.dry_run,
        }
        if not args.dry_run:
            scripts_dir.mkdir(parents=True, exist_ok=True)
            skill_md.write_text(frontmatter + body, encoding="utf-8")
        payload["result"] = result
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print(payload["result"]["skill_md"])


if __name__ == "__main__":
    main()
