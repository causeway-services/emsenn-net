---

name: math-for-general-audience
description: Write mathematical texts for non-specialist readers with clear definitions,
  motivating examples, and gradual formalization. Use when the intended audience is
  a general reader without advanced math training.
kind: agent-skill
skill-kind: writing
authors:
- gpt-5.2-codex
date-created: 2025-12-26
id: math-for-general-audience-skill
---

- Define the reader persona with [define-reader-persona](/media/writing/tools/define-reader-persona/SKILL.md) and keep assumptions minimal.
- Start with the meaning of words before symbols, using plain language.
- Provide a concrete example before giving a formal definition.
- Introduce symbols only after the reader has seen the concept in words.
- Keep paragraphs short and avoid stacking multiple new terms at once.
- Rephrase each definition in a second, simpler sentence.
- Use multiple representations: words, a tiny diagram, then symbols.
- Add short "check yourself" questions after new concepts when appropriate.
- Prefer one new term per section; define it before using it again.
- Apply [math-symbol-discipline](/media/writing/tools/math-symbol-discipline/SKILL.md) to ensure domain-appropriate notation.
- Apply [plain-language-writing](/media/writing/tools/plain-language-writing/SKILL.md) for structure and tone.

## Voice cues to emulate

- One new idea per paragraph.
- Frequent reminders of "why this matters" in plain language.
- Examples precede formalism.
- Short recap sentences that restate the last step in plain words.

## Example phrasing

- "A function is just a rule that gives one output for each input."
- "Now that we have the idea, we write it as $f:S \to T$."
- "In short: local pieces that agree can be glued into a global piece."
- "Check: if two inputs are the same, should the outputs be the same?"
