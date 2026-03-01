---

skill_spec_version: "1"
id: skill-manifest-skill
name: skill-manifest
summary: Generate a skill manifest from SKILL.md files
description: >
  Scans the library for SKILL.md files conforming to Skill Spec v1,
  validates them, and generates a consolidated skill-manifest.json
  that can be consumed by APIs and MCP servers.
version: "1.0.0"
kind: skill
skill_kind: programming
authors:
  - emsenn
date-created: 2026-01-01
tags:
  - library
  - skills
  - manifest
  - api
runtime:
  entrypoint: scripts/build-skill-manifest.py
  language: python
  invocation: cli
inputs:
  - name: output
    description: Path to write the manifest file
    type: path
    required: false
    default: skill-manifest.json
  - name: validate
    description: Only validate, don't write output
    type: boolean
    required: false
    default: false
  - name: spec_version
    description: Filter by skill spec version
    type: string
    required: false
    default: "1"
outputs:
  - name: manifest_path
    description: Path to the generated manifest
    type: path
  - name: skill_count
    description: Number of skills in the manifest
    type: integer
  - name: validation_errors
    description: List of validation errors (if any)
    type: array
capabilities:
  domains:
    - library
    - skills
    - api
  consumes:
    - skill-definition
  provides:
    - skill-manifest
  composable: true
examples:
  - description: Generate manifest
    inputs:
      output: skill-manifest.json
    expected_output:
      manifest_path: skill-manifest.json
      skill_count: 150
      validation_errors: []
---

# Build Skill Manifest

This skill generates a skill manifest from SKILL.md files in the library.

## Usage

```bash
python scripts/build-skill-manifest.py
python scripts/build-skill-manifest.py --output my-manifest.json
python scripts/build-skill-manifest.py --validate
```

## Output Format

The manifest is a JSON file with:

```json
{
  "version": "1.0.0",
  "generated_at": "2026-01-01T00:00:00Z",
  "skill_count": 150,
  "skills": [
    {
      "id": "browse-library",
      "name": "Browse Library",
      "path": "mathematics/objects/agential-semioverse/tools/browse-library",
      "runtime": { ... },
      "inputs": [ ... ],
      "outputs": [ ... ],
      "capabilities": { ... }
    }
  ]
}
```

## Validation

With `--validate`, the script checks that all skills conform to Skill Spec v1
and reports any errors without writing output.
