---

skill_spec_version: "1"
id: make-directory-skill
name: make-directory
summary: Create a directory under the library root.
description: Create a directory path under the library root and return an effect report.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2026-01-09
tags:
  - library-kernel
  - filesystem
runtime:
  entrypoint: scripts/make-directory.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Library-relative directory path to create
    required: true
  - name: parents
    type: boolean
    description: Create parent directories if needed
    required: false
    default: true
  - name: exist_ok
    type: boolean
    description: Do not error if the directory already exists
    required: false
    default: true
outputs:
  - name: result
    type: object
    description: Creation result and effect report
---

- Returns JSON on stdout.
- Honors `LIBRARY_ROOT` for the root directory (defaults to `library`).
