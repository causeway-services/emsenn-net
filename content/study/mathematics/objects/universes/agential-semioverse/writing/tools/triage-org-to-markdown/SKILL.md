---

name: triage-org-to-markdown
description: Convert a triage Org file into Markdown+TeX with normalized frontmatter.
  Use when processing inbox/triage content into Markdown.
kind: skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: triage-org-to-markdown-skill
summary: Normalize an Org triage note into Markdown with valid frontmatter.
runtime:
  invocation: manual
  tool: human
inputs:
  - name: source_path
    type: path
    description: Org file to convert (relative to repository root)
    required: true
  - name: target_path
    type: path
    description: Destination Markdown file path (relative to repository root)
    required: false
outputs:
  - name: markdown_path
    type: path
    description: Location of the normalized Markdown file
---

- Read the source `.org` file in [/inbox/triage/](/inbox/triage/).
- Convert with Pandoc: `pandoc -f org -t markdown --wrap=none <file.org>`.
- Create frontmatter using [frontmatter-schema](/mathematics/objects/agential-semioverse/tools/frontmatter-schema/README.md).
- Quote frontmatter values that include `:` to keep YAML valid.
- Place the converted file under [/study/{domain}/](/study/) with a clear filename.
- Remove Org-only directives (`#+` lines, Org export blocks) from the Markdown output.
- Preserve headings, lists, emphasis, and citations; use `[@key]` for citations.
- If the Org content uses inline reference lists, keep them as a `References` section for later normalization.
- Write the Markdown file beside the source with the same basename.
