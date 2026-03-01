---

skill_spec_version: "1"
id: library-api-frontmatter-search-skill
name: library-api-frontmatter-search
summary: Search frontmatter by key/value across markdown files.
description: Search frontmatter by key and value across markdown files. Use when clients need key/value filtering beyond tag and kind queries.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-31
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/frontmatter-search.py
  language: python
  invocation: cli
inputs:
  - name: key
    type: string
    description: Frontmatter key to match
    required: true
  - name: value
    type: string
    description: Value substring to match
    required: true
  - name: path
    type: string
    description: Optional subpath to limit search
    required: false
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: matches
    type: array
    description: Matching files with frontmatter snippets
---
- Run the script: `scripts/frontmatter-search.py`
- Provide `--key` and `--value`, plus optional `--root` and `--contains`.
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-frontmatter-search/execute with {"inputs": {...}}.
