---
title: Fixed Functor
act: FixedFunctor
slug: fixed-functor
top: Spectrum
bottom: FixedMorphism
summary: >-
  Map fixed recognitions via spectral decomposition while preserving morphisms
  by composing `Spectrum` with `FixedMorphism`.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Functor

A fixed functor maps each fixed recognition to another fixed recognition in a
way compatible with the fixed morphisms, identity, and composition.  We encode
this by letting the spectral action witness the morphism structure:
`(Spectrum FixedMorphism)` earns ***FixedFunctor***.

[Spectrum](spectrum.md) decomposes each recognition into harmonic components,
and `FixedMorphism` records the allowed structure-preserving maps between fixed
recognitions.  Their composition ensures that objects are mapped via spectral
decomposition while morphisms are transported compatibly, automatically
preserving identities and composition.