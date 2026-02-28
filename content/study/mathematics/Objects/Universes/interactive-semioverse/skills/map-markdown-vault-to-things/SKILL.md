---

name: map-markdown-vault-to-things
description: Map a markdown vault into thing handles, interaction surfaces, and
  footprints. Use when building an interactive semioverse representation of a vault.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: map-markdown-vault-to-things-skill
tags:
- semiotics
- interactive-semioverse
- markdown
runtime:
  invocation: inference
  tool: llm
dependencies:
- /mathematics/objects/interactive-semioverse/skills/survey-markdown-vault/SKILL.md
- /mathematics/objects/interactive-semioverse/skills/record-markdown-thing-footprint/SKILL.md
---

# Map a Markdown Vault to Things

- Assign stable thing handles to each chosen unit (file, section, or heading).
- Build interaction surfaces for each handle from headings, links, and definitions.
- Generate thing fragments and compute footprints for each handle.
- Store the mapping and footprint summaries in a vault index document.
