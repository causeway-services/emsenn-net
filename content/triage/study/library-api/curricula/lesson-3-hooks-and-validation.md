---
title: Validation and Follow-up Checks
id: library-api-lesson-hooks
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- api
- programming
dependencies:
- /study/library-api/curricula/lesson-2-crud-and-dry-run.md
- /mathematics/objects/agential-semioverse/tools/validate-frontmatter/SKILL.md
---

# Validation and Follow-up Checks

The engine does not run post-write hooks automatically. Validation is a
separate Skill execution step.

## Validation flow

- Run validation Skills (for example, `validate-frontmatter`) after writes.
- Use the outputs to correct structure or metadata issues.
