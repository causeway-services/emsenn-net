---
title: Completing Trace
act: CompleteTrace
slug: complete-trace
top: StartTrace
bottom: AdvanceTrace
summary: >-
  *Continue Trace* alone does not record the full trace object. Forcing *Start
  Trace* to witness *Advance Trace* binds the initial step with its
  progression, yielding ***Complete Trace*** (`CompleteTrace`).
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Completing Trace

## Interpretation

*Continue Trace* alone does not record the full trace object.  Forcing *Start Trace* to witness *Advance Trace* binds the initial step with its progression, yielding ***Complete Trace*** ([CompleteTrace](complete-trace.md)).

Both components are available; composing them records the entire act of initiating and advancing, so `(StartTrace AdvanceTrace)` earns *Complete Trace*.