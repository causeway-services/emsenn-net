#!/usr/bin/env python3
"""Build a skill manifest from SKILL.md files."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def find_library_root() -> Path:
    """Locate the library/ directory by walking parents."""
    for parent in Path(__file__).resolve().parents:
        if parent.name == "library":
            return parent
    raise RuntimeError("library root not found")


LIBRARY_ROOT = find_library_root()
FRONTMATTER_BOUNDARY = "---"

REQUIRED_SPEC_V1_FIELDS = ["id", "name", "kind"]
OPTIONAL_SPEC_V1_FIELDS = [
    "skill_spec_version",
    "summary",
    "description",
    "version",
    "skill_kind",
    "authors",
    "date-created",
    "date-updated",
    "tags",
    "runtime",
    "inputs",
    "outputs",
    "capabilities",
    "examples",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build skill manifest")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("skill-manifest.json"),
        help="Path to write the manifest file",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Only validate, don't write output",
    )
    parser.add_argument(
        "--spec-version",
        type=str,
        default=None,
        help="Filter by skill spec version",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        default=True,
        help="Pretty-print JSON output",
    )
    return parser.parse_args()


def read_frontmatter(path: Path) -> dict[str, Any] | None:
    """Read YAML frontmatter from a file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None
    
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        return None
    
    for index in range(1, len(lines)):
        if lines[index].strip() == FRONTMATTER_BOUNDARY:
            frontmatter_text = "\n".join(lines[1:index])
            try:
                data = yaml.safe_load(frontmatter_text)
                if isinstance(data, dict):
                    return data
            except yaml.YAMLError:
                pass
            break
    
    return None


def validate_skill(
    path: Path,
    frontmatter: dict[str, Any],
    spec_version: str | None,
) -> list[str]:
    """Validate a skill against the spec."""
    errors: list[str] = []
    
    skill_spec = frontmatter.get("skill_spec_version")
    if spec_version and skill_spec != spec_version:
        return []
    
    for field in REQUIRED_SPEC_V1_FIELDS:
        if field not in frontmatter:
            errors.append(f"Missing required field: {field}")
    
    skill_id = frontmatter.get("id")
    if skill_id and not isinstance(skill_id, str):
        errors.append("Field 'id' must be a string")
    
    inputs = frontmatter.get("inputs", [])
    if inputs and not isinstance(inputs, list):
        errors.append("Field 'inputs' must be a list")
    else:
        for i, inp in enumerate(inputs):
            if not isinstance(inp, dict):
                errors.append(f"Input {i} must be an object")
            elif "name" not in inp:
                errors.append(f"Input {i} missing 'name' field")
            elif "type" not in inp:
                errors.append(f"Input {i} ({inp.get('name')}) missing 'type' field")
    
    outputs = frontmatter.get("outputs", [])
    if outputs and not isinstance(outputs, list):
        errors.append("Field 'outputs' must be a list")
    else:
        for i, out in enumerate(outputs):
            if not isinstance(out, dict):
                errors.append(f"Output {i} must be an object")
            elif "name" not in out:
                errors.append(f"Output {i} missing 'name' field")
            elif "type" not in out:
                errors.append(f"Output {i} ({out.get('name')}) missing 'type' field")
    
    runtime = frontmatter.get("runtime")
    if runtime:
        if not isinstance(runtime, dict):
            errors.append("Field 'runtime' must be an object")
        else:
            invocation = runtime.get("invocation")
            non_exec = {"manual", "none", "inference", "documentation"}
            if invocation not in non_exec and "entrypoint" not in runtime:
                errors.append("Runtime missing 'entrypoint' field")
            if invocation not in non_exec and "language" not in runtime:
                errors.append("Runtime missing 'language' field")
    
    return errors


def format_skill_entry(
    path: Path,
    frontmatter: dict[str, Any],
) -> dict[str, Any]:
    """Format a skill for the manifest."""
    skill_dir = path.parent
    relative_path = skill_dir.relative_to(LIBRARY_ROOT)
    
    entry: dict[str, Any] = {
        "id": frontmatter.get("id"),
        "name": frontmatter.get("name"),
        "path": str(relative_path),
        "skill_file": str(path.relative_to(LIBRARY_ROOT)),
    }
    
    if "skill_spec_version" in frontmatter:
        entry["skill_spec_version"] = frontmatter["skill_spec_version"]
    
    if "summary" in frontmatter:
        entry["summary"] = frontmatter["summary"]
    elif "description" in frontmatter:
        desc = frontmatter["description"]
        if isinstance(desc, str):
            entry["summary"] = desc[:200].split("\n")[0]
    
    for field in ["kind", "skill_kind", "version", "tags"]:
        if field in frontmatter:
            entry[field] = frontmatter[field]
    
    if "runtime" in frontmatter:
        runtime = frontmatter["runtime"]
        invocation = runtime.get("invocation", "cli")
        non_exec = {"manual", "none", "inference", "documentation"}
        if invocation in non_exec:
            entry["runtime"] = {
                "invocation": invocation,
                "tool": runtime.get("tool"),
                "model": runtime.get("model"),
            }
        else:
            entry["runtime"] = {
                "entrypoint": str(relative_path / runtime.get("entrypoint", "")),
                "language": runtime.get("language"),
                "invocation": invocation,
            }
            if "env_vars" in runtime:
                entry["runtime"]["env_vars"] = runtime["env_vars"]
    
    if "inputs" in frontmatter:
        entry["inputs"] = frontmatter["inputs"]
    
    if "outputs" in frontmatter:
        entry["outputs"] = frontmatter["outputs"]
    
    if "capabilities" in frontmatter:
        entry["capabilities"] = frontmatter["capabilities"]
    
    return entry


def find_skills() -> list[tuple[Path, dict[str, Any]]]:
    """Find all SKILL.md files."""
    skills = []
    
    for skill_file in LIBRARY_ROOT.rglob("SKILL.md"):
        frontmatter = read_frontmatter(skill_file)
        if frontmatter:
            skills.append((skill_file, frontmatter))
    
    return skills


def build_manifest(
    skills: list[tuple[Path, dict[str, Any]]],
    spec_version: str | None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Build the manifest and collect validation errors."""
    entries = []
    all_errors = []
    
    for path, frontmatter in skills:
        errors = validate_skill(path, frontmatter, spec_version)
        
        if errors:
            all_errors.append({
                "path": str(path.relative_to(LIBRARY_ROOT)),
                "errors": errors,
            })
            continue
        
        if spec_version:
            if frontmatter.get("skill_spec_version") != spec_version:
                continue
        
        entry = format_skill_entry(path, frontmatter)
        entries.append(entry)
    
    entries.sort(key=lambda x: x.get("id") or "")
    
    manifest = {
        "version": "1.0.0",
        "spec_version": spec_version or "mixed",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "skill_count": len(entries),
        "skills": entries,
    }
    
    return manifest, all_errors


def main() -> None:
    args = parse_args()
    
    all_skills = find_skills()
    manifest, errors = build_manifest(all_skills, args.spec_version)
    
    if errors:
        print(f"Validation errors in {len(errors)} skills:")
        for error_entry in errors:
            print(f"\n  {error_entry['path']}:")
            for err in error_entry["errors"]:
                print(f"    - {err}")
    
    if args.validate:
        print(f"\nValidated {manifest['skill_count']} skills")
        if errors:
            print(f"Found errors in {len(errors)} skills")
            raise SystemExit(1)
        print("All skills valid")
        return
    
    output_path = args.output
    if not output_path.is_absolute():
        output_path = LIBRARY_ROOT / output_path
    
    indent = 2 if args.pretty else None
    output_path.write_text(json.dumps(manifest, indent=indent), encoding="utf-8")
    
    print(f"Generated manifest with {manifest['skill_count']} skills")
    print(f"Written to: {output_path}")


if __name__ == "__main__":
    main()
