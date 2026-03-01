---

name: interpret-tarot-spread
description: Interpret a tarot spread using card meanings and position roles. Use when
  turning a spread draw into a narrative reading.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: interpret-tarot-spread-skill
tags:
- tarot
runtime:
  invocation: inference
  tool: human
dependencies:
- /spirituality/divination/tarot/SPECIFICATIONS.md
- /spirituality/divination/tarot/cards/major-arcana.md
- /spirituality/divination/tarot/cards/minor-arcana.md
---

# Interpret Tarot Spread

- Run `scripts/interpret-tarot-spread.py` on a YAML spread draw.
- Review the position roles and card themes in context.
- Write a short narrative linking position, orientation, and card meaning.
