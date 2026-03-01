---

skill_spec_version: "1"
id: list-directory-skill
name: list-directory
summary: List entries in a library directory.
description: List immediate entries under a library directory and return a structured listing.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2026-01-09
tags:
  - library-kernel
  - filesystem
runtime:
  entrypoint: scripts/list-directory.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Library-relative directory path to list
    required: false
    default: "."
outputs:
  - name: result
    type: object
    description: Directory entries and effect report
---

- Returns JSON on stdout.
- Honors `LIBRARY_ROOT` for the root directory (defaults to `library`).
