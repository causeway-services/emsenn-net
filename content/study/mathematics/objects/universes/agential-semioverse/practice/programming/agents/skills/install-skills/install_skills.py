#!/usr/bin/env python3
"""Install skills by copying skill folders into ./.codex/skills."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from typing import Iterable

SKILL_FILENAME = "SKILL.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy skill folders into ./.codex/skills.",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("library"),
        help="Path to scan for SKILL.md (default: ./library)",
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path(".codex/skills"),
        help="Destination skills directory (default: ./.codex/skills)",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove existing destination skill folders before copying",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be installed without copying",
    )
    return parser.parse_args()


def iter_skill_dirs(root: Path) -> Iterable[Path]:
    for skill_file in root.rglob(SKILL_FILENAME):
        yield skill_file.parent


def copy_skill_dir(source: Path, destination: Path, clean: bool) -> None:
    if destination.exists() and clean:
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)


def main() -> None:
    args = parse_args()
    source_root = args.source.resolve()
    destination_root = args.destination.resolve()

    if not source_root.exists():
        raise SystemExit(f"missing source directory: {source_root}")

    skill_dirs = sorted(iter_skill_dirs(source_root))
    if not skill_dirs:
        raise SystemExit(f"no skills found under {source_root}")

    for skill_dir in skill_dirs:
        skill_name = skill_dir.name
        destination = destination_root / skill_name
        if args.dry_run:
            print(f"dry-run: {skill_dir} -> {destination}")
        else:
            copy_skill_dir(skill_dir, destination, args.clean)

    if args.dry_run:
        print(f"Dry-run complete for {len(skill_dirs)} skill(s)")
    else:
        print(f"Installed {len(skill_dirs)} skill(s) to {destination_root}")


if __name__ == "__main__":
    main()
