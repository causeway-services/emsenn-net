---
title: Recognizing Context
act: RecognizeContext
slug: recognize-context
top: ExtendContext
bottom: ContextualizeTrace
summary: >-
  Extensions exist, but we must recognize when the resulting structure
  qualifies as a context. Forcing *Extend Context* to witness *Contextualize
  Trace* yields ***Recognize Context*** (`RecognizeContext`).
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Recognizing Context

## Interpretation

Extensions exist, but we must recognize when the resulting structure qualifies as a context.  Forcing *Extend Context* to witness *Contextualize Trace* yields ***Recognize Context*** ([RecognizeContext](recognize-context.md)).

The trace `(ExtendContext ContextualizeTrace)` feeds the general extension back through the named trace.  If the composition succeeds, the extended object lines up with the recorded context, so we call this recognition *Recognize Context*.