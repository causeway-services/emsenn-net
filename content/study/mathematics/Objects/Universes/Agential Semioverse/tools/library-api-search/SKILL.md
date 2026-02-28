---

skill_spec_version: "1"
id: library-api-search-skill
name: library-api-search
summary: Search library files using ripgrep and emit JSON results.
description: Search library files using ripgrep and emit JSON results. Use when remote agents need structured search output.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-30
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/search-library.py
  language: python
  invocation: cli
inputs:
  - name: query
    type: string
    description: Search query string
    required: true
  - name: root
    type: string
    description: Optional subpath under library/ to limit search
    required: false
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: results
    type: array
    description: Match entries with path, line, and text
---
- Run the script: `scripts/search-library.py`
- Provide `--query` and optionally `--root`.
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-search/execute with {"inputs": {...}}.
