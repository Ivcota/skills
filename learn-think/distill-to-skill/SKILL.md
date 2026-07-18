---
name: distill-to-skill
description: |
  Distill a book, method, or framework into an agent skill (Claude Code or any compatible agent) that follows a structured template (numbered framework sections, application tables, usage patterns, ethical boundaries, references/ deep-dives).
  Grounds every claim in verifiable sources — cites pages, URLs, or quotes; web-searches when the source isn't in front of the agent; drops anything that can't be cited.
  Uses one saved multi-agent workflow for extraction, coherent synthesis, reference expansion, and targeted review when authorized, with a portable direct-Agent fallback.
  Use when the user wants to turn a book / method / framework / paper / talk / course into a skill, or says "distill this", "make a skill from this book", "turn X into a skill", "book to skill", "source to skill".
---

# distill-to-skill — Source to Skill

Transforms a source into a strict skill shape: trigger-rich frontmatter, core principle, numbered framework sections, process, common-mistakes table, quick diagnostic, and `references/` deep-dives.

**Hard rule: every framework, insight, example, and copy pattern must trace to a real source.** No model-memory restatements. If a claim cannot be cited, drop it. See [citation-rules.md](references/citation-rules.md).

**Output cap: the produced SKILL.md must stay ≤100 lines.** Keep one-line section indexes there; put full sections in `references/<section-slug>.md`. See [template.md](references/template.md).

## Quickstart

User: *"Distill The Mom Test into a skill."*
Agent: confirms source → runs the description interview → stages files → builds `sources.md` → invokes one saved Workflow for Extract → Synthesize → Expand → Review/Revise → checks the result → emits it.

## Orchestration rule

Complete interactive Intake and Ingest first. Once `description-brief.md` and `sources.md` pass their gates, invoke `${CLAUDE_SKILL_DIR}/workflows/distill.js` **once** when the Workflow tool exists and the user authorized workflow/multi-agent orchestration. The Workflow owns Phases 3–6 and returns `ready`, `blocked`, or `needs-revision`. Do not create separate Workflow runs for individual phases.

```text
Workflow({
  scriptPath: "${CLAUDE_SKILL_DIR}/workflows/distill.js",
  args: {
    skillDir: "<absolute active skill directory>",
    stagingDir: "<absolute staging directory>",
    estimatedSourceTokens: <number or omit>,
    sourceScope: "full source"
      OR { structure: "...", application: "...", guardrails: "..." },
    maxRevisionRounds: 3
  }
})
```

If Workflow is unavailable or not authorized, follow the direct-Agent fallback in [phases.md](references/phases.md). Both paths must create the same artifacts and pass the same gates.

## Phases

1. **Intake** — detect input type, pick mode + output location, run the [description interview](references/description-interview.md).
   → **Done when:** `description-brief.md` exists. Phase 2 cannot start without it.
2. **Ingest** — build `sources.md` (prefer primary sources; include an author/publisher source for bio claims). See [phases.md](references/phases.md#phase-2-source-ingestion).
   → **Done when:** `sources.md` lists ≥1 primary framework source plus grounded author information with citation pointers.
3. **Extract** — the Workflow launches Structure / Application / Guardrails workers together with disjoint output files and explicit source scopes.
   → **Done when:** all three notes files exist, each ≤10k tokens with citations; any missing or blocked result stops the run.
4. **Synthesize** — one Workflow synthesis Agent owns the complete SKILL.md and canonical ordered section list. In the fallback path, the main session owns this step. See [template.md](references/template.md).
   → **Done when:** SKILL.md exists, is ≤100 lines, and yields unique non-reserved section slugs.
5. **Expand** — the Workflow derives reference paths from synthesis, then pipelines each section plus case studies and checklist through draft → verify.
   → **Done when:** every section link resolves, plus `case-studies.md` and `checklist.md` exist; a missing draft never reaches verification.
6. **Review + Validate** — the same Workflow scores canonical rubric categories, applies non-overlapping surgical revisions, re-scores, then runs the mechanical artifact gates before returning `ready`.
   → **Done when:** status is `ready`; `blocked` reports the failed phase or gate, while `needs-revision` returns unresolved targets.
7. **Emit** — re-run the mechanical checker, then move staging to the confirmed install location; print slug, path, sources, section count, references, and rubric score.
   → **Done when:** install path is printed and confirmed.

**Recovery:** fix the reported blocker or unresolved target, preserve valid staged artifacts, and re-invoke the single end-to-end Workflow. Never switch back to stage-specific Workflow calls.

**Mechanical check:** run `${CLAUDE_SKILL_DIR}/scripts/check.sh <staging-dir>` after the Workflow returns and before emission. Phase 6 scoring still requires agent judgment.

## Defaults

- **Mode:** `strict`; use `liberal` only on request.
- **Staging:** `./skills-draft/<slug>/`; never write directly into live skill directories.
- **Description:** never auto-generate it; always run the interview first.
- **Synthesis:** one coherence owner only — the Workflow's dedicated synthesis Agent, or the main session in fallback mode.

## Anti-patterns

- Filling source gaps from training data
- Starting a Workflow before Intake and Ingest pass
- Creating separate Workflow runs for Extract, Expand, and Review
- Running one monolithic extraction worker
- Auto-generating the description
- Inventing numeric values or application contexts
- Forcing a fixed framework count
- Putting full framework sections inside SKILL.md

## Reference index

- [intake.md](references/intake.md) — input types, modes, output locations
- [phases.md](references/phases.md) — phase detail, workflow contract, fallbacks, gates
- [extraction-jobs.md](references/extraction-jobs.md) — canonical extraction worker specifications
- [template.md](references/template.md) — exact produced SKILL.md shape
- [citation-rules.md](references/citation-rules.md) — citation requirements
- [description-interview.md](references/description-interview.md) — frontmatter interview
- [review-rubric.md](references/review-rubric.md) — scoring and revision protocol
- [anti-patterns.md](references/anti-patterns.md) — full anti-pattern table
- [distill.js](workflows/distill.js) — one-run Claude Code multi-agent orchestration
