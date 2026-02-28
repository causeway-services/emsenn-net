---
title: Theorem of necessary misalignment of truth value under epistemic constraint
date-created: 2025-09-21
title-class: "1"
note-length-class: "0"
inlink-class: "0"
outlink-class: "0"
progressive-summarization-maturity: "0"
note-maturity: "0"
---
# Theorem of necessary misalignment of truth value under epistemic constraint

## Abstract
We establish a general theorem describing the inevitable trade-off between proxy optimization and semantic fidelity under finite epistemic capacity. A bounded agent is modeled as an encoder $p_\theta(y|x)$ producing messages $Y$ from inputs $X$, subject to a rate constraint $I(X;Y)\le R$. The environment defines a latent **semantic variable** $T$ and a computable **proxy reward** $r(Y)$. When the sufficient statistics for $r$ differ from those sufficient for $T$, optimization that increases expected reward necessarily increases semantic distortion $D_T$ and decreases decoder-level semantic information $I(T;S)$.

This **necessary misalignment** follows from the geometry of the achievable region in rate–distortion space and holds for any selection process that monotonically increases reward. The result formalizes a general informational limit on alignment in bounded optimization.

## Introduction
Bounded rational agents must compress observations $X$ into finite representations $Y$ to act on or communicate about the world. When their optimization objective depends on a computable **proxy** $r(Y)$ that is only partially informative about a **semantic** variable $T$, the achievable trade-off between reward and semantic fidelity forms a Pareto frontier. We show that, under mild assumptions, any selection dynamics that increase expected reward move the system along this frontier in a direction that necessarily increases semantic distortion and reduces semantic information. The theorem does not depend on any specific architecture, loss function, or empirical domain.

## Probabilistic Setting
Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space supporting random variables $T\in\mathcal{T}$ (semantic or “truth” variable), $X\in\mathcal{X}$ (input context), $Y\in\mathcal{Y}$ (encoded message), and $S=s(Y)\in\mathcal{S}$ (semantic decoding). The joint source $p(t,x)$ specifies the dependence between $T$ and $X$.

> **Definition (Encoder and Rate Constraint).** An encoder is a Markov kernel $p_\theta(y|x)$. It is rate-bounded if $I(X;Y)\le R$ where mutual information is computed under $p(t,x)p_\theta(y|x)$.

> **Definition (Semantic Distortion).** Fix a measurable loss $d_T:\mathcal{T}\times\mathcal{S}\to[0,\infty)$. For an encoder–decoder pair $(\theta,s)$, the semantic distortion is $D_T(\theta,s)=\mathbb{E}[d_T(T,S)]$ with $S=s(Y)$.

A **proxy reward** is any measurable function $r:\mathcal{Y}\to\mathbb{R}$. The agent’s expected reward is $\mathbb{E}[r(Y)]$.

## Information-Theoretic Preliminaries
> **Definition (Mutual Information).** For random variables $X,Y$ with joint law $p(x,y)$, $I(X;Y)=\mathbb{E}_{p(x,y)}\![\log\tfrac{p(x,y)}{p(x)p(y)}]$.

> **Definition (Semantic Rate–Distortion Function).** Given $p(t)$ and distortion $d_T$, the semantic rate–distortion function is $R_T(D)=\inf_{p(s|t):\mathbb{E}[d_T(T,S)]\le D} I(T;S)$, the minimal information rate required to achieve expected distortion $\le D$. The function $R_T(D)$ is non-increasing and convex.

> **Lemma (Data-Processing Inequality).** For $T\to Y\to S$, $I(T;S)\le I(T;Y)$ with equality iff $S$ is $T$-sufficient for $Y$.

## Proxy–Semantic Mismatch and Achievable Region
> **Assumption (Strict Proxy–Semantic Mismatch).** No encoder–decoder pair $(\theta,s)$ with $I(X;Y)\le R$ simultaneously maximizes $\mathbb{E}[r(Y)]$ and minimizes $D_T(\theta,s)$. Equivalently, no statistic of $Y$ that is sufficient for $T$ is also reward-optimal at rate $R$.

> **Assumption (Convexity and Time-Sharing).** For fixed $R$, the set $\mathcal{A}_R =\{(\mathbb{E}[r(Y)],\, D_T(\theta,s)) : I(X;Y)\le R\}$ is convex and compact, as ensured by bounded losses and time-sharing.

> **Proposition (Monotone Trade-Off Frontier).** Under strict mismatch, the efficient frontier of $\mathcal{A}_R$ satisfies $\tfrac{dD_T}{d\,\mathbb{E}[r(Y)]}>0$ where differentiable.

> **Proof sketch.** If the frontier had non-positive slope, one could increase reward without increasing distortion, contradicting strict mismatch. Convexity guarantees existence and monotonicity of the frontier.

## Selection Dynamics
Let $\pi_\kappa$ be a population distribution over encoders $\theta$ that evolves under replicator or logit dynamics with fitness $F(\theta)=\mathbb{E}[r(Y_\theta)]$ and selection intensity $\kappa>0$. Larger $\kappa$ concentrates $\pi_\kappa$ on encoders with higher expected reward.

## Theorem 1
> **Theorem (Necessary Misalignment under Epistemic Constraint).** Fix a finite rate $R<\infty$, a distortion measure $d_T$, and source distribution $p(t,x)$. Assume strict proxy–semantic mismatch and convexity of $\mathcal{A}_R$. Then there exists $\kappa_c>0$ such that for all $\kappa>\kappa_c$,
> \[
> \frac{dD_T(\kappa)}{d\kappa}>0,\qquad \frac{dR_T(D_T(\kappa))}{d\kappa}<0.
> \]
> If the decoder $s_\kappa$ is semantically efficient ($I(T;S_\kappa)=R_T(D_T(\kappa))$), then $\tfrac{dI(T;S_\kappa)}{d\kappa}<0$.

> **Proof sketch.** As selection intensity $\kappa$ increases, $\pi_\kappa$ shifts toward reward-maximizing encoders on $\partial\mathcal{A}_R$. By the monotone frontier, $D_T(\kappa)$ increases with expected reward. Because $R_T(D)$ is non-increasing, $R_T(D_T(\kappa))$ decreases. Under semantic efficiency, $I(T;S_\kappa)=R_T(D_T(\kappa))$, yielding a strict decline of semantic information with $\kappa$.

## Corollary (Information Bound)
By the data-processing inequality, $I(T;S_\kappa)\le I(T;Y_\kappa)$. Hence a decrease of $I(T;S_\kappa)$ implies a non-increasing lower bound on $I(T;Y_\kappa)$, quantifying unavoidable semantic information loss under intensified optimization.

## Remarks and Edge Cases
1. **Sufficiency.** If the proxy reward $r(Y)$ is $T$-sufficient for $Y$, the frontier may be locally flat, and misalignment need not increase. This equality case is excluded by the strict mismatch assumption.
2. **Scope of “necessary.”** Necessity is with respect to the assumptions: finite rate, mismatch, convexity, and selection that increases reward efficiently.
3. **Why decoder-level information.** Semantic performance is realized through the decoded variable $S=s(Y)$; rate–distortion bounds directly relate $D_T$ and $I(T;S)$, and DPI then connects $I(T;S)$ to $I(T;Y)$.

## Discussion
The theorem identifies misalignment as a structural consequence of limited epistemic capacity. Whenever optimization intensifies for a mismatched proxy under fixed rate $R$, the system traverses the achievable frontier, sacrificing semantic information about $T$ to improve computable reward. Improving alignment therefore requires **epistemic expansion** (increasing $R$) or **proxy refinement** (reducing mismatch between $r$ and $T$). The result applies to any bounded optimizer, regardless of implementation, and situates alignment limits within classical rate–distortion theory and evolutionary dynamics.

## References
- C. E. Shannon. *A Mathematical Theory of Communication.* Bell System Technical Journal 27 (1948).
- T. M. Cover & J. A. Thomas. *Elements of Information Theory.* Wiley (2006).
- I. Csiszár & J. Körner. *Information Theory: Coding Theorems for Discrete Memoryless Systems.* Cambridge (2011).
- A. Kolchinsky & D. H. Wolpert. *Semantic Information and Its Measures.* Entropy 20 (12): 884 (2018).
- J. Hofbauer & K. Sigmund. *Evolutionary Games and Population Dynamics.* Cambridge (1998).
