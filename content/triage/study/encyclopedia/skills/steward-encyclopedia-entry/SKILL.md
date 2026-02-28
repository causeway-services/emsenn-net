---

name: steward-encyclopedia-entry
description: Steward an encyclopedia entry by enforcing structure, sources, and metadata.
  Use when adding or updating encyclopedia content.
kind: skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: steward-encyclopedia-entry-skill
tags:
- encyclopedia
runtime:
  invocation: inference
  tool: llm
dependencies:
- /study/encyclopedia/curricula/index.md
- /skills/assisting/enrich-content/SKILL.md
---

# Steward Encyclopedia Entry

- Ensure the entry defines the topic and scope clearly.
- Add or update sources, references, and context.
- Apply the enrich-content skill to keep metadata current.
