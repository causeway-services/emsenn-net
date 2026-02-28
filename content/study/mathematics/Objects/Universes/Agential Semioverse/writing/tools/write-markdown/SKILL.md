---

name: write-markdown
description: Write well-formed Markdown with frontmatter and linked references. Use
  when creating or editing Markdown files in this repository.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: write-markdown-skill
---

- Include YAML frontmatter with required fields as defined by [frontmatter-schema](/mathematics/objects/agential-semioverse/tools/frontmatter-schema/README.md).
- Use Markdown links for file references; do not use backticks for paths.
- Keep one H1 heading that matches the frontmatter title.
- Add `dependencies` or `references` in frontmatter when the document relies on other files.
- If introducing new terms, include a glossary or link to one.
- Quote frontmatter values that include `:` to keep YAML valid.
- Ensure `SKILL.md` names match their directory; ensure `README.md` ids match `<directory>-readme`.
- Use topical tags per [Tags taxonomy](/mathematics/objects/agential-semioverse/practice/tags-taxonomy/README.md).
