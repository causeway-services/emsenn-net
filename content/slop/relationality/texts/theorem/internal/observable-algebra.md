---
title: Observable Algebra
tags:
  - measure
  - observable
  - algebra
depends_on:
  - measure
  - profile-measure
  - profile-integral
  - profile-entropy-measure
  - profile-entropy-seed
  - flow-observation
  - flow-observation-equivalence
---
# Theorem (Observable Algebra)

The measurement acts—`Measure`, `ProfileMeasure`, `ProfileIntegral`,
`FlowObservation`, etc.—assemble into an algebra of observables compatible with
the flow and nucleus.  This theorem packages the internal witnesses.

## 1. Basic observables

**Theorem 1 (Observation data).**  
[Observables](slop/relationality/texts/theorem/internal/observables.md) already describe the fixed observation recognitions,
normalization, and observational sufficiency.  They show that observables are
internal to the fixed profile and that normalization collapses step traces.

## 2. Measures and integration

**Theorem 2 (Measure and integral).**  
[Measure](measure.md),
[Profile Measure](profile-measure.md), and
[Profile Integral](profile-integral.md) equip the fixed profile
with measure/integration operators.  Their proofs show how flow-observation steps
push measures forward.

*Proof sketch.* `ProfileMeasure` builds the measure algebra on recognitions;
`ProfileIntegral` integrates observables against those measures by iterating
`FlowObservation`.  The recorded commutation ensures compatibility with flow. ∎

## 3. Algebraic structure

**Theorem 3 (Algebra of observables).**  
[Profile Entropy Measure](profile-entropy-measure.md),
[Profile Entropy Seed](profile-entropy-seed.md), and
[Profile Integral](profile-integral.md) show that observables form
a lattice-ordered algebra closed under addition and scalar multiplication (inside
the semantics layer).  [Flow Observation](flow-observation.md) and
[Flow Observation Equivalence](flow-observation-equivalence.md)
ensure the algebra is invariant under flow.

*Proof sketch.* These acts explicitly define addition/ordering on observables and
prove closure under flow.  The equivalence act shows that flow-identical
observables are identified, giving the usual quotient by null observations. ∎

## 4. Compatibility with physics invariants

**Theorem 4 (Sound measurements).**  
[Physics Soundness and Invariants](slop/relationality/texts/theorem/internal/physics-soundness-invariants.md) ensures every
observable stays within the fixed geometry/semantics.  [Relational Markov Dynamics](../../external/relational-markov-dynamics.md)
and [Mixing and Ergodic Invariants](mixing-ergodicity.md) provide the probabilistic
interpretation.

*Proof sketch.* The soundness lemma records that observables remain valid in the
fixed semantics; the Markov theorem shows how they integrate against stationary
kernels. ∎

## Summary

| Observable feature | Witnessing acts |
| ------------------ | ---------------- |
| Fixed observations | `Observables`, `FlowObservation` |
| Measure/integration | `Measure`, `ProfileMeasure`, `ProfileIntegral` |
| Algebraic structure | `ProfileEntropyMeasure`, `ProfileEntropySeed`, `FlowObservationEquivalence` |
| Compatibility | `Physics Soundness and Invariants`, `Relational Markov Dynamics` |

This theorem gives the internal algebra needed for any measurement correspondence.
