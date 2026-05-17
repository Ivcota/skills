# Phase details

Full prose for each phase. SKILL.md keeps the one-line summary; this file holds the gates, sub-agent fan-out rules, and source-size logic.

## Phase 2: Source ingestion

Build a source manifest before any extraction. For each available source, record: `{type, location, access_method, coverage_estimate}`.

- Files: read the full text, chunk if needed, keep page/section pointers
- URLs: WebFetch; record URL + retrieval date
- Title-only: WebSearch for — author page, publisher page, structured summaries (Blinkist, Shortform, Farnam Street, Derek Sivers' notes), interviews with author, official talks / YouTube transcripts, reviews that quote heavily. Prefer primary over secondary.

**Exit gate:** manifest committed to `./skills-draft/<slug>/sources.md` with at least one primary source and links for gap-filling.

## Phase 3: Parallel extraction

Fan out **3 sub-agents** using the Agent tool, launched in a **single message with multiple tool calls**. Each is sized to stay under 150k tokens of context. See [extraction-jobs.md](extraction-jobs.md) for full prompts and token budgets.

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

Assemble SKILL.md in the main thread using [template.md](template.md) as the exact shape. Do not delegate synthesis — the main thread owns coherence across sections. Pull content from extraction notes only; if a section has thin material, flag it and either (a) spawn a targeted follow-up sub-agent, or (b) drop the section.

Ordering check: framework sections should follow the author's own sequence, not your preferred order.

## Phase 5: References fan-out

For each framework section in SKILL.md, spawn one sub-agent to draft `references/<section-slug>.md`. The sub-agent gets: the section's notes, the source manifest, permission to WebSearch for deeper citations. Target ~100-300 lines per reference file. Also generate `references/case-studies.md` and `references/checklist.md`.

**Exit gate:** every section linked from SKILL.md has a matching reference file.

## Phase 6: Review

Self-score against [review-rubric.md](review-rubric.md). Any category scoring <8/10 triggers a revision pass on that section. Minimum bar to ship:

- [ ] Description includes "Use when..." with specific trigger phrases
- [ ] SKILL.md ≤ 100 lines (push framework section detail into `references/<section>.md`)
- [ ] Every framework section has Core concept + Why it works + Key insights + Application table + Copy patterns + Ethical boundary + reference link in its reference file
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
