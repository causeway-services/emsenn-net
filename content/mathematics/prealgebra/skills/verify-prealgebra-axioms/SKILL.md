---

name: verify-prealgebra-axioms
description: Check whether a set and operation satisfy magma, semigroup, or monoid
  axioms. Use when you need to validate a proposed prealgebraic structure.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: verify-prealgebra-axioms-skill
tags:
- mathematics
- prealgebra
runtime:
  invocation: inference
  tool: llm
inputs:
  - name: elements
    type: array
    description: Elements of the set
    required: false
  - name: operation
    type: object
    description: Operation rule/table ((a,b)->c) or description
    required: false
outputs:
  - name: axioms_satisfied
    type: array
    description: Axioms that hold (closure, associativity, identity)
dependencies:
- /study/math/structures/prealgebra/curricula/lesson-1-magmas-semigroups.md
- /study/math/structures/prealgebra/curricula/lesson-2-monoids-homomorphisms.md
- /study/math/structures/prealgebra/terms/index.md
---

# Verify Prealgebra Axioms

- Specify the set `S` and operation `* : S x S -> S`.
- Check closure by verifying the result stays in `S` for representative inputs.
- Test associativity with a symbolic check or explicit counterexample search.
- If claiming a monoid, identify the candidate identity element and verify both sides.
- Record which axioms hold and name the strongest structure justified by them.
