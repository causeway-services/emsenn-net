#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--destination", required=True)
    parser.add_argument("--overwrite", action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args()

    library_root = Path(os.environ.get("LIBRARY_ROOT", "library"))
    if not library_root.is_absolute():
        library_root = (Path.cwd() / library_root).resolve()

    def normalize(raw_path: str) -> Path:
        raw = raw_path.strip()
        if raw.startswith("/"):
            raw = raw[1:]
        if raw.startswith("library/"):
            raw = raw[len("library/"):]
        return (library_root / raw).resolve()

    source = normalize(args.source)
    destination = normalize(args.destination)

    if not source.is_relative_to(library_root) or not destination.is_relative_to(library_root):
        raise SystemExit("path outside library root")
    if not source.exists():
        raise SystemExit("source not found")
    if destination.exists():
        if not args.overwrite:
            raise SystemExit("destination exists")
        if destination.is_dir():
            raise SystemExit("destination is a directory")
        destination.unlink()

    destination.parent.mkdir(parents=True, exist_ok=True)
    source.rename(destination)

    rel_source = str(source.relative_to(library_root))
    rel_destination = str(destination.relative_to(library_root))
    hashes = {}
    if destination.is_file():
        digest = hashlib.sha256(destination.read_bytes()).hexdigest()
        hashes[rel_destination] = digest

    result = {
        "source": rel_source,
        "destination": rel_destination,
        "effect_report": {
            "created_paths": [],
            "modified_paths": [],
            "moved_paths": [{"from": rel_source, "to": rel_destination}],
            "hashes": hashes,
        },
    }
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
