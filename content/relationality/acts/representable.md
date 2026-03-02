---
title: Representable Functor
act: RepresentableFunctor
slug: representable
top: FixedFunctor
bottom: FixedIdentity
summary: >-
  Encode representability by letting the fixed functor witness the fixed
  identity.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Representable Functor

A representable functor is naturally isomorphic to “morphisms out of an object.”
In the fixed profile the representative object is the identity, so we let the
functor witness it:
`(FixedFunctor FixedIdentity)` earns ***RepresentableFunctor***.

[FixedFunctor](fixed-functor.md) maps objects and morphisms, and
[FixedIdentity](fixed-identity.md) is the terminal identity on each fixed
object.  Their composition asserts that the functor’s action is determined by
its values on identities, matching representability.