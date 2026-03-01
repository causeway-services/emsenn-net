---
id: inaturalist-practices-purpose-scope-philosophy
kind: doc
authors:
- emsenn
date-created: '2025-12-30'
title: "iNaturalist Practices: purpose, scope, philosophy"
aliases:
  - "iNaturalist Practices: purpose, scope, Philosophy"
tags:
- inaturalist
- citizen-science
---

This site is a critical-practice manual for producing iNaturalist observations that can support scientific use. It treats citizen science as a socio-technical system with known failure modes: platform incentives, uneven effort, misidentifications, and sampling bias. The goal is to help practitioners reduce harm and increase reliability by making their observations auditable and fit for purpose.

## Scope

- **This is not a beginner tutorial.** It assumes you already know how to create observations and navigate iNaturalist.
- **This is not marketing.** Every section is grounded in data outcomes and platform mechanics.
- **This is for co-stewards of data quality.** Observation is an act of data production with downstream consequences.

## Core distinctions

- **Observation ≠ data point.** An observation becomes a usable data record only when context, evidence, and identification support it.
- **Research Grade ≠ unbiased.** Grade is a platform state, not a guarantee of representativeness or correctness.
- **Presence data ≠ abundance.** Most iNaturalist data are presence-only, not a systematic measure of population size.

## Strengths and pitfalls of citizen science

**Strengths**:

- **Scale and coverage:** distributed observers can document large areas and long time spans that formal surveys cannot.
- **Rapid detection:** unusual or invasive species can be reported quickly, creating early warning signals.
- **Public review:** open evidence and comments create an audit trail that can improve records over time.

**Pitfalls**:

- **Uneven effort:** observer behavior drives sampling, not ecological patterns.
- **Validation limits:** community review is uneven across taxa and regions.
- **Context loss:** downstream users often see only the record, not the discussion or uncertainty.

## Indigenous data sovereignty and local governance

Citizen science data can intersect with Indigenous lands, knowledge, and governance. Observations may unintentionally expose culturally sensitive sites or biological resources. Practitioners should treat location data as a responsibility, not an entitlement.

Key implications:

- **Consent and context matter:** recording on or near Indigenous lands should follow local protocols and permissions.
- **Data sovereignty:** Indigenous communities have rights to govern data about their lands and biota. Align practice with CARE Principles for Indigenous Data Governance.
- **Geoprivacy as protection:** use obscured locations when local guidance or cultural sensitivity requires it.

## How iNaturalist data travel

1. **Field observation** is recorded with media, date, and coordinates.
2. **Community review** assigns and revises IDs, sometimes converging on Research Grade.
3. **Data export** to GBIF and other aggregators occurs if licenses and criteria allow.
4. **Downstream use** (models, maps, management reports) often treats records as standardized occurrences.

At each step, uncertainty can increase if evidence is thin or review is limited. This manual focuses on improving the earliest steps because they have the highest leverage.

## What goes wrong if you do this poorly

If observations are created without intent or evidence, they produce false confidence: biased occurrence maps, flawed ecological inferences, and inappropriate management decisions. Harm accumulates when well-intended uploads overwhelm review capacity or amplify charismatic species at the expense of under-observed taxa. These patterns are documented across citizen science platforms and are not hypothetical edge cases.

## Sources and grounding

- iNaturalist help on Data Quality Assessment: <https://www.inaturalist.org/pages/help#quality>
- GBIF guidance on presence-only data and bias: <https://www.gbif.org/document/82642>
- Guralnick et al. (2015) on data quality in biodiversity informatics: <https://doi.org/10.1016/j.tree.2014.12.005>
- Boakes et al. (2010) on bias in biodiversity records: <https://doi.org/10.1111/j.1466-8238.2010.00563.x>
- CARE Principles for Indigenous Data Governance: <https://www.gida-global.org/care>

## Next steps

If you are ready to improve practice, start with these actions:

1. **Clarify intent:** choose a question or ecological purpose for your observations.
2. **Audit evidence quality:** review recent uploads for missing metadata or weak evidence.
3. **Pick a repeatable site:** establish a core location you can revisit across seasons.
4. **Choose a review role:** identify within a taxon where expert coverage is thin.
5. **Document uncertainty:** leave notes when IDs are tentative or evidence is incomplete.

## Civic and open science posture

Citizen science is civic science when it is accountable to place, transparent in method, and open to community review. If you contribute data, you are also participating in the governance of shared knowledge. This site emphasizes open science practices that improve reliability while protecting sensitive information.

## Navigate by topic

If you are looking for a specific practice area, use the [site index](site-index.md) or the [glossary](ecology/topics/citizen-science/inaturalist/terms/glossary.md).

## Interpreting uncertainty by use case

- **Range confirmation:** moderate uncertainty can be acceptable if evidence is clear and location is reliable.
- **Occupancy or distribution modeling:** uncertainty must be modeled explicitly; weak metadata can invalidate outputs.
- **Management decisions:** high uncertainty should trigger verification, not action.

## How DQA flags travel

Data Quality Assessment flags shape whether records are shared to aggregators. Many downstream users filter by Research Grade without checking individual flags or evidence. If a record has issues (e.g., location mismatch, captive status), mark it explicitly to prevent inappropriate reuse.
