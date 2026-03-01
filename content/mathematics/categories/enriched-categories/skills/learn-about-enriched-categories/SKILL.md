---

name: learn-about-enriched-categories
description: Learn how enriched categories generalize ordinary categories using
  monoidal bases. Use when you need to interpret hom-objects and enriched composition.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: learn-about-enriched-categories-skill
tags:
- mathematics
- category-theory
- enriched-categories
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: base_monoidal_category
    type: string
    description: Base of enrichment (e.g., V)
    required: false
  - name: goal
    type: string
    description: Topic to cover (data, examples, coherence)
    required: false
outputs:
  - name: outline
    type: string
    description: Study outline tailored to the goal
dependencies:
- /mathematics/structures/categories/enriched-categories/curricula/index.md
- /mathematics/structures/categories/enriched-categories/terms/index.md
---

# Learn About Enriched Categories

- Read the [Enriched categories curriculum](/mathematics/structures/categories/enriched-categories/curricula/index.md).
- Use the [Enriched categories glossary](/mathematics/structures/categories/enriched-categories/terms/index.md) for term definitions.
- Write the data of an enriched category in the form of hom-objects, composition, and units.
