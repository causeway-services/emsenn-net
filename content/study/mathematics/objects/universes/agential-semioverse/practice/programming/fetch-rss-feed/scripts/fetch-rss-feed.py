#!/usr/bin/env python3
from __future__ import annotations

import argparse
import time
from pathlib import Path
from urllib.request import urlopen


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--prefix", default="rss")
    args = parser.parse_args()

    with urlopen(args.url) as response:
        content = response.read()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_path = output_dir / f"{args.prefix}-{timestamp}.xml"
    output_path.write_bytes(content)
    print(str(output_path))


if __name__ == "__main__":
    main()
