---

skill_spec_version: "1"
id: fetch-fediverse-posts-skill
name: fetch-fediverse-posts
summary: Fetch a limited number of public posts from a fediverse account and save them.
description: Fetch a limited number of public posts from a fediverse account and save them to a target directory. Use when collecting recent posts for archival.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- fediverse
- mastodon
runtime:
  entrypoint: scripts/fetch-fediverse-posts.py
  language: python
  invocation: cli
inputs:
  - name: acct
    type: string
    description: Account identifier (user@host) or provide user/host separately
    required: false
  - name: user
    type: string
    description: Fediverse username (if acct not provided)
    required: false
  - name: host
    type: string
    description: Fediverse host (if acct not provided)
    required: false
  - name: limit
    type: integer
    description: Number of posts to fetch (1-20)
    required: false
    default: 5
  - name: output_dir
    type: string
    description: Directory to store JSON under library/
    required: true
outputs:
  - name: saved_paths
    type: array
    description: Paths of saved JSON files
---

- Run the script: `scripts/fetch-fediverse-posts.py`
- Provide `--acct user@host` or `--user` and `--host`.
- Use `--limit` (1-20) and keep it small to be polite.
- Provide `--output-dir` for where to save the JSON.
