#!/usr/bin/env python3
import argparse
import json
import os
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import yaml
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


def append_log(script_dir: Path, payload: dict) -> None:
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    log_path = script_dir / "run-log.jsonl"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def find_library_root() -> Path:
    env_root = os.environ.get("LIBRARY_ROOT")
    if env_root:
        return Path(env_root).resolve()
    for parent in Path(__file__).resolve().parents:
        if (parent / "library").exists():
            return (parent / "library").resolve()
    return Path("library").resolve()


def default_schema_path() -> Path:
    library_root = find_library_root()
    candidates = [
        library_root
        / "math"
        / "objects"
        / "agential-semioverse"
        / "tools"
        / "frontmatter-schema"
        / "schema.json",
        library_root / "skills" / "writing" / "frontmatter-schema" / "schema.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("frontmatter schema not found in expected locations")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", type=Path, default=None)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("paths", nargs="*", default=["library"])
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    payload = {"args": vars(args), "status": "ok"}

    try:
        schema_path = args.schema or default_schema_path()
        payload["args"]["schema"] = str(schema_path)
        schema = load_schema(schema_path)
        failures = []
        checked = 0
        for root in args.paths:
            root_path = Path(root)
            if root_path.is_file():
                candidates = [root_path]
            else:
                candidates = list(root_path.rglob("*.md"))
            for path in candidates:
                if should_skip(path):
                    continue
                checked += 1
                ok, reason = validate_file(path, schema)
                if not ok:
                    failures.append({"path": str(path), "reason": reason})
        payload["result"] = {"ok": not failures, "checked": checked, "failures": failures}
        if failures:
            payload["status"] = "error"
            payload["error"] = "frontmatter_validation_failed"
    except Exception as exc:
        payload["status"] = "error"
        payload["error"] = str(exc)

    append_log(script_dir, payload)
    if payload["status"] != "ok":
        output = json.dumps(payload["result"], ensure_ascii=True)
        print(output, file=sys.stderr)
        raise SystemExit(payload["error"])
    if args.json:
        print(json.dumps(payload["result"], ensure_ascii=True))
    else:
        print("frontmatter ok")


if __name__ == "__main__":
    main()
