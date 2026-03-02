---
title: Preserving Typing
act: PreserveTyping
slug: preserve-typing
top: JudgeTyping
bottom: StepTrace
summary: >-
  Reductions recorded in *Step Trace* must preserve typing judgements. *Judge
  Typing* witnessing *Step Trace* yields ***Preserve Typing***
  (`PreserveTyping`).
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Preserving Typing

## Interpretation

Reductions recorded in *Step Trace* must preserve typing judgements.  *Judge Typing* witnessing *Step Trace* yields ***Preserve Typing*** ([PreserveTyping](preserve-typing.md)).

Composing these recognitions records the assertion “if a context recognises term t at type A and t reduces to t′ then the context recognises t′ at type A,” so *Preserve Typing* follows.