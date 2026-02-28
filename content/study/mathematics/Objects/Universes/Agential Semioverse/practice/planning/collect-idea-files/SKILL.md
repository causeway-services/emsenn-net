---

skill_spec_version: "1"
id: collect-idea-files-skill
name: collect-idea-files
summary: List idea documents stored under /ideas with their titles.
description: List idea documents stored under /ideas with their titles. Use when you need a quick index of idea files.
kind: skill
skill_kind: planning
authors:
  - gpt-5.2-codex
date-created: 2025-12-26
runtime:
  entrypoint: scripts/collect-idea-files.py
  language: python
  invocation: cli
inputs:
  - name: root
    type: string
    description: "Optional root path to search (default: ideas/)"
    required: false
outputs:
  - name: idea_files
    type: array
    description: List of idea file paths and titles
---

- Run: `scripts/collect-idea-files.py`
- If ideas are stored elsewhere, pass `--root <path>`.
