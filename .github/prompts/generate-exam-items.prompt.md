---
description: "Generate AI-900 practice exam items grounded in Microsoft Learn docs"
agent: "agent"
tools: ["search/codebase"]
---

Generate ${input:count:3} AI-900 practice exam items for the "${input:domain:generative AI}" domain at Bloom's ${input:level:Apply} level.

Before writing any items, search Microsoft Learn for the current AI-900 study guide objectives for this domain.

Follow the format and rules in [practice question standards](../../.github/instructions/practice-questions.instructions.md).

Each item must include:
- A workplace scenario stem using Microsoft fictional companies
- 4 options (A-D) with exactly 1 correct
- Rationale for ALL options inside a `<details>` block
- A Microsoft Learn reference URL

Use ONLY current Azure terminology per [copilot instructions](../../.github/copilot-instructions.md).
