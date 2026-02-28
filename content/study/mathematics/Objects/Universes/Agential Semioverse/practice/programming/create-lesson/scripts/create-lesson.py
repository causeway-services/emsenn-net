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
    parser.add_argument("--description", default="")
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--dependency", action="append", default=[])
    parser.add_argument("--author", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    library_root = resolve_library_root()
    payload: dict = {"args": vars(args), "status": "ok"}

    try:
        target = resolve_path(library_root, args.path)
        authors = args.author or ["gpt-5.2-codex"]
        tags = args.tag or []
        deps = args.dependency or []
        frontmatter_lines = [
            "---",
            f"title: {args.title}",
            f"id: {args.id}",
            "kind: lesson",
            "authors:",
            *[f"- {author}" for author in authors],
            f"date-created: {datetime.now(timezone.utc).date().isoformat()}",
        ]
        if args.description:
            frontmatter_lines.append(f"description: {args.description}")
        if tags:
            frontmatter_lines.append("tags:")
            frontmatter_lines.extend([f"- {tag}" for tag in tags])
        frontmatter_lines.append("dependencies:")
        frontmatter_lines.extend([f"- {dep}" for dep in deps])
        frontmatter_lines.append("---")
        body = "\n".join(
            [
                f"# {args.title}",
                "",
                "## Assumed audience",
                "",
                "- Reading level: general adult.",
                "- Background: TBD.",
                "- Goal: TBD.",
                "",
            ]
        )
        content = "\n".join(frontmatter_lines) + "\n" + body
        result = {
            "path": str(target.relative_to(library_root)),
            "dry_run": args.dry_run,
        }
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
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
        print(payload["result"]["path"])


if __name__ == "__main__":
    main()
