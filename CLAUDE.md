# CLAUDE.md

Instructions for Claude Code and Claude agents working in this repository.

## Project Overview

This is **emsenn's** research site, built with [Quartz 4](https://quartz.jzhao.xyz/). The
`content/` directory is emsenn's Obsidian vault. The site is published at **emsenn.net**.

emsenn is a Lakota land steward and independent researcher whose work develops
**relationality** — grounded in Lakota epistemologies — as a framework for understanding
life, governance, and history. All agent work should be oriented around supporting that
research.

## Repository Structure

`content/` is the Obsidian vault and primary working area. Its subdirectory structure
evolves over time — use `find content -mindepth 1 -maxdepth 2 -type d` to discover it.
Each directory may have an `index.md` whose `title:` frontmatter field describes its
purpose.

Top-level content directories by purpose:

- `assets/` — images and binary files
- `encyclopedia/` — reference entries (events, people, terms, times)
- `personal/` — emsenn's personal writing
- `private/` — private notes, gitignored, never touch
- `slop/` — AI agent workspace (see below)
- `study/` — research notes organized by discipline
- `triage/` — unprocessed inbox (see below)
- `writing/` — fiction
- `meta/` — Obsidian templates and Copilot prompts, not published
- `tags/` — Quartz tag index pages

Outside `content/`:

- `quartz/` — Quartz framework source, do not modify without explicit instruction
- `quartz.config.ts` / `quartz.layout.ts` — site configuration, leave alone unless asked

## Content That Is Not Published

Quartz is configured to ignore these directories — their content does not appear on the
public site:

- `content/private/` — also gitignored
- `content/meta/`
- `content/slop/`
- `content/triage/`

## The slop/ Directory

`slop/` is the designated workspace for AI agents. You may freely create and edit files
here. Content in `slop/` is not published and not expected to be polished. When you
produce drafts, working notes, or intermediate outputs, put them in `slop/`.

Do not move content out of `slop/` into published directories without explicit instruction.

## The triage/ Directory

`triage/` is an inbox for content that needs to be processed and placed somewhere. Do not
move or delete triage content without explicit instruction. If asked to process triage
content, consult emsenn about destination before acting.

## Frontmatter

Notes use YAML frontmatter. Common fields:

```yaml
title: Note Title
date-created: 2025-01-01T00:00:00
```

New notes need at minimum `title` and `date-created`.

## Style

emsenn has a detailed style guide at `content/slop/emsemioverse-style-guide.md`. Key rules
for agent-generated writing:

- Write respectfully: don't tell the reader how to feel; acknowledge people have qualities
  but are not those qualities
- Use `emsenn` (lowercase, never capitalized)
- Use "use" not "utilize" unless something is being used in an unusual way
- Avoid vague adverbs: very, quite, clearly, completely, significantly, etc.
- Don't mix contractions with their spelled-out equivalents in the same piece
- Never form contractions from a noun and a verb (e.g., "emsenn's developing" is wrong)
- Prefer active voice and direct phrasing

When writing or editing content intended for publication, read the full style guide first.

## Git Conventions

- Binary files (images, PDFs, STLs, etc.) are tracked with Git LFS — handled automatically
- `content/private/` is gitignored — never stage files from there
- `.claude/worktrees/` and `.claude/projects/` are gitignored; `.claude/skills/` is tracked

## What Not to Touch

- `content/private/` — private notes, not in git
- `quartz/` — framework code, leave alone unless specifically asked
- `quartz.config.ts` / `quartz.layout.ts` — site configuration, leave alone unless asked
- Obsidian metadata in `content/.obsidian/` — leave alone
