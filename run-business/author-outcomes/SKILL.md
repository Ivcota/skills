---
name: author-outcomes
description: >-
  Scaffolds or co-authors product/context/outcomes.md from the paired template.
  Facilitates outcomes one at a time with L1/L2 metrics. Does not invent
  outcomes or Today/Target values. Use when the user wants outcomes, success
  criteria, measurable prep, or readiness for a project, event, or engagement.
disable-model-invocation: true
---

# Author outcomes

Single job: produce or update **`product/context/outcomes.md`** using **`outcomes-template.md`** in this skill directory.

## Non-negotiables

1. **Do not invent outcomes.** Names and paragraphs come from the user (PM/owner). You propose structure and wording only after they choose an outcome theme.
2. **Do not invent metrics.** Never fabricate **Today** or **Target**. Use `_you fill_`, **Draft:** (provisional), or **N/A** until the user attests.
3. **One outcome at a time** when co-authoring. Finish Outcome *n* (name → paragraph → metrics) before starting *n+1*.
4. **Do not overwrite** an existing file with `status: ratified` unless the user explicitly asks.

## Paths

| Item | Path |
| --- | --- |
| Template | `.cursor/skills/author-outcomes/outcomes-template.md` |
| Output | `product/context/outcomes.md` |

Create `product/context/` if missing.

## Mode A — Scaffold (empty or new engagement)

1. Read the template.
2. Set frontmatter: `engagement` = repo folder name or user slug; `last-revised` = today (ISO date); `status: draft`.
3. Replace `<Title>`, `<slug>`, `<owner>` from user input (ask once if missing).
4. Leave outcome bodies and metric cells empty or as template placeholders.
5. Tell the owner what they must author (3–5 outcomes, 2–4 metrics each, counter-outcomes, boundaries).

## Mode B — Co-author (user is ready to fill content)

For each outcome, in order:

1. **Pick theme** — Offer 2–4 optional themes OR accept the user’s short title.
2. **Paragraph** — Draft one paragraph from their answers; they edit.
3. **Metrics** — Table with **L2** (leading: what moves first) then **L1** (lagging: result). Include **Today | Target | Source**.
4. **Help with Today/Target** — Give a short checklist (concrete actions), then **Draft:** rows they can confirm or correct. Update the file when they confirm.
5. Stop when the user says they are done; do not pad extra outcomes.

## Metric rules

- **L2**: Prep steps, rehearsals, checklists, counts, time estimates.
- **L1**: End state or post-event judgment (often filled after the fact).
- **Source**: Workbook, schedule, notes, self-review — something verifiable.

## Optional sections

- **Counter-outcomes**: Guardrails (e.g. “don’t rush speakers”).
- **What this list does not cover**: Scope boundary.

Skip Outcome 3+ placeholders if the user only needs 1–2 outcomes.

## User asks to “open” the file

Open `product/context/outcomes.md` in the editor (`open -a Cursor <path>` on macOS) and show the relevant section in chat.

## Done report

One line: path, count of outcomes authored, `status: draft` until the owner ratifies.

## Example invocation

> Author outcomes for a team workshop — agenda flow and participant experience, one at a time.

Agent: scaffold if needed → Outcome 1 (flow) with metric table → wait for confirm → Outcome 2 (experience) → stop.
