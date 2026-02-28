---
title: Skill Execution Flow
id: library-api-lesson-crud
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- api
- programming
dependencies:
- /study/library-api/curricula/lesson-1-library-api-overview.md
- /mathematics/objects/agential-semioverse/tools/read-file/SKILL.md
- /mathematics/objects/agential-semioverse/tools/write-file/SKILL.md
- /mathematics/objects/agential-semioverse/tools/list-directory/SKILL.md
---

# Skill Execution Flow

The engine executes Skills directly. There is no server-side dry-run toggle; use
separate Skills to inspect and validate before and after writes.

## Read

- Use `read-file-skill` with `{ "path": "..." }`.
- Use `list-directory-skill` to discover paths.

## Write

- Use `write-file-skill` with `{ "path": "...", "content": "..." }`.
- Re-run `read-file-skill` to verify the result.

## Move

- Use `move-path-skill` for renames or relocations.
