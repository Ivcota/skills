---
name: distill-to-skill
description: |
  Distill a book, method, or framework into an agent skill (Claude Code or any compatible agent) that follows a structured template (numbered framework sections, application tables, usage patterns, ethical boundaries, references/ deep-dives).
  Grounds every claim in verifiable sources — cites pages, URLs, or quotes; web-searches when the source isn't in front of the agent; drops anything that can't be cited.
  Fans out parallel sub-agents for extraction, then synthesizes against a strict template.
  Use when the user wants to turn a book / method / framework / paper / talk / course into a skill, or says "distill this", "make a skill from this book", "turn X into a skill", "book to skill", "source to skill".
---

# distill-to-skill — Source to Skill

Transforms a source (book, paper, method, talk, course, URL) into a skill that follows a strict template: trigger-rich frontmatter, core principle, numbered framework sections, process, common-mistakes table, quick-diagnostic table, and `references/` deep-dives.

**Hard rule: every framework, insight, example, and copy pattern must trace back to a real source.** No model-memory restatements. If a claim can't be cited, it's dropped. See [citation-rules.md](references/citation-rules.md).

**Output cap: the produced SKILL.md must stay ≤ 100 lines.** Each framework section is a one-line index entry in SKILL.md; the full section (Core concept, Why it works, Insights, Application table, Copy patterns, Ethical boundary) lives in `references/<section-slug>.md`. See [template.md](references/template.md).

## Quickstart

User: *"Distill The Mom Test into a skill."*
Agent: confirms source → asks 3 description-interview questions → creates `./skills-draft/mom-test/` → builds `sources.md` → fans out 3 extraction sub-agents → assembles ≤100-line SKILL.md → one sub-agent per section into `references/` → scores rubric → prints summary and offers to move to `~/.claude/skills/mom-test/`.

## Phases

1. **Intake** — detect input type, pick mode + output location, run the description interview. See [intake.md](references/intake.md).
   → **Done when:** `./skills-draft/<slug>/description-brief.md` exists on disk. (Mechanical gate — Phase 2 cannot start without it. This kills the "auto-generate description" capture error.)
2. **Ingest** — build `sources.md` manifest (prefer primary sources; WebSearch only to fill gaps). See [phases.md](references/phases.md#phase-2-source-ingestion).
   → **Done when:** `sources.md` lists ≥1 primary source with citation pointers.
3. **Extract** — fan out 3 parallel sub-agents (Structure / Application / Guardrails) in a single message. Source-size gate decides full-load vs chapter-map. See [extraction-jobs.md](references/extraction-jobs.md) and [phases.md](references/phases.md#phase-3-parallel-extraction).
   → **Done when:** 3 notes files exist, each ≤10k tokens, each item carries ≥1 citation.
4. **Synthesize** — assemble SKILL.md in the main thread from extraction notes only. Match the author's own section order and count. See [template.md](references/template.md).
   → **Done when:** SKILL.md exists and is ≤100 lines. If over, push section detail into `references/` and re-check.
5. **Expand** — one sub-agent per framework section drafts `references/<section-slug>.md` (~100–300 lines each), plus `case-studies.md` and `checklist.md`. See [phases.md](references/phases.md#phase-5-references-fan-out).
   → **Done when:** every section link in SKILL.md resolves to a real file.
6. **Review** — self-score against [review-rubric.md](references/review-rubric.md). Anything <8/10 triggers a revision pass on that section.
   → **Done when:** no rubric category scores <8/10.
7. **Emit** — move staging dir to chosen install location; print slug, path, sources used, section count, rubric score.
   → **Done when:** install path printed and user has confirmed location.

**Recovery:** if any gate fails, fix the named artifact and re-run from that phase. Do not skip forward.

**Mechanical check:** run `./scripts/check.sh <staging-dir>` after each phase (or `--phase N` for a single phase). It validates the file-on-disk gates (description-brief, sources.md, extraction notes ≤10k tokens, SKILL.md ≤100 lines, all `references/*.md` links resolve) and exits non-zero on failure. Phase 6 rubric scoring still needs agent judgment.

## Defaults

- **Mode:** `strict` (paraphrase closely, drop un-citable content). `liberal` only on request.
- **Staging:** `./skills-draft/<slug>/` until Phase 7. Never write directly into live skill dirs.
- **Description:** never auto-generated — always run the [description interview](references/description-interview.md) first.

## Anti-patterns

The big six (full table in [anti-patterns.md](references/anti-patterns.md)):

- Letting the model fill gaps from training data → no citation, no content
- Single monolithic extraction pass → separate extract → synthesize phases
- Auto-generating the description → always run the description interview
- Inventing numeric values in tables → only what the source states
- Forcing a fixed section count → match the source's actual structure
- **Putting full framework sections inside SKILL.md** → one-line index in SKILL.md, full section in `references/<slug>.md` (keeps SKILL.md ≤ 100 lines)

## Reference index

- [intake.md](references/intake.md) — Phase 1 detail (input types, modes, output locations)
- [phases.md](references/phases.md) — Phases 2–7 detail with exit gates
- [extraction-jobs.md](references/extraction-jobs.md) — Sub-agent prompts and token budgets
- [template.md](references/template.md) — Exact output shape for produced SKILL.md
- [citation-rules.md](references/citation-rules.md) — What counts as a citation, what gets dropped
- [description-interview.md](references/description-interview.md) — Questions that drive the frontmatter
- [review-rubric.md](references/review-rubric.md) — Scoring rubric for Phase 6
- [anti-patterns.md](references/anti-patterns.md) — Full anti-pattern table
