---

name: build-markdown-vault-index
description: Scan a markdown vault and emit a vault index document. Use when producing
  an interactive semioverse mapping overview for a vault.
kind: skill
skill-kind: programming
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: build-markdown-vault-index-skill
tags:
- semiotics
- interactive-semioverse
- markdown
runtime:
  invocation: inference
  tool: llm
dependencies:
- /mathematics/objects/interactive-semioverse/skills/map-markdown-vault-to-things/SKILL.md
- /mathematics/objects/interactive-semioverse/templates/markdown-vault-index.md.j2
---

# Build Markdown Vault Index

- Run `scripts/build-markdown-vault-index.py`.
- Provide `--vault-root` (directory to scan) and `--output` (index markdown file).
- Optionally set `--template` to a different `.md.j2` template.
- Commit or store the generated index near the vault root.
