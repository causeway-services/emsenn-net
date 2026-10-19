---

name: estimate-conditional-probability
description: Estimate conditional probability from counted outcomes. Use when
  updating a probability based on evidence.
kind: skill
skill-kind: analysis
authors:
- gpt-5.2-codex
date-created: 2026-01-01
id: estimate-conditional-probability-skill
tags:
- probability
- mathematics
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: event_a
    type: string
    description: Event A or count of A occurrences
    required: false
  - name: event_b
    type: string
    description: Event B (evidence) or count of B occurrences
    required: false
  - name: counts
    type: object
    description: Optional counts (total, a, b, a_and_b)
    required: false
outputs:
  - name: estimate
    type: string
    description: Estimated P(A|B) or guidance to compute it
dependencies:
- /mathematics/probability/curricula/conditional-and-independence.md
- /mathematics/probability/terms/index.md
---

# Estimate Conditional Probability

- Define the sample space and the evidence event.
- Count outcomes where both the event and evidence occur.
- Divide by the count of outcomes where the evidence occurs.
- Note any assumptions about equally likely outcomes.
