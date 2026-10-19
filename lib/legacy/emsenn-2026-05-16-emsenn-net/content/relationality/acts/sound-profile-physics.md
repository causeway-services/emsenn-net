---
title: Sound Profile Physics
act: SoundProfilePhysics
slug: sound-profile-physics
top: PhysicsProfile
bottom: ProfileSemantics
summary: >-
  Witness that profile-level physics judgements are valid in profile semantics
  by composing `PhysicsProfile` with `ProfileSemantics`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Sound Profile Physics

`PhysicsProfile = (FlowObservation FlowProfile)` couples the profile flow with
observations to produce physical judgements.
[ProfileSemantics](profile-semantics.md) interprets those judgements.  Their
composition,
`(PhysicsProfile ProfileSemantics)`, earns
***SoundProfilePhysics***,
recording that profile physics stays inside the profile semantics.