---
title: Converging Baseline
act: BaselineConvergence
slug: baseline-convergence
top: ReflexStepIterate
bottom: Nothing
summary: >-
  To see whether an iteration collapses toward pure absence, we compare it
  against the void; this comparison defines baseline convergence.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Converging Baseline

## Interpretation

To see whether an iteration collapses toward pure absence, we compare it against the void; this comparison defines baseline convergence.

The composition `(ReflexStepIterate Nothing)` runs the iterated step against *Nothing*.  If the result agrees with the baseline, we have convergence, hence the name *Baseline Convergence*.