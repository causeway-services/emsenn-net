---

skill_spec_version: "1"
id: read-file-skill
name: read-file
summary: Read a library file and return content with metadata.
description: Read a file from the library root and return its content and metadata with an effect report.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2026-01-09
tags:
  - library-kernel
  - filesystem
runtime:
  entrypoint: scripts/read-file.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Library-relative path to read
    required: true
outputs:
  - name: result
    type: object
    description: Content, metadata, and effect report
---

- Returns JSON on stdout.
- Honors `LIBRARY_ROOT` for the root directory (defaults to `library`).
