#!/usr/bin/env python3
"""Locate the library/ directory starting from CWD."""

from __future__ import annotations

import sys
from pathlib import Path


def find_library_root(start: Path | None = None) -> Path:
    base = start or Path.cwd()
    for parent in [base, *base.parents]:
        if parent.name == "library":
            return parent
    raise SystemExit("library root not found; set LIBRARY_ROOT or run inside repo")


def main() -> None:
    root = find_library_root()
    print(str(root))


if __name__ == "__main__":
    main()
