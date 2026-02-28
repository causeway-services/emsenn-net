---

skill_spec_version: "1"
id: library-api-list-files-skill
name: library-api-list-files
summary: List library files under a root path with optional extension filters.
description: List library files under a root path with optional extension filters. Use when remote agents need an inventory of library files.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2025-12-31
tags:
  - agential-semioverse
runtime:
  entrypoint: scripts/list-library-files.py
  language: python
  invocation: cli
inputs:
  - name: root
    type: string
    description: Root path to list (relative to library/)
    required: false
  - name: ext
    type: string
    description: Optional file extension filter
    required: false
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: files
    type: array
    description: File entries with path and size
---
- Run the script: `scripts/list-library-files.py`
- Provide `--root` (library-relative) and optional `--ext` filters.
- Use `--json` for machine-readable output.

- HTTP: POST /api/v1/skills/library-api-list-files/execute with {"inputs": {...}}.
