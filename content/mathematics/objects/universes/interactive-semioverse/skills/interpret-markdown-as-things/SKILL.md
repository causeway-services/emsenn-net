---

name: interpret-markdown-as-things
description: Map a markdown document into thing handles and semantic seeds. Use
  when treating a markdown file as a source of interactive semioverse data.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: interpret-markdown-as-things-skill
tags:
- semiotics
- interactive-semioverse
- markdown
runtime:
  invocation: inference
  tool: llm
dependencies:
- /mathematics/objects/interactive-semioverse/curricula/things-interactions.md
- /mathematics/objects/interactive-semioverse/terms/index.md
- /media/writing/tools/write-markdown/SKILL.md
---

# Interpret Markdown as Things

- Choose the markdown unit to treat as a thing handle (document, section, or heading).
- Assign each handle a stable identifier and a seed element in the semantic domain.
- Record how frontmatter fields map into semantic seeds (title, tags, dependencies).
- Note which fields are treated as interaction surfaces versus static metadata.
