---
title: "Heyting Algebras"
aliases:
  - "Heyting Algebras"
  - "heyting-algebras"
id: order-theory-lesson-3
kind: curriculum-lesson
authors:
  - claude-opus-4-6
date-created: 2026-03-01T00:00:00
tags:
  - math
  - order-theory
  - logic
dependencies:
  - /mathematics/objects/posets/curricula/lattices.md
---

## Entry conditions

Use Heyting algebras when you can:

- Start from a lattice with top $\top$ and bottom $\bot$.
- Define an implication operation $a \Rightarrow b$ for every pair of elements.
- Accept that some elements may lack complements — excluded middle may fail.

## Definitions

A **bounded lattice** is a lattice with a greatest element $\top$ and a least element $\bot$.

A **Heyting algebra** is a bounded lattice $(H, \leq, \wedge, \vee, \bot, \top)$ equipped with a binary operation $\Rightarrow$ (called Heyting implication) satisfying:

$$
c \leq (a \Rightarrow b) \quad \text{iff} \quad c \wedge a \leq b
$$

for all $a, b, c \in H$.

A Heyting algebra is **complete** when every subset (not just every pair) has a meet and a join — that is, the underlying lattice is a complete lattice.

A **Boolean algebra** is a Heyting algebra where every element $a$ has a complement $\neg a$ such that $a \wedge \neg a = \bot$ and $a \vee \neg a = \top$. In a Boolean algebra, excluded middle holds universally. In a general Heyting algebra it does not.

## Vocabulary (plain language)

- **Implication**: the largest element whose meet with $a$ stays below $b$. Read $a \Rightarrow b$ as "the extent to which $a$ entails $b$."
- **Pseudocomplement**: the element $\neg a := a \Rightarrow \bot$, the largest element disjoint from $a$. Unlike a Boolean complement, $a \vee \neg a$ need not equal $\top$.
- **Complete**: every collection of elements (not just pairs) has a meet and a join.

## Symbols used

- $\wedge$: meet (greatest lower bound).
- $\vee$: join (least upper bound).
- $\Rightarrow$: Heyting implication.
- $\neg a$: pseudocomplement, shorthand for $a \Rightarrow \bot$.
- $\top, \bot$: top and bottom elements.

## Intuition

A Boolean algebra is the algebra of yes-or-no propositions: every statement is either true or false. A Heyting algebra drops that assumption. Propositions can be partial, underdetermined, or context-dependent — an element may have a pseudocomplement without having a full complement. This makes Heyting algebras the natural algebraic setting for reasoning about meaning, evidence, and constructive proof, where you cannot always assert that a claim is either established or refuted.

The standard source of Heyting algebras is topology: the open sets of any topological space, ordered by inclusion, form a complete Heyting algebra. The interior of the complement of an open set $U$ is its pseudocomplement, but $U$ together with its pseudocomplement may not cover the whole space — points on the boundary belong to neither.

## Worked example

Let $X = \{0, 1\}$ with the topology $\tau = \{\emptyset, \{0\}, \{0,1\}\}$ (the Sierpinski space). The open sets ordered by inclusion form a Heyting algebra:

| $a$ | $b$ | $a \Rightarrow b$ |
|-----|-----|--------------------|
| $\emptyset$ | any | $\{0,1\}$ |
| $\{0\}$ | $\emptyset$ | $\emptyset$ |
| $\{0\}$ | $\{0\}$ | $\{0,1\}$ |
| $\{0\}$ | $\{0,1\}$ | $\{0,1\}$ |
| $\{0,1\}$ | $\emptyset$ | $\emptyset$ |
| $\{0,1\}$ | $\{0\}$ | $\{0\}$ |
| $\{0,1\}$ | $\{0,1\}$ | $\{0,1\}$ |

The pseudocomplement of $\{0\}$ is $\{0\} \Rightarrow \emptyset = \emptyset$. So $\{0\} \vee \neg\{0\} = \{0\} \vee \emptyset = \{0\} \neq \{0,1\}$. Excluded middle fails.

This is a complete Heyting algebra (it is finite, so every subset has a meet and join).

## Applications

Heyting algebras arise in topology (the open sets of any topological space form a complete Heyting algebra), in constructive logic (as the Lindenbaum-Tarski algebras of [intuitionistic logic](../../../disciplines/logic/curricula/intuitionistic-logic.md)), in sheaf theory (the subobject classifier of a topos is a Heyting algebra), and in any domain where reasoning involves partial or contextual evidence rather than binary truth and falsity.

## How to recognize the structure

- You have a lattice with top and bottom.
- For any pair $a, b$ you can identify a largest element $c$ such that $c \wedge a \leq b$.
- If some elements lack complements (i.e. $a \vee \neg a \neq \top$ for some $a$), you have a proper Heyting algebra rather than a Boolean one.

## Common mistakes

- Assuming excluded middle. In a Heyting algebra, $a \vee \neg a = \top$ is not guaranteed. Check before using it.
- Confusing pseudocomplement with complement. The pseudocomplement $\neg a$ is the largest element disjoint from $a$, but $a$ and $\neg a$ may not cover the whole algebra.
- Treating implication as material implication. In classical logic, $a \Rightarrow b$ equals $\neg a \vee b$. In a Heyting algebra, this identity can fail.

## Minimal data

- A complete lattice $(H, \leq)$ with $\top$ and $\bot$.
- An implication operation $\Rightarrow$ satisfying the adjunction: $c \leq (a \Rightarrow b)$ iff $c \wedge a \leq b$.

## References

- Johnstone, Peter T. *Stone Spaces*. Cambridge: Cambridge University Press, 1982. (Heyting algebras in the context of locale theory and topology.)
- Davey, B. A., and H. A. Priestley. *Introduction to Lattices and Order*. 2nd ed. Cambridge: Cambridge University Press, 2002. (Accessible introduction to lattice theory including Heyting algebras.)
- Esakia, Leo. *Heyting Algebras: Duality Theory*. Edited by Guram Bezhanishvili and Wesley H. Holliday. Cham: Springer, 2019.
