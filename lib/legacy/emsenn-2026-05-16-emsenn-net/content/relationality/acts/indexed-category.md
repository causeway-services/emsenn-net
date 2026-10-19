---
title: Indexed Category
act: IndexedCategory
slug: indexed-category
top: IndexBase
bottom: FiberCategory
summary: >-
  Package the base, fibers, and reindexing into the internal indexed category of
  contexts.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Indexed Category

An indexed category is a functor from the base contexts to categories of
fibres, with reindexing functors on morphisms.  We combine the base, fibres, and
reindexing into this structure:
`(IndexBase FiberCategory Reindexing)` earns
***IndexedCategory***.

`IndexBase` gives the contexts, `FiberCategory` provides the fibre
categories, and `Reindexing` maps context morphisms to fibre functors,
encoding an internal functor `IndexBaseᵒᵖ → Cat`.