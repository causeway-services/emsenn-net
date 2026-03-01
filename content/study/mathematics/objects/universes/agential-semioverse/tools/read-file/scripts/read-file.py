#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
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
    if not target.exists():
        raise SystemExit("path not found")

    data = target.read_bytes()
    try:
        content = data.decode("utf-8")
        encoding = "utf-8"
        binary = False
    except UnicodeDecodeError:
        content = base64.b64encode(data).decode("ascii")
        encoding = "base64"
        binary = True

    digest = hashlib.sha256(data).hexdigest()
    stat = target.stat()
    rel_path = str(target.relative_to(library_root))
    result = {
        "path": rel_path,
        "content": content,
        "encoding": encoding,
        "binary": binary,
        "size": stat.st_size,
        "mtime": stat.st_mtime,
        "hash": digest,
        "effect_report": {
            "created_paths": [],
            "modified_paths": [],
            "moved_paths": [],
            "hashes": {rel_path: digest},
        },
    }
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
