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
    parser.add_argument("--title", required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--kind", default="readme")
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--author", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        target_dir = resolve_path(library_root, args.path)
        authors = args.author or ["gpt-5.2-codex"]
        tags = args.tag or []
        readme_path = target_dir / "README.md"
        spec_path = target_dir / "SPECIFICATIONS.md"
        curricula_dir = target_dir / "curricula"
        skills_dir = target_dir / "skills"
        tests_dir = target_dir / "tests"
        frontmatter_lines = [
            "---",
            f"title: {args.title}",
            f"id: {args.id}",
            f"kind: {args.kind}",
            "authors:",
            *[f"- {author}" for author in authors],
            f"date-created: {datetime.now(timezone.utc).date().isoformat()}",
        ]
        if tags:
            frontmatter_lines.append("tags:")
            frontmatter_lines.extend([f"- {tag}" for tag in tags])
        frontmatter_lines.append("---")
        readme_content = "\n".join(frontmatter_lines) + f"\n# {args.title}\n"
        spec_content = (
            "---\n"
            f"title: {args.title} Specifications\n"
            f"id: {args.id}-specifications\n"
            "kind: specification\n"
            "authors:\n"
            + "\n".join([f"- {author}" for author in authors])
            + f"\n\ndate-created: {datetime.now(timezone.utc).date().isoformat()}\n---\n\n"
            + f"# {args.title} Specifications\n"
        )
        result = {
            "path": str(target_dir.relative_to(library_root)),
            "readme": str(readme_path.relative_to(library_root)),
            "specifications": str(spec_path.relative_to(library_root)),
            "dry_run": args.dry_run,
        }
        if not args.dry_run:
            curricula_dir.mkdir(parents=True, exist_ok=True)
            skills_dir.mkdir(parents=True, exist_ok=True)
            tests_dir.mkdir(parents=True, exist_ok=True)
            target_dir.mkdir(parents=True, exist_ok=True)
            readme_path.write_text(readme_content, encoding="utf-8")
            spec_path.write_text(spec_content, encoding="utf-8")
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
        print(payload["result"]["readme"])


if __name__ == "__main__":
    main()
