---

name: verify-structure-entry-conditions
description: Verify that a concrete situation meets the axioms required to use a specific
  foundational structure. Use when you must justify the validity of applying a structure.
kind: skill
skill-kind: researching
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: verify-structure-entry-conditions-skill
tags:
- math
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: structure
    type: string
    description: Structure to apply
    required: false
  - name: assumptions
    type: string
    description: Assumptions/data of the situation
    required: false
outputs:
  - name: validation
    type: string
    description: Which entry conditions are satisfied or missing
---
- Identify the target structure and its topic cluster (sets/relations, order theory, category theory, sheaf theory).
- List the exact entry conditions from the corresponding curriculum lesson in that cluster.
- Check each condition explicitly against the situation.
- Record a pass/fail result for each condition and note any missing data.
- If any condition fails, stop and recommend not using the structure.
