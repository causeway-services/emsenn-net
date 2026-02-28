#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default=".")
    args = parser.parse_args()

    library_root = Path(os.environ.get("LIBRARY_ROOT", "library"))
    if not library_root.is_absolute():
        library_root = (Path.cwd() / library_root).resolve()

    raw = args.path.strip() or "."
    if raw.startswith("/"):
        raw = raw[1:]
    if raw.startswith("library/"):
        raw = raw[len("library/"):]

    target = (library_root / raw).resolve()
    if not target.is_relative_to(library_root):
        raise SystemExit("path outside library root")
    if not target.exists():
        raise SystemExit("path not found")
    if not target.is_dir():
        raise SystemExit("path is not a directory")

    entries = []
    for entry in sorted(target.iterdir(), key=lambda item: item.name):
        rel_entry = str(entry.relative_to(library_root))
        entry_type = "dir" if entry.is_dir() else "file"
        size = None
        mtime = None
        if entry.is_file():
            stat = entry.stat()
            size = stat.st_size
            mtime = stat.st_mtime
        entries.append(
            {
                "path": rel_entry,
                "name": entry.name,
                "type": entry_type,
                "size": size,
                "mtime": mtime,
            }
        )

    result = {
        "path": str(target.relative_to(library_root)),
        "count": len(entries),
        "entries": entries,
        "effect_report": {
            "created_paths": [],
            "modified_paths": [],
            "moved_paths": [],
            "hashes": {},
        },
    }
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
