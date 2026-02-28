---

skill_spec_version: "1"
id: ideate-skill
name: ideate
summary: Generate and refine ideas with clear scope and motivation.
description: Generate and refine ideas with clear scope and motivation. Use when you need to propose new work without committing to a plan.
kind: skill
skill_kind: planning
authors:
  - gpt-5.2-codex
date-created: 2025-12-26
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: problem
    type: string
    description: One-sentence problem or gap statement
    required: true
outputs:
  - name: ideas
    type: array
    description: Candidate ideas with summary and motivation
---

- State the problem or gap in one sentence.
- Generate 3–5 candidate ideas that address it.
- For each idea, write a one-line summary and one-line motivation.
- Reject ideas that cannot be expressed in one sentence.
- If an idea survives, write it using `/library/mathematics/objects/agential-semioverse/practice/planning/write-idea/SKILL.md`.
