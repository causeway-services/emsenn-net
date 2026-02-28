#!/usr/bin/env python3
"""Wrapper to run the repository Markdown well-formedness checker."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def find_repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "library").exists():
            return parent
    return Path.cwd().resolve()


def main() -> int:
    repo_root = find_repo_root()
    checker = repo_root / "library/media/writing/tools/check-markdown-well-formed/scripts/check-markdown.py"
    if not checker.exists():
        print("checker script not found", file=sys.stderr)
        return 1

    cmd = [sys.executable, str(checker), *sys.argv[1:]]
    result = subprocess.run(cmd, cwd=repo_root)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
