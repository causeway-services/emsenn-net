#!/usr/bin/env python3
"""List available skills in the library."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


def find_library_root(explicit: str | None = None) -> Path:
    if explicit:
        return Path(explicit).resolve()
    for parent in [Path.cwd(), *Path.cwd().parents, *Path(__file__).resolve().parents]:
        if parent.name == "library":
            return parent
    raise RuntimeError("library root not found; pass --library-root")


LIBRARY_ROOT = find_library_root()
FRONTMATTER_BOUNDARY = "---"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List available skills")
    parser.add_argument(
        "--library-root",
        type=str,
        default=None,
        help="Path to the library/ directory (optional)",
    )
    parser.add_argument(
        "--domain",
        type=str,
        default=None,
        help="Filter by capability domain",
    )
    parser.add_argument(
        "--kind",
        type=str,
        default=None,
        help="Filter by skill kind",
    )
    parser.add_argument(
        "--provides",
        type=str,
        default=None,
        help="Filter by what the skill provides",
    )
    parser.add_argument(
        "--consumes",
        type=str,
        default=None,
        help="Filter by what the skill consumes",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Include full skill details",
    )
    parser.add_argument(
        "--output",
        choices=["json", "text"],
        default="json",
        help="Output format",
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


def find_skills() -> list[tuple[Path, dict[str, Any]]]:
    """Find all SKILL.md files in the library."""
    skills = []

    for skill_file in LIBRARY_ROOT.rglob("SKILL.md"):
        frontmatter = read_frontmatter(skill_file)
        if frontmatter:
            skills.append((skill_file, frontmatter))

    return skills


def matches_filter(
    skill: dict[str, Any],
    domain: str | None,
    kind: str | None,
    provides: str | None,
    consumes: str | None,
) -> bool:
    """Check if a skill matches the given filters."""
    if kind and skill.get("kind") != kind:
        return False
    
    capabilities = skill.get("capabilities", {})
    
    if domain:
        domains = capabilities.get("domains", [])
        if domain not in domains:
            return False
    
    if provides:
        skill_provides = capabilities.get("provides", [])
        if provides not in skill_provides:
            return False
    
    if consumes:
        skill_consumes = capabilities.get("consumes", [])
        if consumes not in skill_consumes:
            return False
    
    return True


def format_skill(
    path: Path,
    frontmatter: dict[str, Any],
    verbose: bool,
) -> dict[str, Any]:
    """Format a skill for output."""
    skill_dir = path.parent
    relative_path = skill_dir.relative_to(LIBRARY_ROOT)
    
    if verbose:
        result = {
            "id": frontmatter.get("id"),
            "name": frontmatter.get("name"),
            "summary": frontmatter.get("summary") or frontmatter.get("description"),
            "path": str(relative_path),
            "kind": frontmatter.get("kind"),
            "skill_kind": frontmatter.get("skill_kind"),
            "version": frontmatter.get("version", "0.1.0"),
            "runtime": frontmatter.get("runtime"),
            "inputs": frontmatter.get("inputs", []),
            "outputs": frontmatter.get("outputs", []),
            "capabilities": frontmatter.get("capabilities", {}),
            "tags": frontmatter.get("tags", []),
        }
    else:
        result = {
            "id": frontmatter.get("id"),
            "name": frontmatter.get("name"),
            "summary": frontmatter.get("summary") or frontmatter.get("description"),
            "path": str(relative_path),
            "kind": frontmatter.get("kind"),
        }
    
    return result


def main() -> None:
    args = parse_args()
    global LIBRARY_ROOT
    LIBRARY_ROOT = find_library_root(args.library_root)

    all_skills = find_skills()
    
    filtered_skills = [
        (path, fm)
        for path, fm in all_skills
        if matches_filter(fm, args.domain, args.kind, args.provides, args.consumes)
    ]
    
    formatted = [
        format_skill(path, fm, args.verbose)
        for path, fm in filtered_skills
    ]
    
    formatted.sort(key=lambda x: x.get("id") or "")
    
    output = {
        "total": len(formatted),
        "skills": formatted,
    }
    
    if args.output == "json":
        print(json.dumps(output, indent=2))
    else:
        print(f"Found {len(formatted)} skills:")
        print()
        for skill in formatted:
            print(f"  [{skill.get('kind', 'skill')}] {skill['id']}")
            print(f"        {skill.get('name', '')}")
            if skill.get("summary"):
                print(f"        {skill['summary'][:60]}...")
            print()


if __name__ == "__main__":
    main()
