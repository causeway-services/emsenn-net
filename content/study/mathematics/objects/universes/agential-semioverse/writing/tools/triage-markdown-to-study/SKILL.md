---

name: triage-markdown-to-study
description: Normalize triage Markdown into well-formed study documents under /study/{domain}.
  Use when processing triage Markdown files.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: triage-markdown-to-study-skill
---

- Read the source Markdown file under [/inbox/triage/](/inbox/triage/).
- Extract or infer a title from the first H1 or filename.
- Create frontmatter using [frontmatter-schema](/mathematics/objects/agential-semioverse/tools/frontmatter-schema/README.md).
- Quote frontmatter values that include `:` to keep YAML valid.
- Add tags including `triage` and the destination domain.
- Place the file under [/study/{domain}/](/study/).
