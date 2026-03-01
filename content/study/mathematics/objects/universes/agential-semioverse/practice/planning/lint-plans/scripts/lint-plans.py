#!/usr/bin/env python3
"""Lint PLANS.md for required inline fields."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List

INLINE_FIELD = re.compile(r"\[(?P<key>[^:\]]+)::\s*(?P<value>[^\]]+)\]")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lint PLANS.md for inline fields.")
    parser.add_argument("path", type=Path, help="Path to PLANS.md")
    return parser.parse_args()


def extract_fields(line: str) -> List[str]:
    return [match.group("key").strip() for match in INLINE_FIELD.finditer(line)]


def main() -> None:
    args = parse_args()
    path = args.path
    if not path.exists():
        raise SystemExit(f"missing PLANS file: {path}")

    errors: List[str] = []
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.lstrip().startswith("-"):
            continue
        if "[ ]" not in line and "[x]" not in line and "[X]" not in line:
            continue
        fields = extract_fields(line)
        missing = [key for key in ("roles", "goals") if key not in fields]
        if missing:
            errors.append(f"line {idx} missing fields: {', '.join(missing)}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)

    print("ok")


if __name__ == "__main__":
    main()
