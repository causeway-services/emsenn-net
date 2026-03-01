---

skill_spec_version: "1"
id: library-api-write-skill
name: library-api-write
summary: Write to a library file with validation, diff, and dry-run support.
description: Write a file to the library with path validation, diff output, and dry-run support. Use when remote agents submit changes.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-30
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/write-library-file.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Path to write (relative to library/ or absolute under library/)
    required: true
  - name: content
    type: string
    description: Content to write (omit if using stdin)
    required: false
  - name: stdin
    type: boolean
    description: Read content from stdin
    required: false
    default: false
  - name: dry_run
    type: boolean
    description: Preview without writing
    required: false
    default: false
  - name: json
    type: boolean
    description: Emit JSON result instead of diff text
    required: false
    default: false
outputs:
  - name: changed
    type: boolean
    description: Whether the content differs from previous
  - name: diff
    type: string
    description: Unified diff of changes
  - name: path
    type: string
    description: Written file path relative to library/
---
- Run the script: `scripts/write-library-file.py`
- Provide `--path` and content via `--stdin` or `--content`.
- Use `--dry-run` for preview and `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-write/execute with {"inputs": {...}}.
