---

skill_spec_version: "1"
id: collect-documents-for-publishing-skill
name: collect-documents-for-publishing
summary: Collect documents matching publication criteria into a MkDocs docs directory
description: >
  Scans the library for Markdown files whose frontmatter publications list matches
  a publication_name/publication_status pair, then copies matching files into the
  configured docs_dir preserving their paths.
version: "1.0.0"
kind: skill
skill_kind: automation
authors:
  - emsenn
date-created: 2025-12-26
tags:
  - publishing
  - mkdocs
runtime:
  entrypoint: scripts/collect-documents-for-publishing.py
  language: python
  invocation: cli
inputs:
  - name: config
    description: Path to publication.yml configuration file
    type: path
    required: true
  - name: source
    description: Source directory to scan for documents
    type: path
    required: false
    default: library
  - name: dry_run
    description: Print matches without copying files
    type: boolean
    required: false
    default: false
outputs:
  - name: collected_count
    description: Number of documents collected
    type: integer
  - name: docs_dir
    description: Path to the output docs directory
    type: path
capabilities:
  domains:
    - publishing
  consumes:
    - markdown-file
    - publication-config
  provides:
    - site-directory
  composable: true
examples:
  - description: Collect documents for emsenn-net publication
    inputs:
      config: library/agents/emsenn/content/emsenn-net/publication.yml
      dry_run: false
    expected_output:
      collected_count: 42
      docs_dir: library/agents/emsenn/products/emsenn-net/content
---

# Collect Documents for Publishing

This skill collects Markdown documents from the library that are marked for a specific publication.

## Usage

```bash
python scripts/collect-documents-for-publishing.py <path-to-publication.yml>
```

## Configuration

The publication config must include:
- `publication_name`: Name of the publication
- `publication_status`: Status to match (e.g., "publishable")
- `docs_dir`: Output directory for collected documents

Optional config keys:
- `output_root_dir`: Directory that receives `mkdocs.yml` plus `overrides/` from the publication config folder
- `extra_source_dirs`: Comma-separated list or bracketed list of directories to copy into `docs_dir`
- `extra_source_dir`: Single directory to copy into `docs_dir`
- `overrides_dir`: Directory to copy into `docs_dir/overrides`

## How It Works

1. Scans Markdown files in the source directory
2. Parses frontmatter for a `publications` list
3. Matches entries of the form `{publication}: {status}`
4. Copies matching files to `docs_dir`, preserving paths
5. Copies declared `dependencies` alongside matched files
6. Generates `references.bib` from frontmatter `references` lists

## Example Frontmatter

```yaml
publications:
  - emsenn-net: publishable
```
