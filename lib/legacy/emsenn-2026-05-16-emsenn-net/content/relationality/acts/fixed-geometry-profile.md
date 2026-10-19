---
title: Fixed Geometry Profile
act: FixedGeometryProfile
slug: fixed-geometry-profile
top: FixedFlowProfile
bottom: FixedNucleateProfile
summary: >-
  Combine the restricted flow and nucleus of the fixed profile to form its
  geometry.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Geometry Profile

A geometry on a profile combines its restricted flow and restricted nucleus.
For the fixed profile we pair
[FixedFlowProfile](fixed-flow-profile.md) with
[FixedNucleateProfile](fixed-nucleate-profile.md):
`(FixedFlowProfile FixedNucleateProfile)` earns
***FixedGeometryProfile***.

`FixedFlowProfile` provides the shuffle-derived dynamics on the fixed
recognitions, and `FixedNucleateProfile` supplies the corresponding closure.
Their composition packages the compatible pair as the geometry of the fixed
profile.