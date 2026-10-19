---
title: Fixed Identity
act: FixedIdentity
slug: fixed-identity
top: IdentifyMorph
bottom: FixedProfileRecognitions
summary: >-
  Restrict identity morphisms to fixed recognitions by composing
  `IdentifyMorph` with `FixedProfileRecognitions`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Identity

A category needs identity morphisms.  `IdentifyMorph = (Morph Reflex)` provides
identities in the full profile.  We restrict it to the fixed-recognition objects by
composing with [FixedProfileRecognitions](fixed-profile-recognitions.md):
`(IdentifyMorph FixedProfileRecognitions)` earns ***FixedIdentity***.

`IdentifyMorph` identifies the identity on any recognition, and restricting its
domain to the fixed ones gives identity morphisms for the fixed category.