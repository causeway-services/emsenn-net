---
title: "Closure Operators as API Contracts"
aliases:
  - "Closure Operators as API Contracts"
  - "closure operators as api contracts"
date-created: 2026-01-06T00:00:00
---


Think of every endpoint as computing a closure: a generator produces candidates, a law L is applied until stable, and the fixed point is returned. Declaring “Endpoint : Generator<S> → FixedPoint<S, L>” tells clients the input/output shape and guarantees:

- **Soundness**: output is closed under L (apply L again, no change).
- **Minimality**: nothing extra beyond what L forces from the seed.
- **Monotonicity**: larger seeds yield larger (never weaker) fixed points, enabling incremental recompute/cache.
- **Idempotence**: re-run returns the same fixed point.

Reusable template:
- Name: e.g., `transitive-closure`
- Law L: “extend by relation R until stable”
- Input (Generator): seed set S
- Output (Fixed Point): least X ⊇ S with “if a R b and a ∈ X then b ∈ X”
- Properties: idempotent, monotone, inflationary, least fixed point
- Observables: iterations to convergence, per-step delta (for SSE), stable hash for caching.

Examples:
- Graph reachability: seed nodes → follow edges to saturation.
- Document normalization: raw doc → apply rewrites until stable.
- Authorization derivation: asserted roles → expand via inheritance until stable.

Verification is light: check idempotence, monotonicity, minimality (remove any element and closure breaks). Composition becomes mechanical: closures over compatible laws compose; distributing laws can swap order safely, turning pipelines into algebra you can rearrange without changing meaning.
