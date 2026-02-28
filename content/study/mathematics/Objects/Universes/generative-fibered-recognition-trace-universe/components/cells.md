---
title: Cells
id: gfrtu-cells
kind: doc
authors:
- gpt-5.2-codex
date-created: 2025-12-26
tags:
- math
---
# Cells

## Definition

A **cell** is a local GFRTU obtained by restricting the trace site $(T,J)$ to a full subcategory $U \subseteq T$ with the induced topology. The corresponding sheaf topos $\mathbf{Sh}(U,J|_U)$ embeds into the global universe.

## Plain-language meaning

A cell is a local sub-universe: it describes how recognitions behave inside a chosen region of traces.

## Minimal structure

- A full subcategory $U$ of the trace site.
- The induced topology $J|_U$.
- The restricted recognition fibers on $U$.

## Entry conditions

Use cells only when:

- You can identify a meaningful subcollection of traces.
- The subcollection is closed under the needed morphisms.

## Example

If $T$ has traces $\{t_0,t_1,t_2\}$, take $U=\{t_0,t_1\}$ with all morphisms between them. The resulting cell describes recognitions on that subsite.
