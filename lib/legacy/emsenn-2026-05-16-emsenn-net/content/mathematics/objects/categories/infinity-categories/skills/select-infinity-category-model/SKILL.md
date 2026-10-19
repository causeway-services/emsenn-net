---

name: select-infinity-category-model
description: Compare common models of infinity categories and pick one for a task.
  Use when you need a concrete representation of higher categories.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: select-infinity-category-model-skill
tags:
- mathematics
- category-theory
- infinity-categories
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: use_case
    type: string
    description: Intended use (homotopy theory, higher algebra, formal reasoning)
    required: false
outputs:
  - name: recommendation
    type: string
    description: Recommended model and rationale
dependencies:
- /mathematics/structures/categories/infinity-categories/curricula/quasi-categories.md
- /mathematics/structures/categories/infinity-categories/terms/index.md
---

# Select an Infinity Category Model

- List the intended use: homotopy theory, higher algebra, or formal reasoning.
- Compare at least two models (quasi-categories, complete Segal spaces, or others).
- Choose a model with tooling or literature support for the intended use case.
- Record the model choice and the reason it fits the task constraints.
