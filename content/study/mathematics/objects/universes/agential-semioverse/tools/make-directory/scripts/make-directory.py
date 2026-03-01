#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--parents", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--exist-ok", action=argparse.BooleanOptionalAction, default=True)
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

    existed = target.exists()
    if existed and not args.exist_ok:
        raise SystemExit("path already exists")

    if not existed:
        target.mkdir(parents=args.parents, exist_ok=args.exist_ok)

    rel_path = str(target.relative_to(library_root))
    created_paths = [] if existed else [rel_path]
    result = {
        "path": rel_path,
        "created": not existed,
        "effect_report": {
            "created_paths": created_paths,
            "modified_paths": [],
            "moved_paths": [],
            "hashes": {},
        },
    }
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
