---

skill_spec_version: "1"
id: write-file-skill
name: write-file
summary: Write content to a library file.
description: Write UTF-8 content to a file under the library root and return an effect report.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2026-01-09
tags:
  - library-kernel
  - filesystem
runtime:
  entrypoint: scripts/write-file.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Library-relative path to write
    required: true
  - name: content
    type: string
    description: Content to write (UTF-8)
    required: true
  - name: dry_run
    type: boolean
    description: Preview changes without writing
    required: false
    default: false
outputs:
  - name: result
    type: object
    description: Write result and effect report
---

- Returns JSON on stdout.
- Honors `LIBRARY_ROOT` for the root directory (defaults to `library`).
