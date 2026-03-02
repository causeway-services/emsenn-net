---

name: write-agda-proof
description: Translate a mathematical statement into Agda and produce a verified proof term. Use when formalizing mathematical claims constructively.
kind: skill
skill-kind: programming
authors:
  - claude-opus-4-6
date-created: 2026-03-01T00:00:00
id: write-agda-proof-skill
tags:
  - proof-assistant
  - agda
  - formal-verification
runtime:
  invocation: inference
  tool: llm
dependencies:
  - /technology/disciplines/computing/software/agda/curricula/index.md
  - /mathematics/disciplines/type-theory/curricula/dependent-types.md
inputs:
  - A mathematical statement in natural language or informal notation
outputs:
  - An Agda module containing the type signature and proof term
---

# Write Agda Proof

- State the proposition as an Agda type signature with explicit parameters.
- Identify which standard library imports are needed (`Relation.Binary`, `Algebra`, etc.).
- Define prerequisite types and structures if not already available in the library.
- Write the proof as a function definition using pattern matching and equational reasoning.
- Use holes (`?`) during development to inspect goal types incrementally.
- Verify the proof type-checks by loading the file (C-c C-l or `agda --check`).
