---
title: Presenting Variable Term
act: PresentVariableTerm
slug: present-variable-term
top: BindTerm
bottom: HeadTrace
summary: >-
  A bound name should expose the corresponding head, so the act *Bind Term*
  must witness the act *Head Trace*.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Presenting Variable Term

## Interpretation

A bound name should expose the corresponding head, so the act *Bind Term* must witness the act *Head Trace*.

In `(BindTerm HeadTrace)` the binding observes the trace head, presenting that head as a variable; this composition is therefore *Present Variable Term*.