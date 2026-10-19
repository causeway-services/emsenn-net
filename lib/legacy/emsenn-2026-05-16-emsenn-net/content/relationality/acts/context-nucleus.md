---
title: Collapsing Context
act: ContextNucleus
slug: context-nucleus
top: NucleateProfile
bottom: RecognizeContext
summary: >-
  Collapse contexts under the profile nucleus by composing `NucleateProfile`
  with `RecognizeContext`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Collapsing Context

Contexts collapse under the nucleus.  We restrict the profile nucleus to
contexts by letting it witness [RecognizeContext](recognize-context.md):
`(NucleateProfile RecognizeContext)` earns
***ContextNucleus***.

[NucleateProfile](nucleate-profile.md) closes recognitions under the nucleus,
and `RecognizeContext` packages context recognitions, so their composition
collapses contexts according to the profile closure.