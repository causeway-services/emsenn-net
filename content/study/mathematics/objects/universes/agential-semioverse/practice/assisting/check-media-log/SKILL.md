---

name: check-media-log
description: Check the media log for stale entries and prompt for updates if needed.
  Use when monitoring media consumption logs.
kind: agent-skill
skill-kind: assisting
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: check-media-log-skill
tags:
- media-log
dependencies:
- /agents/emsenn/content/media-log/media-log.md
- /skills/assisting/agent-log-guidance/README.md
---

- Run `scripts/check-media-log.py` with `--path` to the media log.
- If more than one day has passed since the last entry, ask the operator (if emsenn) for updates.
