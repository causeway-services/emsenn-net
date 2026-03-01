#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--content", required=True)
    parser.add_argument("--dry-run", action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args()

    library_root = Path(os.environ.get("LIBRARY_ROOT", "library"))
    if not library_root.is_absolute():
        library_root = (Path.cwd() / library_root).resolve()

    raw = args.path.strip()
    if raw.startswith("/"):
        raw = raw[1:]
    if raw.startswith("library/"):
        raw = raw[len("library/"):]

    target = (library_root / raw).resolve()
    if not target.is_relative_to(library_root):
        raise SystemExit("path outside library root")

    previous_exists = target.exists()
    previous_content = target.read_text(encoding="utf-8") if previous_exists else ""
    changed = previous_content != args.content

    if changed and not args.dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(args.content, encoding="utf-8")

    data = args.content.encode("utf-8") if changed else previous_content.encode("utf-8")
    digest = hashlib.sha256(data).hexdigest()
    rel_path = str(target.relative_to(library_root))

    created_paths = []
    modified_paths = []
    if changed:
        if previous_exists:
            modified_paths.append(rel_path)
        else:
            created_paths.append(rel_path)

    result = {
        "path": rel_path,
        "changed": changed,
        "previous_exists": previous_exists,
        "dry_run": args.dry_run,
        "bytes_written": len(args.content.encode("utf-8")) if changed and not args.dry_run else 0,
        "hash": digest,
        "effect_report": {
            "created_paths": created_paths,
            "modified_paths": modified_paths,
            "moved_paths": [],
            "hashes": {rel_path: digest},
        },
    }
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
