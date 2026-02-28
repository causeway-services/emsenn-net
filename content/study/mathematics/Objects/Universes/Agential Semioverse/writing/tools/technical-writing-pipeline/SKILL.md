---

name: technical-writing-pipeline
description: Chain writing skills into a technical-writing workflow with branching
  by audience and content type. Use when starting a technical document.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: technical-writing-pipeline-skill
---

- Define the reader persona using [define-reader-persona](/media/writing/tools/define-reader-persona/SKILL.md).
- Apply [emstyle-voice](/media/writing/tools/emstyle-voice/SKILL.md).
- If the audience is general, apply [plain-language-writing](/media/writing/tools/plain-language-writing/SKILL.md).
- If the document is mathematical, apply [compose-math-docs](/media/writing/tools/compose-math-docs/SKILL.md); otherwise apply [technical-writing](/media/writing/tools/technical-writing/SKILL.md).
- Apply [write-markdown](/media/writing/tools/write-markdown/SKILL.md) for frontmatter and link rules.
- Apply [avoid-vague-adverbs](/media/writing/tools/avoid-vague-adverbs/SKILL.md) and [contractions-consistency](/media/writing/tools/contractions-consistency/SKILL.md) during revision.
- If the document introduces new terms, apply [write-glossary](/media/writing/tools/write-glossary/SKILL.md).
