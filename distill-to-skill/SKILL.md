---
name: distill-to-skill
description: |
  Distill a book, method, or framework into an agent skill (Claude Code or any compatible agent) that follows a structured template (numbered framework sections, application tables, usage patterns, ethical boundaries, references/ deep-dives).
  Grounds every claim in verifiable sources — cites pages, URLs, or quotes; web-searches when the source isn't in front of the agent; drops anything that can't be cited.
  Fans out parallel sub-agents for extraction, then synthesizes against a strict template.
  Use when the user wants to turn a book / method / framework / paper / talk / course into a skill, or says "distill this", "make a skill from this book", "turn X into a skill", "book to skill", "source to skill".
---

# distill-to-skill — Source to Skill

Transforms a source (book, paper, method, talk, course, URL) into a skill with this shape: frontmatter with trigger-rich description, core principle, numbered framework sections (each with Core concept, Why it works, Key insights, Applications table, Usage patterns, Ethical boundary, reference link), numbered process, common-mistakes table, quick-diagnostic table, `references/` deep-dives.

**Hard rule: every framework, insight, example, and copy pattern must trace back to a real source.** No model-memory restatements. If a claim can't be cited, it's dropped. See [citation-rules.md](references/citation-rules.md).

References: [Output template](references/template.md) | [Extraction jobs](references/extraction-jobs.md) | [Citation rules](references/citation-rules.md) | [Description interview](references/description-interview.md) | [Review rubric](references/review-rubric.md)

## Input detection

Accepts one or more of:
- **File** — PDF, epub, markdown, txt (any path the Read tool can open; PDFs ≤20 pages per call, chunk longer books)
- **URL** — article, blog post, transcript, publisher page
- **Title + author** — triggers web research (WebSearch → WebFetch)
- **Pasted text** — inline method description

If only a title is given, confirm with the user before spending tokens on research: "I'll search for {title} by {author} — anything specific to prioritize (chapters, concepts)?"

## Modes

- **strict** (default) — paraphrase closely; cite aggressively; drop un-citable content
- **liberal** — rewrite in template voice; still cite but allow synthesis (tables, copy patterns) inferred from quoted material

Ask the user which mode only if ambiguous.

## Output location

Detect which skill directories exist on the user's system and offer them as targets. Common locations:
- `~/.claude/skills/<slug>/` — Claude Code user-scoped skills
- `~/.agents/skills/<slug>/` — generic agent skills (any compatible harness)
- `./skills-draft/<slug>/` — local staging dir (review before installing)
- A project-local `.claude/skills/` or `.agents/skills/` if one exists in the cwd

Ask before writing: "Write to {detected-paths} or stage at `./skills-draft/<slug>/` first?" Slug = kebab-case of 3-5 significant words from the book/method title.

## Phase 1: Intake

1. Detect input type. If only title: propose a research plan and confirm.
2. Ask the 2–3 [description-interview](references/description-interview.md) questions — audience, trigger phrases, primary use case. These drive the frontmatter `description:` (the only thing future agents see).
3. Pick mode (strict / liberal). Pick output location.
4. Derive slug. Create staging dir.

**Exit gate:** slug chosen, mode chosen, output location chosen, description brief written.

## Phase 2: Source ingestion

Build a source manifest before any extraction. For each available source, record: `{type, location, access_method, coverage_estimate}`.

- Files: read the full text, chunk if needed, keep page/section pointers
- URLs: WebFetch; record URL + retrieval date
- Title-only: WebSearch for — author page, publisher page, structured summaries (Blinkist, Shortform, Farnam Street, Derek Sivers' notes), interviews with author, official talks / YouTube transcripts, reviews that quote heavily. Prefer primary over secondary.

**Exit gate:** manifest committed to `./skills-draft/<slug>/sources.md` with at least one primary source and links for gap-filling.

## Phase 3: Parallel extraction

Fan out sub-agents using the Agent tool. Launch in a **single message with multiple tool calls** so they run concurrently. Each job returns structured notes with citations. See [extraction-jobs.md](references/extraction-jobs.md) for the exact prompts.

Default job set:
1. **Core-principle** — the one-sentence thesis + scoring model (if any)
2. **Frameworks** — the numbered models / levers / pillars (usually 6–10)
3. **Copy patterns** — phrases and sentence templates the author uses verbatim
4. **Case studies** — examples grouped by context (SaaS / Coaching / E-commerce / Agency / Info product — or whatever categories the source uses)
5. **Common mistakes** — failure modes, anti-patterns, what the author warns against
6. **Ethical boundaries** — caveats, honesty rules, things the author flags as off-limits
7. **Author + further reading** — bio, other books, canonical links
8. **Process** — numbered steps to apply the whole framework end-to-end
9. **Triggers** — phrases a user might say that should invoke this skill (feeds the `description:` field)

Each sub-agent is instructed: "If you can't find it in the source, WebSearch. If web can't confirm, omit. Return a citation for every item."

**Exit gate:** each job returned notes with ≥1 citation per item.

## Phase 4: Synthesis

Assemble SKILL.md in the main thread using [template.md](references/template.md) as the exact shape. Do not delegate synthesis — the main thread owns coherence across sections. Pull content from extraction notes only; if a section has thin material, flag it and either (a) spawn a targeted follow-up sub-agent, or (b) drop the section.

Ordering check: framework sections should follow the author's own sequence, not your preferred order.

## Phase 5: References fan-out

For each framework section in SKILL.md, spawn one sub-agent to draft `references/<section-slug>.md`. The sub-agent gets: the section's notes, the source manifest, permission to WebSearch for deeper citations. Target ~100-300 lines per reference file. Also generate `references/case-studies.md` and `references/checklist.md`.

**Exit gate:** every section linked from SKILL.md has a matching reference file.

## Phase 6: Review

Self-score against [review-rubric.md](references/review-rubric.md). Any category scoring <8/10 triggers a revision pass on that section. Minimum bar to ship:

- [ ] Description includes "Use when..." with specific trigger phrases
- [ ] Every framework section has Core concept + Why it works + Key insights + Application table + Copy patterns + Ethical boundary + reference link
- [ ] Every claim traces to a citation in `sources.md`
- [ ] No invented dollar values, statistics, or outcomes — only what the source states
- [ ] Product-application table has ≥5 rows with distinct contexts
- [ ] Common-mistakes table has ≥5 rows
- [ ] Further reading section cites the primary source (ISBN / URL)
- [ ] About-the-author section is grounded (no biographical invention)

## Phase 7: Emit

Move from staging to the chosen install location (e.g., `~/.claude/skills/<slug>/`, `~/.agents/skills/<slug>/`, or a project-local skills dir). Print:
- slug + path
- sources used
- section count + reference count
- rubric score

## Process summary

1. Intake → confirm source, mode, slug, location, description brief
2. Ingest → build `sources.md` manifest
3. Extract → fan out parallel sub-agents with citation rule
4. Synthesize → assemble SKILL.md from notes only
5. Expand → one sub-agent per reference file
6. Review → score, revise
7. Emit → move to final location

## Anti-patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| Letting the model fill gaps from training data | Produces plausible-but-ungrounded skills; erodes trust in the output | Hard rule: no citation, no content |
| Single monolithic extraction pass | Misses structure; synthesis and extraction fight each other | Separate extract → synthesize phases |
| Auto-generating the description without user input | Triggers are the single most important field; hardest to guess | Always run the description interview |
| Inventing numeric values in application tables | Faking values the source never stated is deceptive | Only include values the source states; otherwise leave qualitative |
| Forcing a fixed section count | Some sources have 4 pillars, others 8 — padding to a target invents content | Match the source's actual structure |
| Skipping the staging dir | Bad output pollutes the live skills dir and starts firing on triggers | Stage, review, then move |
