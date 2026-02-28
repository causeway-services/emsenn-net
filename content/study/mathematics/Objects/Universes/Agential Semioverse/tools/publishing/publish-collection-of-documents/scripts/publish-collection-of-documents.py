#!/usr/bin/env python3
"""Publish a document collection using MkDocs."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a MkDocs site from a provided mkdocs.yaml.",
    )
    parser.add_argument(
        "config",
        type=Path,
        help="Path to mkdocs.yaml",
    )
    args = parser.parse_args()

    config_path = args.config.resolve()
    if not config_path.exists():
        raise SystemExit(f"missing mkdocs config: {config_path}")
    if not config_path.is_file():
        raise SystemExit(f"mkdocs config is not a file: {config_path}")

    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "-f", str(config_path)],
        check=True,
    )


if __name__ == "__main__":
    main()
