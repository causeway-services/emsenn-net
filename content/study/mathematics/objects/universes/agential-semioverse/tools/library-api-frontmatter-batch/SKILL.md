---

skill_spec_version: "1"
id: library-api-frontmatter-batch-skill
name: library-api-frontmatter-batch
summary: Extract frontmatter from multiple markdown files in one call.
description: Extract frontmatter from multiple markdown files in one call. Use when clients need metadata for a set of paths.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-31
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/extract-frontmatter-batch.py
  language: python
  invocation: cli
inputs:
  - name: paths
    type: array
    description: List of markdown file paths under library/
    required: true
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: frontmatter
    type: array
    description: Parsed frontmatter for each path
---
- Run the script: `scripts/extract-frontmatter-batch.py`
- Provide `--paths` with one or more library-relative paths.
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-frontmatter-batch/execute with {"inputs": {...}}.
