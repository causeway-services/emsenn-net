---

name: formalize-structure-minimally
description: Specify the minimal data required to define a foundational structure
  once entry conditions are satisfied. Use when you need a precise, minimal formalization.
kind: skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: formalize-structure-minimally-skill
tags:
- math
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: structure
    type: string
    description: Structure to formalize
    required: false
outputs:
  - name: formalization
    type: string
    description: Minimal data/axioms captured
---
- Confirm entry conditions using `verify-structure-entry-conditions`. If any fail, stop.
- Write down the minimal data for the structure, using the relevant cluster lessons:
  - set: elements and membership rule
  - relation: ordered pairs
  - function: total mapping
  - order: relation with axioms
  - lattice: meet/join rules
  - category: objects, morphisms, identities, composition
  - functor: object/morphism map, preservation proofs
  - site: category plus Grothendieck topology
  - sheaf: assignment plus gluing condition
- State any axioms that must still be checked.
