---

name: write-lean-proof
description: Translate a mathematical statement into a Lean 4 theorem declaration and produce a verified proof. Use when formalizing mathematical claims from the vault.
kind: skill
skill-kind: programming
authors:
  - claude-opus-4-6
date-created: 2026-03-01T00:00:00
id: write-lean-proof-skill
tags:
  - proof-assistant
  - lean
  - formal-verification
runtime:
  invocation: inference
  tool: llm
dependencies:
  - /technology/disciplines/computing/software/lean/curricula/index.md
  - /mathematics/disciplines/type-theory/curricula/dependent-types.md
inputs:
  - A mathematical statement in natural language or informal notation
outputs:
  - A Lean 4 file containing the theorem declaration and proof
---

# Write Lean Proof

- State the proposition as a Lean `theorem` with an explicit type signature.
- Identify which Mathlib imports are needed (`import Mathlib.Order.Heyting.Basic`, etc.).
- Choose proof strategy: term-mode for short proofs, tactic-mode for multi-step proofs.
- Write the proof incrementally, checking each tactic step against the expected goal state.
- Use `exact?` or `apply?` to search for relevant library lemmas when unsure.
- Verify the proof compiles by running `lake build` or checking in the editor.
