---
title: Enriched Category
act: EnrichedCategory
slug: enriched-category
top: EnrichmentTensor
bottom: EnrichmentUnit
summary: >-
  Assemble the enriched units, tensor, and hom-objects into the enriched
  category structure.
tags:
  - act
date-created: 2025-04-01T00:00:00
---
# Enriched Category

Enrichment requires units, tensor, and hom-objects; we assemble them by letting
the tensor witness the unit and hom:
`(EnrichmentTensor EnrichmentUnit EnrichmentHom)` earns
***EnrichedCategory***.

The act asserts the enriched-category coherence laws for the fixed setting.