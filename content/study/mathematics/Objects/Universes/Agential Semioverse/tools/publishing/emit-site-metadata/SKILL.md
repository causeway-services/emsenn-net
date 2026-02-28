---

skill_spec_version: "1"
id: emit-site-metadata-skill
name: emit-site-metadata
summary: Generate JSON and RDF metadata files for a built MkDocs site
description: >
  Creates machine-readable API files (pages.json, tags.json, pages.ttl)
  from a built MkDocs site for programmatic access to site content.
version: "1.0.0"
kind: agent-skill
skill_kind: automation
authors:
  - emsenn
date-created: 2025-12-30
tags:
  - publishing
  - metadata
  - api
  - rdf
runtime:
  entrypoint: scripts/emit-site-metadata.py
  language: python
  invocation: cli
inputs:
  - name: mkdocs_config
    description: Path to mkdocs.yml configuration file
    type: path
    required: true
outputs:
  - name: pages_json
    description: Path to generated pages.json
    type: path
  - name: tags_json
    description: Path to generated tags.json
    type: path
  - name: pages_ttl
    description: Path to generated pages.ttl (RDF)
    type: path
capabilities:
  domains:
    - publishing
    - metadata
  consumes:
    - html-site
    - mkdocs-config
  provides:
    - json-api
    - rdf-graph
  composable: true
examples:
  - description: Generate metadata for emsenn-net
    inputs:
      mkdocs_config: library/agents/emsenn/products/emsenn-net/mkdocs.yml
    expected_output:
      pages_json: library/agents/emsenn/products/emsenn-net/site/api/pages.json
      tags_json: library/agents/emsenn/products/emsenn-net/site/api/tags.json
      pages_ttl: library/agents/emsenn/products/emsenn-net/site/api/pages.ttl
---

# Emit Site Metadata

This skill generates machine-readable metadata files for a built MkDocs site.

## Usage

```bash
python scripts/emit-site-metadata.py <mkdocs.yml>
```

## Output Files

The script writes to `site/api/`:
- `pages.json`: JSON index of all pages with metadata
- `tags.json`: Tag taxonomy with associated pages
- `pages.ttl`: RDF/Turtle representation of the site graph
