---
title: Fixed Monad Multiplication
act: FixedMonadMultiply
slug: fixed-monad-multiply
top: FixedNucleateProfile
bottom: FixedNucleateProfile
summary: >-
  Record the monad multiplication by composing the fixed nucleus with itself,
  yielding the idempotent collapse of double closure.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Monad Multiplication

Applying the nucleus twice should collapse as a single closure.  The monad
multiplication identifies `N(N(X))` with `N(X)`, so we let the nucleus observe
its own action:
`(FixedNucleateProfile FixedNucleateProfile)` earns
***FixedMonadMultiply***.

`FixedNucleateProfile` already idempotently closes recognitions, and the
composition records the multiplication `μ_X : N(N(X)) → N(X)` implementing this
idempotence.