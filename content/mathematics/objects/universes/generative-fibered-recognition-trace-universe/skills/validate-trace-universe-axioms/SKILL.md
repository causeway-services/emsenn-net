---

name: validate-trace-universe-axioms
description: Validate the toy GFRTU against its axioms and fixed fibers. Use when
  checking consistency of a trace universe model.
kind: skill
skill-kind: researching
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: validate-trace-universe-axioms-skill
tags:
- math
runtime:
  invocation: inference
  tool: llm
---
- Confirm the trace category is small and finite.
- Confirm each fiber is a Heyting algebra.
- Confirm stabilizer and drift are monotone and commute.
- Confirm fixed fibers match the toy model.
- Confirm the closure sequence matches the golden output.
