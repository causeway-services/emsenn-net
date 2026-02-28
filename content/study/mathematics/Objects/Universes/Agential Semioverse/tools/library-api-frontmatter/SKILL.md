---

skill_spec_version: "1"
id: library-api-frontmatter-skill
name: library-api-frontmatter
summary: Extract YAML frontmatter from a library markdown file.
description: Extract YAML frontmatter from a library markdown file. Use when remote agents need metadata without full file contents.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-31
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/extract-frontmatter.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Markdown file path under library/
    required: true
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: frontmatter
    type: object
    description: Parsed YAML frontmatter
---
- Run the script: `scripts/extract-frontmatter.py`
- Provide `--path` to a markdown file.
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-frontmatter/execute with {"inputs": {...}}.
