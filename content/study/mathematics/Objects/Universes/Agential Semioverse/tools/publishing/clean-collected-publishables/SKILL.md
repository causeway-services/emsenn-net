---

skill_spec_version: "1"
id: clean-collected-publishables-skill
name: clean-collected-publishables
summary: Remove collected publishables from a products output directory
description: >
  Removes the output directory created during document collection,
  resetting the publication build output for a fresh collection.
version: "1.0.0"
kind: skill
skill_kind: automation
authors:
  - emsenn
date-created: 2025-12-26
tags:
  - publishing
  - cleanup
runtime:
  entrypoint: scripts/clean-collected-publishables.py
  language: python
  invocation: cli
inputs:
  - name: config
    description: Path to publication.yml configuration file
    type: path
    required: true
  - name: dry_run
    description: Print the target path without deleting it
    type: boolean
    required: false
    default: false
outputs:
  - name: cleaned_path
    description: Path that was (or would be) removed
    type: path
  - name: success
    description: Whether the cleanup succeeded
    type: boolean
capabilities:
  domains:
    - publishing
  consumes:
    - publication-config
  provides: []
  composable: true
examples:
  - description: Clean emsenn-net publication output
    inputs:
      config: library/agents/emsenn/content/emsenn-net/publication.yml
      dry_run: false
    expected_output:
      cleaned_path: library/agents/emsenn/products/emsenn-net/content
      success: true
---

# Clean Collected Publishables

This skill removes collected publishables from a products output directory, resetting for a fresh build.

## Usage

```bash
python scripts/clean-collected-publishables.py <path-to-publication.yml>
```

## Options

- `--dry-run`: Print the target path without deleting it

## Configuration

The publication config must include:
- `output_root_dir`: Directory to clean
