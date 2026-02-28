---

name: map-semiotic-interaction
description: Map a task to Things, interactions, fragments, and closure. Use when
  acting as Emsemiote or when clarifying the semiotic shape of work.
kind: skill
skill_kind: assisting
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: map-semiotic-interaction-skill
summary: Map a task to Things, interactions, fragments, and closure before acting.
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: task
    type: string
    description: Description of the work to be mapped
    required: true
outputs:
  - name: map
    type: string
    description: Bullet summary of Things, interaction, context, and closure
---

- Name the Thing(s) involved (the primary file or directory being changed).
- Name the interaction being performed.
- List the fragment context:
  - the Thing itself
  - nearest spec or contract
  - governing skill (if any)
  - directly referenced files
- State the closure condition.
- Use that mapping to guide the smallest effective change.
