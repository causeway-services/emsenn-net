---

skill_spec_version: "1"
id: collect-plan-files-skill
name: collect-plan-files
summary: List plan documents stored under /plans with their titles.
description: List plan documents stored under /plans with their titles. Use when you need a quick index of plan files.
kind: skill
skill_kind: planning
authors:
  - gpt-5.2-codex
date-created: 2025-12-26
runtime:
  entrypoint: scripts/collect-plan-files.py
  language: python
  invocation: cli
inputs:
  - name: root
    type: string
    description: "Optional root path to search (default: plans/)"
    required: false
outputs:
  - name: plan_files
    type: array
    description: List of plan file paths and titles
---

- Run: `scripts/collect-plan-files.py`
- If plans are stored elsewhere, pass `--root <path>`.
