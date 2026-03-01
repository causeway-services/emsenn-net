---

skill_spec_version: "1"
id: fetch-rss-feed-skill
name: fetch-rss-feed
summary: Fetch an RSS feed and store raw XML in a target directory.
description: Fetch an RSS feed and store the raw XML in a target directory. Use when collecting feed updates into the inbox.
kind: skill
skill_kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- rss
- syndication
runtime:
  entrypoint: scripts/fetch-rss-feed.py
  language: python
  invocation: cli
inputs:
  - name: url
    type: string
    description: RSS feed URL
    required: true
  - name: output_dir
    type: string
    description: Directory to store feed XML under library/
    required: true
  - name: prefix
    type: string
    description: Optional filename prefix
    required: false
outputs:
  - name: saved_path
    type: path
    description: Path of saved XML file
---

- Run the script: `scripts/fetch-rss-feed.py`
- Provide `--url`, `--output-dir`, and optional `--prefix`.
- Store outputs under `/library/inbox/` for later processing.
