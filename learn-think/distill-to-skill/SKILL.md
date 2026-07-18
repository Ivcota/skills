---
name: distill-to-skill
description: |
  Distill a book, method, or framework into an agent skill (Claude Code or any compatible agent) that follows a structured template (numbered framework sections, application tables, usage patterns, ethical boundaries, references/ deep-dives).
  Grounds every claim in verifiable sources — cites pages, URLs, or quotes; web-searches when the source isn't in front of the agent; drops anything that can't be cited.
  Uses a saved multi-agent workflow for parallel extraction, reference expansion, and targeted review when authorized, with a portable direct-Agent fallback.
  Use when the user wants to turn a book / method / framework / paper / talk / course into a skill, or says "distill this", "make a skill from this book", "turn X into a skill", "book to skill", "source to skill".
---

# distill-to-skill — Source to Skill

Transforms a source into a strict skill shape: trigger-rich frontmatter, core principle, numbered framework sections, process, common-mistakes table, quick diagnostic, and `references/` deep-dives.

**Hard rule: every framework, insight, example, and copy pattern must trace to a real source.** No model-memory restatements. If a claim cannot be cited, drop it. See [citation-rules.md](references/citation-rules.md).

**Output cap: the produced SKILL.md must stay ≤100 lines.** Keep one-line section indexes there; put full sections in `references/<section-slug>.md`. See [template.md](references/template.md).

## Quickstart

User: *"Distill The Mom Test into a skill."*
Agent: confirms source → runs the description interview → stages files → builds `sources.md` → orchestrates 3 extraction workers → synthesizes SKILL.md in the main thread → orchestrates one writer/verifier pipeline per reference → reviews and surgically revises → emits the result.

## Orchestration rule

For Phases 3, 5, and 6, use `${CLAUDE_SKILL_DIR}/workflows/distill.js` when the Workflow tool exists **and the user has authorized workflow/multi-agent orchestration**. Pass absolute `skillDir` and `stagingDir` paths. If Workflow is unavailable or not authorized, use the direct Agent fallback in the referenced phase instructions. Both paths must create the same artifacts and pass the same gates.

Workflow call shape:

```text
Workflow({
  scriptPath: "${CLAUDE_SKILL_DIR}/workflows/distill.js",
  args: { stage: "extract|expand|review", skillDir, stagingDir, ...stageInputs }
})
```

## Phases

1. **Intake** — detect input type, pick mode + output location, run the [description interview](references/description-interview.md).
   → **Done when:** `description-brief.md` exists. Phase 2 cannot start without it.
2. **Ingest** — build `sources.md` (prefer primary sources; WebSearch only to fill gaps). See [phases.md](references/phases.md#phase-2-source-ingestion).
   → **Done when:** `sources.md` lists ≥1 primary source with citation pointers.
3. **Extract** — invoke workflow stage `extract` with `sourceScope` and `estimatedSourceTokens`; fallback: launch Structure / Application / Guardrails Agents together. See [extraction-jobs.md](references/extraction-jobs.md).
   → **Done when:** `notes-structure.md`, `notes-application.md`, and `notes-guardrails.md` exist, each ≤10k tokens with citations.
4. **Synthesize** — assemble SKILL.md in the main thread from extraction notes only. Match the author's order and count. See [template.md](references/template.md).
   → **Done when:** SKILL.md exists and is ≤100 lines.
5. **Expand** — ensure `references/` exists, then invoke workflow stage `expand` with `sections: [{name, slug}]`; fallback: one Agent per section plus case studies and checklist. See [phases.md](references/phases.md#phase-5-references-fan-out).
   → **Done when:** every section link resolves, plus `case-studies.md` and `checklist.md` exist.
6. **Review** — invoke workflow stage `review` with optional `maxRevisionRounds`; fallback: self-score and launch targeted revision Agents. See [review-rubric.md](references/review-rubric.md).
   → **Done when:** no rubric category scores below target.
7. **Emit** — move staging to the chosen install location; print slug, path, sources, section count, and rubric score.
   → **Done when:** install path is printed and confirmed.

**Recovery:** if a gate fails, fix that artifact and re-run from that phase. Do not skip forward.

**Mechanical check:** run `${CLAUDE_SKILL_DIR}/scripts/check.sh <staging-dir>` after each phase, or add `--phase N`. Phase 6 scoring still requires agent judgment.

## Defaults

- **Mode:** `strict`; use `liberal` only on request.
- **Staging:** `./skills-draft/<slug>/`; never write directly into live skill directories.
- **Description:** never auto-generate it; always run the interview first.
- **Synthesis:** never delegate final SKILL.md coherence to a worker.

## Anti-patterns

- Filling source gaps from training data
- Running one monolithic extraction pass
- Auto-generating the description
- Inventing numeric values or application contexts
- Forcing a fixed framework count
- Putting full framework sections inside SKILL.md

## Reference index

- [intake.md](references/intake.md) — input types, modes, output locations
- [phases.md](references/phases.md) — phase detail, workflow inputs, fallbacks, gates
- [extraction-jobs.md](references/extraction-jobs.md) — canonical extraction worker specifications
- [template.md](references/template.md) — exact produced SKILL.md shape
- [citation-rules.md](references/citation-rules.md) — citation requirements
- [description-interview.md](references/description-interview.md) — frontmatter interview
- [review-rubric.md](references/review-rubric.md) — scoring and revision protocol
- [anti-patterns.md](references/anti-patterns.md) — full anti-pattern table
- [distill.js](workflows/distill.js) — Claude Code multi-agent orchestration; direct-Agent fallback remains portable
