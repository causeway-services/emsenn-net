---

skill_spec_version: "1"
id: list-skills-skill
name: list-skills
summary: Discover and list available skills in the library
description: >
  Scans the library for SKILL.md files and returns metadata
  about available skills, including their inputs, outputs,
  and capabilities.
version: "1.0.0"
kind: skill
skill_kind: programming
authors:
  - emsenn
date-created: 2026-01-01
tags:
  - library
  - skills
  - discovery
runtime:
  entrypoint: scripts/list-skills.py
  language: python
  invocation: cli
inputs:
  - name: domain
    description: Filter by capability domain
    type: string
    required: false
  - name: kind
    description: Filter by skill kind (skill, agent-skill)
    type: string
    required: false
    enum:
      - skill
      - agent-skill
  - name: provides
    description: Filter by what the skill provides
    type: string
    required: false
  - name: consumes
    description: Filter by what the skill consumes
    type: string
    required: false
  - name: verbose
    description: Include full skill details
    type: boolean
    required: false
    default: false
outputs:
  - name: skills
    description: List of discovered skills
    type: array
  - name: total
    description: Total number of skills found
    type: integer
capabilities:
  domains:
    - library
    - skills
  consumes: []
  provides:
    - skill-manifest
  composable: true
examples:
  - description: List all skills
    inputs:
      verbose: false
    expected_output:
      total: 15
      skills:
        - id: browse-library
          name: Browse Library
          summary: List directories and read files
  - description: List publishing skills
    inputs:
      domain: publishing
      verbose: true
    expected_output:
      total: 4
---

# List Skills

This skill discovers and lists available skills in the library.

## Usage

```bash
python scripts/list-skills.py
python scripts/list-skills.py --domain publishing
python scripts/list-skills.py --kind agent-skill --verbose
python scripts/list-skills.py --provides html-site
```

## Options

- `--domain`: Filter by capability domain
- `--kind`: Filter by skill kind
- `--provides`: Filter by provided resource type
- `--consumes`: Filter by consumed resource type
- `--verbose`: Include full skill details
