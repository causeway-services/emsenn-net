---

skill_spec_version: "1"
id: search-library-skill
name: search-library
summary: Full-text search across library markdown content
description: >
  Searches the library for content matching a query string,
  returning matching files with context and relevance scores.
  Supports searching in content, frontmatter, or both.
version: "1.0.0"
kind: skill
skill_kind: programming
authors:
  - emsenn
date-created: 2026-01-01
tags:
  - library
  - search
  - fulltext
runtime:
  entrypoint: scripts/search-library.py
  language: python
  invocation: cli
inputs:
  - name: query
    description: Search query string
    type: string
    required: true
  - name: scope
    description: Where to search
    type: string
    required: false
    default: all
    enum:
      - all
      - content
      - frontmatter
      - title
  - name: path
    description: Path to limit search to (relative to library root)
    type: path
    required: false
    default: ""
  - name: kind
    description: Filter by document kind
    type: string
    required: false
  - name: limit
    description: Maximum number of results
    type: integer
    required: false
    default: 20
  - name: context_lines
    description: Number of context lines around matches
    type: integer
    required: false
    default: 2
outputs:
  - name: results
    description: List of search results
    type: array
    schema_ref: search-result
  - name: total_matches
    description: Total number of matches found
    type: integer
capabilities:
  domains:
    - library
    - search
  consumes: []
  provides:
    - search-result
  composable: true
examples:
  - description: Search for documents about git
    inputs:
      query: git
      scope: all
      limit: 10
    expected_output:
      total_matches: 15
      results:
        - path: study/git/README.md
          score: 0.95
          matches:
            - line: 1
              text: "# Git"
  - description: Search skills for publishing
    inputs:
      query: publishing
      path: skills
      kind: skill
    expected_output:
      total_matches: 4
---

# Search Library

This skill provides full-text search across library markdown content.

## Usage

```bash
python scripts/search-library.py --query "relational dynamics"
python scripts/search-library.py --query git --path study --limit 5
python scripts/search-library.py --query skill --scope frontmatter --kind skill
```

## Options

- `--query`: Search query string (required)
- `--scope`: Where to search (all, content, frontmatter, title)
- `--path`: Limit search to a subdirectory
- `--kind`: Filter by document kind from frontmatter
- `--limit`: Maximum results to return
- `--context-lines`: Lines of context around matches
