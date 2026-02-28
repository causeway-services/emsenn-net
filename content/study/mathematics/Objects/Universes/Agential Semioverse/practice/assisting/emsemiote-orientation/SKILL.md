---

name: emsemiote-orientation
description: Orient work as the Emsemiote by mapping tasks to semiotic interactions
  and closure. Use when operating as a semiotic agent in this repository.
kind: skill
skill_kind: assisting
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: emsemiote-orientation-skill
summary: Frame the current task as an Emsemiote by mapping Things, interactions, and closure.
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: task
    type: string
    description: Task description to orient within the Emsemioverse
    required: true
outputs:
  - name: orientation
    type: string
    description: Brief mapping of Things, interactions, and closure
---

- Read the abstracts of the Semiotic Universe and Interactive Semioverse documents.
- Identify the Things involved (documents, skills, agents, plans, specifications).
- Identify the interaction being performed (edit, collect, publish, interpret).
- Identify the intended closure (what output validates completion).
- Choose the minimal change that preserves semantics.
- Report which processes were used in the response.
