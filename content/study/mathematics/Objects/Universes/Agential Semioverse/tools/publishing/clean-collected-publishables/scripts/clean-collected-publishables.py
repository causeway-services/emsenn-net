#!/usr/bin/env python3
"""Remove collected publishables from a products output directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove the collected publishables output directory.",
    )
    parser.add_argument(
        "config",
        type=Path,
        help="Path to publication.yml",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the target path without deleting it",
    )
    return parser.parse_args()


def parse_publication_config(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    config: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            continue
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        config[key.strip()] = raw_value.strip().strip("'\"")
    return config


def resolve_output_root_dir(config: dict[str, str], config_path: Path) -> Path:
    output_root = config.get("output_root_dir")
    if not output_root:
        raise SystemExit("missing publication config key: output_root_dir")
    output_path = Path(output_root)
    if not output_path.is_absolute():
        output_path = (config_path.parent / output_path).resolve()
    return output_path


def main() -> None:
    args = parse_args()
    config_path = args.config.resolve()
    if not config_path.exists():
        raise SystemExit(f"missing publication config: {config_path}")

    config = parse_publication_config(config_path)
    output_root = resolve_output_root_dir(config, config_path)

    if output_root.resolve() == config_path.parent.resolve():
        raise SystemExit("refusing to remove the publication config directory")

    if not output_root.exists():
        print(f"nothing to remove at {output_root}")
        return

    if args.dry_run:
        print(f"would remove {output_root}")
        return

    shutil.rmtree(output_root)
    print(f"removed {output_root}")


if __name__ == "__main__":
    main()
