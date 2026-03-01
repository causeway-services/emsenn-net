---
title: "Enriched Category"
aliases:
  - "Enriched Category"
  - "enriched category"
act: EnrichedCategory
slug: enriched-category
top: EnrichmentTensor
bottom: EnrichmentUnit
summary: >-
  Assemble the enriched units, tensor, and hom-objects into the enriched
  category structure.
tags:
  - act
---

Enrichment requires units, tensor, and hom-objects; we assemble them by letting
the tensor witness the unit and hom:
`(EnrichmentTensor EnrichmentUnit EnrichmentHom)` earns
***EnrichedCategory***.

The act asserts the enriched-category coherence laws for the fixed setting.


{{ act_info(page.meta) }}

{{ act_nav(page.meta) }}
