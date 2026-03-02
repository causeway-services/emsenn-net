---
title: Sound Profile Geometry
act: SoundProfileGeometry
slug: sound-profile-geometry
top: PhysicsProfile
bottom: GeometryProfile
summary: >-
  Show that profile physics respects the profile geometry by composing
  `PhysicsProfile` with `GeometryProfile`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Sound Profile Geometry

`GeometryProfile = (FlowProfile NucleateProfile)` packages the compatible
flow–nucleus pair on the active profile.  `PhysicsProfile = (FlowObservation
FlowProfile)` couples the same flow with observations.  To record that the
physical dynamics respect the geometric invariants, we compose them:
`(PhysicsProfile GeometryProfile)` earns
***SoundProfileGeometry***.