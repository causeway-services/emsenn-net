---

skill_spec_version: "1"
id: create-lesson-skill
name: create-lesson
summary: Create a lesson Markdown file with required frontmatter and template content.
description: Create a lesson Markdown file with required frontmatter and template content. Use when adding lessons to curricula.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-30
tags:
- programming
runtime:
  entrypoint: scripts/create-lesson.py
  language: python
  invocation: cli
inputs:
  - name: path
    type: string
    description: Lesson file path (relative to library/)
    required: true
  - name: title
    type: string
    description: Lesson title
    required: true
  - name: id
    type: string
    description: Lesson id for frontmatter
    required: true
  - name: dependency
    type: string
    description: Optional prerequisite lesson id
    required: false
  - name: dry_run
    type: boolean
    description: Preview without writing files
    required: false
    default: false
outputs:
  - name: created_path
    type: path
    description: Path of the created lesson file
---

- Run the script: `scripts/create-lesson.py`
- Provide `--path`, `--title`, and `--id`.
- Use `--dependency` to list prerequisite lessons.
- Use `--dry-run` to preview without writing files.
