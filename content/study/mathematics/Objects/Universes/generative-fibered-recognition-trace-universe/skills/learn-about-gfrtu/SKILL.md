---

name: learn-about-gfrtu
description: Learn the GFRTU object through its short explainers and identify which
  processes apply to a task. Use when you need to apply GFRTU concepts without reading
  the full paper.
kind: skill
skill-kind: researching
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: learn-about-gfrtu-skill
tags:
- math
runtime:
  invocation: inference
  tool: llm
---
- Read `curricula/overview.md` to identify GFRTU entry conditions and misuse warnings.
- Read `curricula/lesson-1-trace-site.md` and `curricula/lesson-2-stabilization-drift.md` to understand the required primitives.
- Read `curricula/lesson-3-closure-ug.md` for the minimality requirement.
- Read `curricula/processes.md` for the whole-object workflow.
- State whether the task satisfies the entry conditions. If not, stop and recommend a different object.
- If it does, state the required primitives, the closure operator, and the expected fixed point you will use.
