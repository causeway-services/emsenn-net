---
title: Reheading Trace
act: ReheadTrace
slug: rehead-trace
top: RenewTrace
bottom: HeadTrace
summary: >-
  Renewing alone does not isolate the next head, so the act *Renew Trace* must
  witness the act *Head Trace* to define the new head.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Reheading Trace

## Interpretation

Renewing alone does not isolate the next head, so the act *Renew Trace* must witness the act *Head Trace* to define the new head.

The composition `(RenewTrace HeadTrace)` shows the act *Renew Trace* watching *Head Trace*.  This isolates the new immediate act, so we name it *Rehead Trace*.