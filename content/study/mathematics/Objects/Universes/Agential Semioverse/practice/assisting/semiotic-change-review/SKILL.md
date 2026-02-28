---

name: semiotic-change-review
description: Review a proposed change for fragment scope and closure alignment. Use
  before editing core specs, agent contracts, or foundational docs.
kind: skill
skill_kind: assisting
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: semiotic-change-review-skill
summary: Check a proposed change for scope, governing specs, and closure alignment.
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: change_summary
    type: string
    description: Short description of the proposed change
    required: true
  - name: artifacts
    type: array
    description: Related files or specs being changed
    required: false
outputs:
  - name: review
    type: string
    description: Structured notes on Things, context, and closure risks
---

- Identify the Thing(s) being changed.
- List the fragment context:
  - the Thing itself
  - nearest spec or contract
  - governing skill (if any)
  - directly referenced files
- Confirm the change is minimal for the stated closure.
- If the closure is unclear, stop and ask for it.
