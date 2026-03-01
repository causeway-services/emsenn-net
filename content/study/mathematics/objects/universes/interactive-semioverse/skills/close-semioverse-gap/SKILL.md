---

name: close-semioverse-gap
description: Identify a documentation or skill gap using interactive semioverse concepts
  and close it with targeted artifacts. Use when bridging missing links in the library.
kind: skill
skill-kind: assisting
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: close-semioverse-gap-skill
tags:
- semiotics
- interactive-semioverse
runtime:
  invocation: inference
  tool: llm
dependencies:
- /mathematics/objects/interactive-semioverse/skills/survey-markdown-vault/SKILL.md
- /skills/assisting/identify-content-gap/SKILL.md
- /skills/assisting/identify-skill-gap/SKILL.md
---

# Close Semioverse Gap

- Define the target area as a set of things (documents, modules, or skills).
- Treat missing links, missing metadata, and missing artifacts as gaps in the interaction surface.
- Use `identify-content-gap` or `identify-skill-gap` to formalize the missing artifacts.
- Close the gap by creating the smallest required document, curriculum, or skill.
- Record the closure by updating indexes or READMEs that surface the new artifact.
