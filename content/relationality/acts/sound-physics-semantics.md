---
title: Sound Physics Semantics
act: SoundFixedPhysicsSemantics
slug: sound-fixed-physics-semantics
top: SoundProfilePhysics
bottom: FixedProfileSemantics
summary: >-
  Record that fixed physics judgements remain valid in the fixed semantics by
  composing `SoundProfilePhysics` with `FixedProfileSemantics`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Sound Physics Semantics

Profile physics is already sound in profile semantics via
[SoundProfilePhysics](sound-profile-physics.md).
[FixedProfileSemantics](fixed-profile-semantics.md) restricts those semantics
to the fixed recognitions.  Composing them,
`(SoundProfilePhysics FixedProfileSemantics)`, earns
***SoundFixedPhysicsSemantics***,
ensuring physical judgements remain valid inside the fixed semantics.