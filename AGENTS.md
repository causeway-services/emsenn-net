# AGENTS.md

General instructions for AI agents working in this repository.

## Project

Quartz 4 static site publishing emsenn's research notes from an Obsidian vault.
Live at **emsenn.net**. The `content/` directory is the Obsidian vault and primary
working area.

## Build

```bash
npm install          # install dependencies
npx quartz build     # build site to public/
npx quartz sync      # build and push (requires git remote)
```

Node version is specified in `.node-version`.

## Content Layout

| Directory              | Purpose                          | Published |
| ---------------------- | -------------------------------- | --------- |
| `content/encyclopedia` | Reference entries                | yes       |
| `content/personal`     | Personal writing                 | yes       |
| `content/study`        | Research notes by discipline     | yes       |
| `content/writing`      | Fiction                          | yes       |
| `content/assets`       | Images and binary files          | yes       |
| `content/slop`         | AI working area — drafts         | no        |
| `content/triage`       | Unprocessed inbox content        | no        |
| `content/meta`         | Obsidian templates               | no        |
| `content/private`      | Private notes (also gitignored)  | no        |

## Frontmatter Schema

```yaml
title: string
date-created: ISO 8601 datetime
```

## File Handling

Large binary files are managed with Git LFS. Tracked types: `pdf`, `epub`, `docx`,
`odt`, `png`, `jpg`, `jpeg`, `gif`, `webp`, `tiff`, `stl`, `3mf`, `obj`, `gcode`,
`mp3`, `mp4`, `wav`, `ogg`.

## Conventions

- Markdown files use LF line endings (enforced by `.gitattributes`)
- Internal links use Obsidian wiki-link syntax: `[[path/to/note|Display Text]]`
- `content/private/` is gitignored — do not stage or reference those files
- Agent-generated drafts belong in `content/slop/`
