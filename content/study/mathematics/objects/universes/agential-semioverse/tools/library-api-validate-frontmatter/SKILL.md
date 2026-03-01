---

skill_spec_version: "1"
id: library-api-validate-frontmatter-skill
name: library-api-validate-frontmatter
summary: Validate markdown frontmatter and emit JSON results.
description: Validate markdown frontmatter via JSON output for API use. Use when remote agents need structured validation results.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-31
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/validate-frontmatter-json.py
  language: python
  invocation: cli
inputs:
  - name: paths
    type: array
    description: File or directory paths under library/ to validate
    required: true
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: valid
    type: boolean
    description: Whether frontmatter validates
  - name: errors
    type: array
    description: Validation errors, if any
---
- Run the script: `scripts/validate-frontmatter-json.py`
- Provide one or more paths (file or directory).
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-validate-frontmatter/execute with {"inputs": {...}}.
