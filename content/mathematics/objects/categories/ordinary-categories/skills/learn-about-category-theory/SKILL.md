---

name: learn-about-category-theory
description: Learn the meaning of categories, functors, and natural transformations
  from first principles. Use when you need to interpret or define categorical structures.
kind: skill
skill-kind: researching
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: learn-about-category-theory-skill
tags:
- math
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: goal
    type: string
    description: What categorical concept or task to target
    required: false
  - name: level
    type: string
    description: Background level (beginner, intermediate, advanced)
    required: false
outputs:
  - name: outline
    type: string
    description: Study outline or explanation tailored to the goal
---
- Read [/mathematics/structures/categories/ordinary-categories/curricula/index.md](/mathematics/structures/categories/ordinary-categories/curricula/index.md).
- Read [/mathematics/structures/categories/ordinary-categories/terms/index.md](/mathematics/structures/categories/ordinary-categories/terms/index.md) first if any term is unfamiliar.
- Work through the lessons in order.
- For a task, state objects, morphisms, and composition explicitly before introducing functors.
