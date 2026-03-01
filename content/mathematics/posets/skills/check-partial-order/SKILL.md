---

name: check-partial-order
description: Verify that a relation is a partial order by checking reflexivity,
  antisymmetry, and transitivity. Use when validating poset definitions.
kind: skill
skill-kind: learning
authors:
- gpt-5.2-codex
date-created: 2025-12-31
id: check-partial-order-skill
tags:
- math
runtime:
  invocation: inference
  tool: llm
dependencies:
- /study/math/structures/posets/curricula/lesson-1-orders.md
---

# Check Partial Order

- State the set and the relation `<=`.
- Check reflexivity: `a <= a` for all `a`.
- Check antisymmetry: if `a <= b` and `b <= a`, then `a = b`.
- Check transitivity: if `a <= b` and `b <= c`, then `a <= c`.
- If any axiom fails, record the counterexample.
