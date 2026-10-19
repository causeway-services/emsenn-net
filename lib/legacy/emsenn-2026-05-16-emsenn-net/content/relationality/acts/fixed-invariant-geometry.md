---
title: Geometry of Fixed Invariant States
act: FixedInvariantGeometry
slug: fixed-invariant-geometry
top: ProfileInvariantGeometry
bottom: FixedInvariantLattice
summary: >-
  Restrict the profile invariant geometry to the fixed lattice by composing
  `ProfileInvariantGeometry` with `FixedInvariantLattice`.
  - free
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Geometry of Fixed Invariant States

`ProfileInvariantGeometry = (GeometryProfile ProfileInvariantLattice)` packages
the geometry of profile-invariant states.
[FixedInvariantLattice](fixed-invariant-lattice.md) exhibits the order
structure of fixed invariant states.  Restricting the profile geometry to this
lattice,
`(ProfileInvariantGeometry FixedInvariantLattice)` earns
***FixedInvariantGeometry***.

`ProfileInvariantGeometry` provides flow and nucleus for the profile invariants,
and `FixedInvariantLattice` describes the meet–join order on states fixed by
the flow and compatible with `FixedShape`.  Their composition packages
the order, closure, and dynamics of fixed invariant states as a geometric
structure in its own right.