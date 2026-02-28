#!/usr/bin/env python3
import argparse
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", required=True)
    parser.add_argument("--context", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--templates-dir",
        default="library/mathematics/objects/agential-semioverse/tools/markdown-templates/templates",
    )
    args = parser.parse_args()

    templates_dir = Path(args.templates_dir)
    env = Environment(loader=FileSystemLoader(str(templates_dir)), autoescape=False)
    template = env.get_template(args.template)

    with open(args.context, "r", encoding="utf-8") as f:
        context = yaml.safe_load(f) or {}

    output = template.render(**context)
    Path(args.output).write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
