---

skill_spec_version: "1"
id: publish-collection-of-documents-skill
name: publish-collection-of-documents
summary: Build a MkDocs site from collected documents
description: >
  Runs mkdocs build on a configured MkDocs project to generate
  a static HTML site from the collected Markdown documents.
version: "1.0.0"
kind: skill
skill_kind: automation
authors:
  - emsenn
date-created: 2025-12-26
tags:
  - publishing
  - mkdocs
  - html
runtime:
  entrypoint: scripts/publish-collection-of-documents.py
  language: python
  invocation: cli
inputs:
  - name: mkdocs_config
    description: Path to mkdocs.yml configuration file
    type: path
    required: true
outputs:
  - name: site_dir
    description: Path to the generated site directory
    type: path
  - name: success
    description: Whether the build succeeded
    type: boolean
capabilities:
  domains:
    - publishing
  consumes:
    - site-directory
    - mkdocs-config
  provides:
    - html-site
  composable: true
examples:
  - description: Build emsenn-net site
    inputs:
      mkdocs_config: library/agents/emsenn/products/emsenn-net/mkdocs.yml
    expected_output:
      site_dir: library/agents/emsenn/products/emsenn-net/site
      success: true
---

# Publish Collection of Documents

This skill builds a MkDocs site from collected Markdown documents.

## Usage

```bash
python scripts/publish-collection-of-documents.py <path-to-mkdocs.yml>
```

## Configuration

The MkDocs config must specify:
- `docs_dir`: Directory containing collected documents
- `site_dir`: Output directory for the HTML site

The script passes the config to `mkdocs build` and relies on MkDocs defaults.
