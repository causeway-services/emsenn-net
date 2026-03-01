---
title: Encyclopedia references for tokens
date-created: 2026-01-08T00:00:00
---

# Encyclopedia references for tokens

## Summary
Define a canonical set of encyclopedia entries (concepts, tools, theories) that serve as shared anchors for textual tokens used in agential semioverse interactions. Tokens should map to stable references, reducing ambiguity when agents exchange or log actions.

## Motivation
- Skills and agents exchange tokens referring to concepts or tools; without canonical references, meaning drifts.
- MCP/OpenAPI surfaces should return both data and reference links to these anchors to aid interpretation.

## Potential next steps
- Identify high-frequency tokens in skill manifests and logs; map them to encyclopedia entries.
- Add missing entries (e.g., core math objects, key tools) under `library/encyclopedia/`.
- Update skill outputs to optionally include reference URIs for any token they emit.
- Add validation that emitted tokens reference existing encyclopedia IDs.
