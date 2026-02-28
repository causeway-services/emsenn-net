#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

import yaml
from datetime import date, datetime
import jsonschema


def extract_frontmatter(text: str):
    if not text.startswith("---"):
        return None, "missing_frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "unterminated_frontmatter"
    return parts[1].strip(), None


def load_schema(schema_path: Path):
    with schema_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def is_skill_doc(path: Path, frontmatter: dict):
    if path.name == "SKILL.md":
        return True
    kind = (frontmatter or {}).get("kind", "")
    return kind in {"skill", "agent-skill"}


def should_skip(path: Path) -> bool:
    return path.parts[:3] == ("library", "inbox", "triage")


def validate_file(path: Path, schema):
    text = path.read_text(encoding="utf-8")
    fm_text, err = extract_frontmatter(text)
    if err:
        return False, err
    try:
        data = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        return False, f"invalid_yaml: {e}"
    for key, value in list(data.items()):
        if isinstance(value, (date, datetime)):
            data[key] = value.isoformat()
    authors = data.get("authors")
    if isinstance(authors, str):
        data["authors"] = [authors]
    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.ValidationError as e:
        return False, f"schema_error: {e.message}"
    if is_skill_doc(path, data):
        if not data.get("name"):
            return False, "missing_name_for_skill"
    return True, None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--schema",
        default="library/mathematics/objects/agential-semioverse/tools/frontmatter-schema/schema.json",
    )
    parser.add_argument("paths", nargs="*", default=["library"])
    args = parser.parse_args()

    schema_path = Path(args.schema)
    schema = load_schema(schema_path)

    failures = []
    for root in args.paths:
        root_path = Path(root)
        if root_path.is_file():
            candidates = [root_path]
        else:
            candidates = list(root_path.rglob("*.md"))
        for path in candidates:
            if should_skip(path):
                continue
            ok, reason = validate_file(path, schema)
            if not ok:
                failures.append((path, reason))

    if failures:
        for path, reason in failures:
            print(f"{path}: {reason}")
        sys.exit(1)

    print("frontmatter ok")


if __name__ == "__main__":
    main()
