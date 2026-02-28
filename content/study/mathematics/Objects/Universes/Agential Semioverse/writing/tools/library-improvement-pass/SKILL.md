---

name: library-improvement-pass
description: Run a structured pass to improve library content and metadata. Use when
  performing broad cleanup or quality improvement work.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: library-improvement-pass-skill
---

- Run [validate-frontmatter](/mathematics/objects/agential-semioverse/tools/validate-frontmatter/SKILL.md) and [check-markdown-well-formed](/media/writing/tools/check-markdown-well-formed/SKILL.md).
- Normalize frontmatter with [normalize-frontmatter](/mathematics/objects/agential-semioverse/tools/normalize-frontmatter/SKILL.md).
- Fix missing IDs and H1 mismatches in the highest-value directories first.
- Re-run the validators and record remaining errors.
- Write an agent log entry summarizing decisions and remaining gaps.
