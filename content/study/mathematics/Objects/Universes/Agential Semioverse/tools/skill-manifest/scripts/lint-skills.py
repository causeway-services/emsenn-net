#!/usr/bin/env python3
"""Lint SKILL.md files against Skill Spec v1 schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError

SCRIPT_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = SCRIPT_DIR.parent / "specs" / "skill-spec-v1.schema.json"
def find_library_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if parent.name == "library":
            return parent
    raise RuntimeError("library root not found")

LIBRARY_ROOT = find_library_root()
FRONTMATTER_BOUNDARY = "---"


def read_frontmatter(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    if not text.startswith(FRONTMATTER_BOUNDARY):
        return {}
    parts = text.split(FRONTMATTER_BOUNDARY)
    if len(parts) < 3:
        return {}
    fm_text = parts[1]
    try:
        return yaml.safe_load(fm_text) or {}
    except Exception:
        return {}


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text())
    errors: list[str] = []
    warnings: list[str] = []
    non_executable = {"manual", "none", "inference", "documentation"}
    for skill_file in LIBRARY_ROOT.rglob("SKILL.md"):
        fm = read_frontmatter(skill_file)
        if not fm:
            warnings.append(f"{skill_file}: missing or invalid frontmatter")
            continue
        if fm.get("kind") not in (None, "skill"):
            warnings.append(f"{skill_file}: kind={fm.get('kind')} (skipping lint)")
            continue
        try:
            validate(instance=fm, schema=schema)
        except ValidationError as exc:
            errors.append(f"{skill_file}: {exc.message}")
            continue
        runtime = fm.get("runtime") or {}
        if not runtime:
            warnings.append(f"{skill_file}: runtime missing")
            continue
        invocation = runtime.get("invocation")
        entrypoint = runtime.get("entrypoint")
        if invocation not in non_executable and not entrypoint:
            errors.append(f"{skill_file}: runtime.entrypoint required for invocation {invocation}")
    if errors:
        print("Skill lint failures:")
        for e in errors:
            print("  -", e)
        return 1
    if warnings:
        print("Skill lint warnings:")
        for w in warnings:
            print("  -", w)
    print("Skills OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
