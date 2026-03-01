---

name: survey-markdown-vault
description: Survey a markdown vault to identify thing handles, interaction surfaces,
  and link structure. Use when preparing a vault for interactive semioverse modeling.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: survey-markdown-vault-skill
tags:
- semiotics
- interactive-semioverse
- markdown
runtime:
  invocation: inference
  tool: llm
dependencies:
- /mathematics/objects/interactive-semioverse/skills/interpret-markdown-as-things/SKILL.md
- /mathematics/objects/interactive-semioverse/skills/derive-interaction-terms-from-markdown/SKILL.md
---

# Survey a Markdown Vault

- List all markdown files and decide the granularity of thing handles.
- Record the frontmatter fields that will seed thing handles.
- Identify link density and repeated terms for candidate interaction surfaces.
- Note any missing frontmatter or inconsistent ids for follow-up.
