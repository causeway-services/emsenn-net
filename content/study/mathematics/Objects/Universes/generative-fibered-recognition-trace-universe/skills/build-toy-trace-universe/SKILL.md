---

name: build-toy-trace-universe
description: Construct a trace site and recognition fibers for a target domain. Use
  when you need to formalize locality and recognition structure.
kind: skill
skill-kind: researching
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: build-toy-trace-universe-skill
tags:
- math
runtime:
  invocation: inference
  tool: llm
---
- Define the trace site $T$: objects as traces, morphisms as refinements.
- Choose a Grothendieck topology that marks which refinements cover each trace.
- For each trace, define a finite Heyting algebra $H_t$.
- Define stabilizer $\sigma_t$ and drift $\Delta_t$ for each fiber.
- Define reindexing maps along trace morphisms.
- Record the constructed data in an example file or working notes.
