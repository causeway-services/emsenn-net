---
title: Fixed Kernel
act: FixedKernel
slug: fixed-kernel
top: EnsureFixedPoint
bottom: ObservationKernel
summary: >-
  Apply the fixed-point construction to the observation kernel to obtain its
  stationary behaviour.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Fixed Kernel

A fixed kernel is one whose transition effects stabilise under repeated
application.  Since [ObservationKernel](observation-kernel.md) acts like a
relational operator on fixed states and `EnsureFixedPoint` constructs
fixed points of persistent flows, we apply it directly to the kernel:
`(EnsureFixedPoint ObservationKernel)` earns
***FixedKernel***.

`ObservationKernel` is the evolution–observation operator on fixed invariant
states.  `IterativePersistence` ensures that when iterating this operator along
the trace stabilises, the stable point is a fixed point of the kernel.  Their
composition yields the stationary recognition: the kernel that leaves the fixed
distribution of states unchanged.