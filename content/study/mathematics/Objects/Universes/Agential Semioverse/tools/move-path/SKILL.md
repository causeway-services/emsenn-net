---

skill_spec_version: "1"
id: move-path-skill
name: move-path
summary: Move or rename a path under the library root.
description: Move a file or directory to a new location under the library root.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2026-01-09
tags:
  - library-kernel
  - filesystem
runtime:
  entrypoint: scripts/move-path.py
  language: python
  invocation: cli
inputs:
  - name: source
    type: string
    description: Library-relative source path
    required: true
  - name: destination
    type: string
    description: Library-relative destination path
    required: true
  - name: overwrite
    type: boolean
    description: Overwrite destination if it exists
    required: false
    default: false
outputs:
  - name: result
    type: object
    description: Move result and effect report
---

- Returns JSON on stdout.
- Honors `LIBRARY_ROOT` for the root directory (defaults to `library`).
