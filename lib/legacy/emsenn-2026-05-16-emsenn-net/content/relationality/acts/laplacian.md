---
title: Laplacian
act: Laplacian
slug: laplacian
top: FixedIdentity
bottom: ObservationKernel
summary: >-
  Measure deviation from stationarity by composing the identity with the
  observation kernel.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Laplacian

The Laplacian measures how a state deviates from being stationary, given by
`I − ObservationKernel`.  We capture this by letting the identity observe the
kernel:
`(FixedIdentity ObservationKernel)` earns
***Laplacian***.