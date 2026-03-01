---

skill_spec_version: "1"
id: library-api-links-skill
name: library-api-links
summary: Extract markdown links from a file or directory.
description: Extract markdown links from a file or a directory. Use when clients need link graphs or backlink calculations.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-31
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/extract-links.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: File or directory under library/
    required: true
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: links
    type: array
    description: Extracted link records
---
- Run the script: `scripts/extract-links.py`
- Provide `--path` or `--root` (library-relative).
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-links/execute with {"inputs": {...}}.
