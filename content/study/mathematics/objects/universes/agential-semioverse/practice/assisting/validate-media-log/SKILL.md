---

name: validate-media-log
description: Validate media log formatting and date headings. Use when checking that
  media logs follow the specification.
kind: agent-skill
skill-kind: assisting
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: validate-media-log-skill
tags:
- media-log
dependencies:
- /agents/emsenn/content/media-log/SPECIFICATIONS.md
---

- Run `scripts/validate-media-log.py` with `--path` to the media log.
- Fix invalid date headings or empty sections.
