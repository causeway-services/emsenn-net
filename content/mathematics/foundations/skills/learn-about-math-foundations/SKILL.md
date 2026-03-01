---

name: learn-about-math-foundations
description: Navigate foundational math curricula and choose the correct topic cluster.
  Use when you need to find the right definitions and entry conditions.
kind: skill
skill-kind: researching
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: learn-about-math-foundations-skill
tags:
- math
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: goal
    type: string
    description: Foundation topic/cluster to target
    required: false
outputs:
  - name: outline
    type: string
    description: Study outline tailored to the goal
---
- Read [/mathematics/structures/foundations/curricula/index.md](/mathematics/structures/foundations/curricula/index.md) to choose a topic cluster.
- Open the chosen cluster's glossary first to learn the terms.
- Work through that cluster's lessons in order.
- For a candidate task, list which structure you intend to use and why it meets the entry conditions.
- If any entry condition fails, stop and note the missing requirement.
