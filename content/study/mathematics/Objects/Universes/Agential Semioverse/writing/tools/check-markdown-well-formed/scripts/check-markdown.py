#!/usr/bin/env python3
import argparse
import sys
import tomllib
from pathlib import Path

import yaml


def extract_frontmatter(text: str):
    if not text.startswith("---"):
        return None, None, "missing_frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None, "unterminated_frontmatter"
    fm_text = parts[1].strip()
    body = parts[2]
    return fm_text, body, None


def first_h1(body: str):
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def load_repo_name(repo_root: Path) -> str:
    pyproject = repo_root / "pyproject.toml"
    if not pyproject.exists():
        return "repository"
    data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    return data.get("project", {}).get("name", "repository")


def check_file(path: Path, repo_root: Path, repo_name: str):
    text = path.read_text(encoding="utf-8")
    fm_text, body, err = extract_frontmatter(text)
    if err:
        return [err]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        return [f"invalid_yaml: {e}"]
    issues = []
    title = fm.get("title")
    name = fm.get("name")
    h1 = first_h1(body or "")
    is_skill = path.name == "SKILL.md" or fm.get("kind") in {"skill", "agent-skill"}
    if not title and not name:
        issues.append("missing_title_or_name")
    if not is_skill:
        if not h1:
            issues.append("missing_h1")
        if title and h1 and title != h1:
            issues.append("title_h1_mismatch")
    # Naming conventions
    if path.name == "SKILL.md":
        parent = path.parent.name
        if name and name != parent:
            issues.append("skill_name_dir_mismatch")
        if not name:
            issues.append("missing_name_for_skill")
        expected_id = f"{parent}-skill"
        if fm.get("id") and fm.get("id") != expected_id:
            issues.append("skill_id_dir_mismatch")
    if path.name == "README.md":
        if path.parent == repo_root:
            expected = f"{repo_name}-readme"
            alternates = []
        else:
            parent = path.parent.name
            expected = f"{parent}-readme"
            alternates = []
            if path.parent.parent != repo_root:
                alternates.append(f"{path.parent.parent.name}-{parent}-readme")
            if parent in {"skills", "log"} and alternates:
                expected = alternates[0]
                alternates = []
        if fm.get("id") and fm.get("id") not in {expected, *alternates}:
            issues.append("readme_id_mismatch")
    if path.name in {"IDEAS.md", "PLANS.md", "GLOSSARY.md"}:
        if path.parent == repo_root:
            parent = repo_name
        else:
            parent = path.parent.name
        suffix = path.stem.lower()
        expected = f"{parent}-{suffix}"
        if parent == suffix and path.parent.parent != repo_root:
            expected = f"{path.parent.parent.name}-{suffix}"
        if fm.get("id") and fm.get("id") != expected:
            issues.append("index_id_mismatch")
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", default=["library"])
    args = parser.parse_args()

    failures = []
    repo_root = Path.cwd().resolve()
    repo_name = load_repo_name(repo_root)
    for root in args.paths:
        root_path = Path(root)
        if root_path.is_file():
            candidates = [root_path]
        else:
            candidates = list(root_path.rglob("*.md"))
        for path in candidates:
            if path.parts[:3] == ("library", "inbox", "triage"):
                continue
            if "products" in path.parts:
                continue
            issues = check_file(path, repo_root, repo_name)
            if issues:
                failures.append((path, issues))

    if failures:
        for path, issues in failures:
            print(f"{path}: {', '.join(issues)}")
        sys.exit(1)
    print("markdown ok")


if __name__ == "__main__":
    main()
