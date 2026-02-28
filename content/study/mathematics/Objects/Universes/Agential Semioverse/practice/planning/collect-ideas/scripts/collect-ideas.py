#!/usr/bin/env python3
"""Collect idea headings from IDEAS.md."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List, Dict, Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect idea headings from IDEAS.md.")
    parser.add_argument("path", type=Path, help="Path to IDEAS.md")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write JSON output to a file",
    )
    return parser.parse_args()


def collect_headings(path: Path) -> List[Dict[str, Any]]:
    headings = []
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.startswith("## "):
            title = line[3:].strip()
            if title:
                headings.append({"title": title, "line": idx})
    return headings


def main() -> None:
    args = parse_args()
    entries = collect_headings(args.path)
    payload = {"path": str(args.path), "ideas": entries}
    output = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(output, end="")
    else:
        args.output.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
