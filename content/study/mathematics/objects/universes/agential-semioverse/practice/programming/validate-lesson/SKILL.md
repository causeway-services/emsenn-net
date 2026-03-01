---

skill_spec_version: "1"
id: validate-lesson-skill
name: validate-lesson
summary: Validate a lesson file for required frontmatter fields and structure.
description: Validate a lesson file for required frontmatter fields and structure. Use when checking lesson quality.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-30
tags:
- programming
runtime:
  entrypoint: scripts/validate-lesson.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Lesson markdown path under library/
    required: true
  - name: json
    type: boolean
    description: Emit JSON result
    required: false
    default: true
outputs:
  - name: issues
    type: array
    description: Validation findings
---

- Run the script: `scripts/validate-lesson.py`
- Provide `--path` to the lesson markdown file.
- Use `--json` for machine-readable output.
