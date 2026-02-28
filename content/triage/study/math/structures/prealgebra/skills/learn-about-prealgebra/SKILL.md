---

name: learn-about-prealgebra
description: Learn the basic prealgebraic structures and the axioms they satisfy.
  Use when you need to interpret or define magmas, semigroups, and monoids.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: learn-about-prealgebra-skill
tags:
- mathematics
- prealgebra
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: goal
    type: string
    description: Target topic (e.g., magmas, semigroups, monoids)
    required: false
outputs:
  - name: outline
    type: string
    description: Study outline tailored to the goal
dependencies:
- /study/math/structures/prealgebra/curricula/index.md
- /study/math/structures/prealgebra/GLOSSARY.md
---

# Learn About Prealgebra

- Read [Prealgebra curriculum](/study/math/structures/prealgebra/curricula/index.md).
- Use the [Prealgebra glossary](/study/math/structures/prealgebra/GLOSSARY.md) for term definitions.
- Restate each structure as a set and operation, then list its axioms in your own words.
