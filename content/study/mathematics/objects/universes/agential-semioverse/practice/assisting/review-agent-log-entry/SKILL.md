---

name: review-agent-log-entry
description: Review an agent log entry for clarity, completeness, and traceability.
  Use when checking logs before sharing with other agents.
kind: agent-skill
skill-kind: assisting
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: review-agent-log-entry-skill
tags:
- agent-log
dependencies:
- /skills/assisting/agent-log-guidance/README.md
---

- Ensure all required sections are present and non-empty.
- Verify that key files or directories are referenced.
- Check that decisions and open questions are explicit.
- Note any missing context needed for another agent to continue.
