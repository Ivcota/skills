# Extraction jobs

These are the canonical prompts and output schemas for both orchestration paths: the saved `workflows/distill.js` Workflow and the portable direct-Agent fallback. The Workflow launches all three with `parallel()`; the fallback launches them as Agent calls in one message. Each worker is sized to complete in **≤150k tokens of context**: source slice + system prompt + working notes + output. Author info and trigger phrases stay with the single synthesis owner.

## Token budget per agent

| Component | Budget |
|---|---|
| System prompt + tools | ~5k |
| Source material loaded | ≤100k |
| Working notes / tool calls | ~25k |
| Returned notes (capped) | ≤10k |
| **Total ceiling** | **~140k** |

## Source-size gate

Before spawning, check the source token count (rough: words × 1.3).

- **Source ≤100k tokens** — each agent loads the full source.
- **Source >100k tokens** — each agent loads a **scoped slice**. The calling session builds a chapter map from the TOC before invoking the Workflow and assigns chapter ranges per job (see "Slicing rules" below). Agents are forbidden from reading outside their scope.

## Universal boilerplate

Every job prompt ends with:

> Source manifest: `{staging}/sources.md`. Your scope: {chapters or "full source"}. Do not read outside scope. WebSearch is permitted only to verify a specific citation your scoped reading produced — cap at 3 web reads. If a claim cannot be sourced, omit it; do not invent. Return notes ≤10k tokens in the format below. Every item carries a citation (source + page/URL + quote).

## Job 1 — Structure (the spine)

Covers core principle, framework sections, and end-to-end process. One agent owns the book's skeleton so synthesis has a single coherent backbone.

> Extract:
>
> 1. **Thesis** — the one-sentence foundational claim the framework rests on. Plus any scoring model the author uses (e.g., "rate 0–10").
> 2. **Framework sections** — the numbered models / levers / pillars / stages the author presents as the main framework. Do not force a count. For each: name, one-sentence concept, 2-sentence mechanism (why it works), 4–8 key insights with citations.
> 3. **Process** — the end-to-end numbered steps to apply the whole framework. Prefer the author's own sequence; if implicit, derive from framework order and tag each step with its source section.
>
> Slicing rules (only if source >100k): read intro, conclusion, and the first + last 15% of each part / framework chapter. Skip case-study chapters (Job 2 owns those) and warnings/ethics chapters (Job 3 owns those).
>
> Return:
> ```
> thesis: "<sentence>"
> thesis_citation: {...}
> scoring_model: <description or "none">
> scoring_citation: {...}
> frameworks:
>   - name: "<author's term>"
>     concept: "<one sentence>"
>     mechanism: "<2 sentences>"
>     order_in_source: <n>
>     insights:
>       - text: "<insight>"
>         citation: {...}
> process:
>   - step: <n>
>     action: "<imperative verb + object>"
>     source_section: "<framework name>"
>     citation: {...}
> ```

## Job 2 — Application (the how-to-use)

Covers copy patterns and case studies. One agent owns everything that turns the framework into reusable artifacts.

> Extract:
>
> 1. **Copy patterns** — sentence templates and phrases the author uses verbatim or near-verbatim, grouped by framework section. Generalize placeholders (`[Avatar]`, `[Outcome]`) but keep the structure. Each pattern carries the exact source phrase it derives from.
> 2. **Case studies & applications** — every example and worked application, grouped by context (SaaS / Coaching / E-commerce / Agency / B2B / etc. — only contexts the source actually covers). Do not invent contexts.
>
> Slicing rules (only if source >100k): read example-heavy chapters (use TOC keywords: "examples", "case studies", "in practice", named-customer chapters). Skip pure-theory and pure-warning chapters.
>
> Jobs run in parallel, so group by your best read of the author's structure. The single synthesis owner will reconcile names and ordering using Job 1 as canonical.
>
> Return:
> ```
> copy_patterns:
>   - section: "<framework name>"
>     template: "<pattern>"
>     source_phrase: "<exact quote>"
>     citation: {...}
> cases:
>   - context: "<e.g., Coaching>"
>     application: "<what the author did or recommends>"
>     example: "<specific quoted example>"
>     related_section: "<framework name>"
>     citation: {...}
> ```

## Job 3 — Guardrails (the what-not-to-do)

Covers common mistakes and ethical boundaries. One agent owns negative space.

> Extract:
>
> 1. **Common mistakes** — every failure mode, anti-pattern, or warning the author calls out. For each: the mistake, why it fails (author's reasoning), the fix.
> 2. **Ethical boundaries** — explicit guardrails: what the author says you should NOT do, what crosses a line, what damages trust. Tag each to the framework section it belongs to. If the source lacks explicit ethics, return `boundaries: []` — do not synthesize generic ethics.
>
> Slicing rules (only if source >100k): read warning/objection/pitfall chapters and any ethics or "long-term" chapters. Skim framework chapters only for inline "don't do X" callouts.
>
> Return:
> ```
> mistakes:
>   - mistake: "<name>"
>     why_fails: "<author's reasoning>"
>     fix: "<author's prescription>"
>     citation: {...}
> boundaries:
>   - section: "<framework name>"
>     rule: "<the guardrail>"
>     reasoning: "<author's why>"
>     citation: {...}
> ```

## Ingestion and synthesis-owner tasks

The calling session completes author-source ingestion before the Workflow starts; the one synthesis owner then turns those grounded inputs into final copy.

- **Author + further reading ingestion** — add the author's publisher/personal page to `sources.md`; record the bio evidence, other books, and verified ISBNs/URLs there.
- **Author + further reading synthesis** — use only those manifest entries for the 2–3 sentence bio and reading list; omit unsupported details.
- **Triggers** — derive 8–15 trigger phrases from the description-interview answers + Job 1's framework names. Group into (a) direct names, (b) problem phrases, (c) artifact phrases.

## Forbidden patterns

Each agent prompt explicitly bans:

- Reading outside its assigned scope ("for context")
- WebSearch beyond the 3-call cap
- Returning prose >10k tokens
- Filling gaps from training data when source is silent
- Inventing numeric values ($X, Y%, Nx) the source doesn't state
- Padding application tables with industries the source never covers

## Failure modes to watch

- An agent returns long prose with no citations — reject, re-run with stricter prompt
- An agent's output exceeds 10k tokens — request a compression pass, do not synthesize bloated notes
- Job 1 and Job 2 disagree on framework section names — the synthesis owner reconciles using Job 1 as canonical
- Source >100k but agent ignored slicing — its context will spike; abort and re-spawn with explicit chapter list
