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

Fan out **3 sub-agents** using the Agent tool, launched in a **single message with multiple tool calls**. Each is sized to stay under 150k tokens of context. See [extraction-jobs.md](references/extraction-jobs.md) for full prompts and token budgets.

Job set:
1. **Structure** — thesis + framework sections + end-to-end process (the spine)
2. **Application** — copy patterns + case studies (the how-to-use)
3. **Guardrails** — common mistakes + ethical boundaries (the what-not-to-do)

Author bio, further reading, and trigger phrases are handled in the main thread (small WebFetch + reasoning over Job 1 output) — not delegated.

**Source-size gate:** before spawning, estimate the source's token count.
- ≤100k tokens → each agent loads the full source.
- \>100k tokens → main thread builds a chapter map from the TOC and assigns chapter ranges per agent. Agents are forbidden from reading outside scope.

Each agent is also instructed: read only your scope, cap WebSearch at 3 calls, return ≤10k tokens of structured notes, no inventions when the source is silent.

**Exit gate:** all three agents returned notes with ≥1 citation per item, each under the 10k-token cap.

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
