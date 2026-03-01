---

skill_spec_version: "1"
id: library-api-read-skill
name: library-api-read
summary: Read a library file with path validation and optional JSON output.
description: Read a file from the library with path validation and JSON output. Use when serving library content to remote agents.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-30
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/read-library-file.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Path to read (relative to library/ or absolute under library/)
    required: true
  - name: json
    type: boolean
    description: Emit JSON result instead of raw content
    required: false
    default: false
outputs:
  - name: content
    type: string
    description: File content (string or base64)
  - name: metadata
    type: object
    description: Path, size, mtime, encoding
---
- Run the script: `scripts/read-library-file.py` (accepts `--path`, optional `--json`)
- Provide `--path` (library-relative or `/library/...`).
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-read/execute with {"inputs": {...}}.
