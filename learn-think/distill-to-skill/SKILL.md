---
name: distill-to-skill
description: |
  Distill a book, method, framework, paper, talk, or course into a source-grounded agent skill with a compact SKILL.md and practical reference files.
  Use when the user says "distill this", "make a skill from this book", "turn X into a skill", "book to skill", or "source to skill".
---

# distill-to-skill — Source to Skill

Preserve the author's framework and turn it into usable instructions. Produce a ≤100-line SKILL.md plus framework deep-dives, case studies, a checklist, and sources.md using [template.md](references/template.md).

**Grounding:** every substantive claim, example, pattern, and number must have a source pointer in the final artifacts. Omit unsupported material; never fill gaps from memory. Read [citation-rules.md](references/citation-rules.md) before writing.

## Process

1. **Clarify** — use the conversation to establish the source, audience, intended use, and destination. Ask only consequential missing questions, bundled together. Draft the description from this context; no mandatory interview or approval gate. See [intake.md](references/intake.md) when input or destination is unclear.
2. **Map** — create a compact sources.md with source locations, coverage limits, and the author's ordered framework sections and passage pointers. Inspect structure first; leave detailed reading to the writer. See [phases.md](references/phases.md) for long or incomplete sources.
3. **Write** — read the relevant passages and write final framework references directly, including applications and guardrails. Handle small sources in the main session. For larger sources, optionally assign related sections to a few workers using [writing-jobs.md](references/writing-jobs.md). Each file has one owner; no separate extraction notes.
4. **Assemble** — the main agent owns SKILL.md and terminology, ordering, cross-section process, diagnostics, case studies, and checklist. Build from finished references; return to source passages only for a specific gap. Link to detailed examples instead of copying them across files.
5. **Check** — apply [review-rubric.md](references/review-rubric.md) once, directly or through one reviewer. Repair specific defects and recheck changed material and affected links. Run `bash <skill-directory>/scripts/check.sh <output-directory>` after final edits. Report path, sources, section count, and any coverage limitations.

## Working rules

- Preserve the output categories and the source's actual section order and count. Depth follows evidence, not minimum line, insight, or example counts.
- Use the user's requested destination. Otherwise stage at `./skills-draft/<slug>/`; install only within the requested scope. No separate confirmation is needed for an already authorized destination.
- Keep source mapping compact: section names, pointers, shared definitions, and coverage limits, not a prose summary of every chapter.
- Read supporting instructions only when relevant. Workers receive their source scope and output template, not every reference file or unrelated completed section.
- Reuse retrieved source text. Browse only for unavailable source material or a specific evidence gap; stop searching when the usable scope is established.
- Resume from valid artifacts after interruption. Reopen only incomplete sections or affected dependencies.
- Mechanical checks establish file validity, not factual accuracy. Never represent their success as proof of grounding.

## Supporting guidance

- [template.md](references/template.md) — required output shape; read before writing
- [citation-rules.md](references/citation-rules.md) — final-artifact evidence conventions
- [phases.md](references/phases.md) — source mapping, assembly, and recovery details
- [writing-jobs.md](references/writing-jobs.md) — optional scoped delegation
- [intake.md](references/intake.md) — source and destination choices
- [description-interview.md](references/description-interview.md) — description guidance when context is insufficient
- [review-rubric.md](references/review-rubric.md) — one concrete review checklist
- [anti-patterns.md](references/anti-patterns.md) — troubleshooting waste and fidelity problems
