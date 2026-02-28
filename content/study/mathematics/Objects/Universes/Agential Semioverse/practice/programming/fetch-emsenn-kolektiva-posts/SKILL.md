---

skill_spec_version: "1"
id: fetch-emsenn-kolektiva-posts-skill
name: fetch-emsenn-kolektiva-posts
summary: Fetch recent posts from @emsenn@kolektiva.social and store them in the library.
description: Fetch recent posts from @emsenn@kolektiva.social and store them in the library. Use when refreshing the emsenn kolektiva archive.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- fediverse
dependencies:
- /mathematics/objects/agential-semioverse/practice/programming/fetch-fediverse-posts/SKILL.md
runtime:
  entrypoint: scripts/fetch-fediverse-posts.py
  language: python
  invocation: cli
inputs:
  - name: limit
    type: integer
    description: Number of posts to fetch (keep small, e.g., <=10)
    required: false
    default: 10
  - name: output_dir
    type: string
    description: Directory to store JSON under library/
    required: true
outputs:
  - name: saved_paths
    type: array
    description: Paths of saved JSON files
---

- Run the fediverse fetch script with `--acct emsenn@kolektiva.social`.
- Use `--limit 10` or fewer.
- Save to `/agents/emsenn/content/emsenn-fediverse-kolektiva/kolektiva/`.
