---
title: "Parametric Comonad reindexing"
aliases:
  - "Parametric Comonad reindexing"
  - "parametric comonad reindexing"
act: ParametricComonadReindex
slug: parametric-comonad-reindex
top: Reindexing
bottom: ParametricComonadFiber
summary: >-
  Ensure reindexing commutes with the fibrewise comonad by composing
  `Reindexing` with the comonad action.
tags:
  - act---

Reindexing must commute with the coeffect action, so we let reindexing observe
the fibrewise flow:
`(Reindexing ParametricComonadFiber)` earns
***ParametricComonadReindex***.


{{ act_info(page.meta) }}

{{ act_nav(page.meta) }}
