# Output template

The exact shape SKILL.md must take. Placeholders in `{braces}`. Do not omit sections unless noted. Do not add sections not in this template unless the source has a structural element that demands one.

---

```markdown
---
name: {slug}
description: |
  {One sentence: what the skill does, in third person, naming the author's core framework.}
  {One sentence on what makes it distinct — the signature concept or scoring model.}
  Use when the user mentions {3-5 direct trigger phrases} or {2-3 problem phrases}. Also trigger when {2-3 artifact/context phrases}.
  {Optional: For X, see other-skill. For Y, see other-skill.}
---

# {Framework Name}

{2-3 sentence overview. What the framework is, who wrote it, the one-sentence thesis. Ground in the source.}

## Core Principle

{2-3 paragraphs. Lead with the thesis. Explain the foundation. End with what makes this framework a category of one.}

**The foundation:** {The author's own foundational claim, closely paraphrased or quoted.}

## Scoring

{If the source has a scoring model, describe it here — scale, what a top score means, what to do with lower scores (e.g., "Goal: 10/10" style). If the source has no scoring model, omit this section.}

## The {Framework Name} Framework

### 1. {Section name — author's term}

**Core concept:** {One paragraph. The author's own explanation, closely paraphrased.}

**Why it works:** {One paragraph. The mechanism. Why this lever / pillar / pattern produces the result.}

**Key insights:**
- {Insight 1 — from extraction notes, cited}
- {Insight 2}
- {Insight 3 — aim for 5-7 total}

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **{Context 1}** | {How this section applies} | {Specific quoted example} |
| **{Context 2}** | {...} | {...} |
| **{Context 3}** | {...} | {...} |
| **{Context 4}** | {...} | {...} |
| **{Context 5}** | {...} | {...} |

*Only include rows the source covers. If the source only has B2B examples, don't invent B2C rows.*

**Copy patterns:**
- "{Pattern 1, with [placeholders]}"
- "{Pattern 2}"
- "{Pattern 3 — aim for 4-6 total}"

**Ethical boundary:** {The author's own guardrail for this section. If the author doesn't state one for this section, omit this line — do not synthesize generic ethics.}

See: [references/{section-slug}.md](references/{section-slug}.md) for {specific depth promise}.

### 2. {Next section...}

{Repeat structure. Match the author's section count — 4, 6, 8, 10 — don't force a number.}

## {Framework Name} Process

Follow these steps in order to apply the framework from scratch:

1. **{Imperative verb + object}.** {One-sentence elaboration.}
2. **{Next step}.** {...}
3. ...

*Prefer the author's own sequence. If inferred from structure, note which section each step comes from.*

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| **{Mistake 1}** | {Author's reasoning} | {Author's prescription} |
| **{Mistake 2}** | {...} | {...} |
| *≥5 rows* | | |

## Quick Diagnostic

Use this table to audit an existing {artifact — offer, campaign, product, etc.}:

| Question | If No | Action |
|----------|-------|--------|
| {Diagnostic question 1} | {Failure symptom} | {Remediation} |
| {Q2} | {...} | {...} |

*Questions should map to framework sections 1:1 where possible.*

## Reference Files

- [{section-1-slug}.md](references/{section-1-slug}.md): {One-line description}
- [{section-2-slug}.md](references/{section-2-slug}.md): {...}
- [case-studies.md](references/case-studies.md): Detailed worked examples across {contexts}
- [checklist.md](references/checklist.md): Step-by-step worksheet and scoring rubric

## Further Reading

{One sentence: this skill is based on {work} by {author}. For the complete methodology:}

- [*"{Title}"*]({verified URL}) by {Author}
- {Additional verified titles by same author, if any}

## About the Author

**{Author name}** {2-3 sentences, grounded in a cited source. Role, credentials, why they have authority on this topic. No invention.}
```

---

## Synthesis rules

- **Section count follows the source.** If the source has 4 pillars, the skill has 4. Never pad to a target count.
- **Every bullet must trace to a citation** in `sources.md`.
- **Tables shrink when evidence is thin.** A 3-row application table beats a 5-row table with 2 invented rows.
- **Ethical-boundary lines are optional per section.** Only include when the author has explicit guardrails for that section.
- **Voice matches the source.** If the author is plain-spoken and direct, the skill is too. Don't translate into generic marketing-speak.
- **No metadata drift.** Keep a stable frontmatter schema (name, description, license optional, metadata.author optional, metadata.version optional).
