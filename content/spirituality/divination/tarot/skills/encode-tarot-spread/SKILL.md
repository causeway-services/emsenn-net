---

name: encode-tarot-spread
description: Encode a tarot spread draw using the YAML specification. Use when recording
  a reading for later interpretation.
kind: skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: encode-tarot-spread-skill
tags:
- tarot
runtime:
  invocation: inference
  tool: human
dependencies:
- /study/tarot/SPECIFICATIONS.md
- /study/tarot/spreads/three-card.md
- /study/tarot/spreads/celtic-cross.md
---

# Encode Tarot Spread

- Choose the spread and list its positions.
- Record each drawn card with its position and orientation.
- Save the YAML file under `/study/tarot/examples/` or a session folder.
