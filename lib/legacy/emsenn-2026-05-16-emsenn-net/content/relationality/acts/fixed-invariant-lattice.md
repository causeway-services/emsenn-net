---
title: Structuring Fixed Invariant Lattice
act: FixedInvariantLattice
slug: fixed-invariant-lattice
top: ProfileInvariantLattice
bottom: FixedInvariantOrder
summary: >-
  Restrict the profile invariant lattice to the fixed order by composing
  `ProfileInvariantLattice` with `FixedInvariantOrder`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Structuring Fixed Invariant Lattice

`ProfileInvariantLattice = (StructureSemantics ProfileInvariantOrder)` packages
the lattice structure on profile invariants.  Restricting it along
[FixedInvariantOrder](fixed-invariant-order.md) yields the lattice structure
on fixed invariants:
`(ProfileInvariantLattice FixedInvariantOrder)` earns
***FixedInvariantLattice***.

`ProfileInvariantLattice` encapsulates the algebraic laws of meets, joins, and
implication on the restricted order, and `FixedInvariantOrder` narrows that
order to the fixed invariants.  Their composition records that the fixed
invariant states inherit the same lattice structure.