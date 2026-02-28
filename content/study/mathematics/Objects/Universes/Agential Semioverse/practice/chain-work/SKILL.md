---

skill_spec_version: "1"
id: chain-work-skill
name: chain-work
summary: Plan a chain of skill invocations by wiring outputs to inputs explicitly.
description: >
  Given a target closure and a set of skills, produce an ordered chain
  where each work unit has its inputs satisfied by previous outputs or
  initial context. Use to reduce ambiguity and enable validation before execution.
kind: skill
skill_kind: programming
authors:
  - gpt-5.2-codex
date-created: 2026-01-08
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: closure
    type: string
    description: Desired end state or artifact
    required: true
  - name: available_skills
    type: array
    description: Skill ids and brief capabilities to consider
    required: true
  - name: initial_context
    type: string
    description: Inputs/artifacts already available
    required: false
outputs:
  - name: chain
    type: array
    description: Ordered steps with skill id, inputs, outputs to produce
---

- Identify the minimal skills needed to reach the stated closure.
- For each step, write: `{skill_id, inputs (with source), outputs (tokens/URIs)}`.
- Ensure every input is satisfied by an earlier output or initial_context; if not, insert a work unit to produce it.
- Note shared resources or permissions that could contend; consider splitting parallelizable steps.
