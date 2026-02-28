---

skill_spec_version: "1"
id: browse-library-skill
name: browse-library
summary: List directories and read files from the library.
description: >
  Browse the Emsemioverse library filesystem: list directories, read file
  contents, or extract frontmatter metadata from Markdown files.
version: "1.0.0"
kind: skill
skill_kind: programming
authors:
  - emsenn
date-created: 2026-01-01
tags:
  - library
  - browsing
  - filesystem
runtime:
  entrypoint: scripts/browse-library.py
  language: python
  invocation: cli
inputs:
  - name: path
    description: Path relative to library root to browse
    type: path
    required: false
    default: ""
  - name: action
    description: Action to perform
    type: string
    required: true
    enum:
      - list
      - read
      - metadata
  - name: recursive
    description: Whether to list recursively (for list action)
    type: boolean
    required: false
    default: false
  - name: max_depth
    description: Maximum depth for recursive listing
    type: integer
    required: false
    default: 3
  - name: include_hidden
    description: Whether to include hidden files
    type: boolean
    required: false
    default: false
outputs:
  - name: entries
    description: Directory entries for list action
    type: array
  - name: content
    description: File content for read action
    type: string
  - name: frontmatter
    description: Parsed frontmatter for metadata action
    type: object
---

# Browse Library

This skill provides browsing capabilities for the library filesystem.

## Usage

```bash
python scripts/browse-library.py --action list --path skills/publishing
python scripts/browse-library.py --action read --path skills/publishing/SKILL.md
python scripts/browse-library.py --action metadata --path study/git/README.md
```

## Actions

- `list`: List directory contents
- `read`: Read file contents
- `metadata`: Extract frontmatter from markdown files

## Options

- `--path`: Path relative to library root (default: root)
- `--recursive`: List subdirectories recursively
- `--max-depth`: Maximum depth for recursive listing
- `--include-hidden`: Include hidden files/directories
