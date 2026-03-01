---
title: "Markdown Vaults"
aliases:
  - "Markdown Vaults"
id: markdown-lesson-vaults
kind: lesson
authors:
- gpt-5.2-codex
date-created: 2025-12-31
tags:
- markdown
- documentation
dependencies:
- /technology/computing/specifications/markdown/curricula/frontmatter-metadata.md
- /technology/computing/specifications/markdown/terms/index.md
---


A vault is a collection of markdown files treated as a linked knowledge base.

## Vault properties

- Files are nodes; links are edges.
- Frontmatter supplies stable identifiers and metadata.
- Index files summarize the vault and provide entry points.

## Vault hygiene

- Keep `id` values unique and stable.
- Normalize tags and dependencies.
- Track missing or broken links for repair.
