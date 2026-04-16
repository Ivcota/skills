# Extraction jobs

Each job is a self-contained prompt for a sub-agent spawned via the Agent tool. Launch them **in parallel** — a single message with multiple Agent tool calls. Each returns structured notes with citations per [citation-rules.md](citation-rules.md).

Every job prompt ends with the same boilerplate:

> You have access to the source manifest at `{staging}/sources.md`. You may WebSearch and WebFetch to fill gaps. If a claim cannot be sourced, omit it — do not invent. Return notes in the format shown below. Every item must carry a citation (source + page/URL + quote).

## Job 1 — Core principle

> Read the source and identify the **one-sentence thesis** — the foundational claim the entire framework rests on. Also identify any **scoring model** the author uses (e.g., "rate offers 0–10", "grade leads A/B/C").
>
> Return:
> ```
> thesis: "<one sentence>"
> thesis_citation: {...}
> scoring_model: <description or "none">
> scoring_citation: {...}
> ```

## Job 2 — Framework sections

> Identify the **numbered models, levers, pillars, or stages** the author presents as the main framework. Do not force a count — if the author has 4, return 4. For each, extract: name, one-sentence concept, mechanism (why it works), 4–8 key insights (each with citation).
>
> Return an array of:
> ```
> - name: "<author's term>"
>   concept: "<one sentence>"
>   mechanism: "<why it works, 2 sentences>"
>   insights:
>     - text: "<insight>"
>       citation: {...}
>   order_in_source: <n>
> ```

## Job 3 — Copy patterns

> For each framework section (from Job 2), extract **sentence templates and phrases the author uses verbatim or near-verbatim**. Generalize placeholders (`[Avatar]`, `[Outcome]`, `[Time Frame]`) but keep the structure.
>
> Return per section:
> ```
> section: "<name>"
> patterns:
>   - template: "<pattern>"
>     source_phrase: "<exact quote the pattern comes from>"
>     citation: {...}
> ```

## Job 4 — Case studies & applications

> Extract every example, case study, and worked application the author presents. Group by context (SaaS / Coaching / E-commerce / Agency / Info product / Local / B2B / Consumer — whatever the source covers). **Do not invent context rows the source doesn't cover.**
>
> Return:
> ```
> cases:
>   - context: "<e.g., Coaching>"
>     application: "<what the author did or recommends>"
>     example: "<specific quoted example>"
>     related_section: "<framework section name>"
>     citation: {...}
> ```

## Job 5 — Common mistakes & anti-patterns

> Extract every failure mode, mistake, anti-pattern, or warning the author calls out. For each: the mistake, why it fails (in the author's words), the fix.
>
> Return:
> ```
> mistakes:
>   - mistake: "<name>"
>     why_fails: "<author's reasoning>"
>     fix: "<author's prescription>"
>     citation: {...}
> ```

## Job 6 — Ethical boundaries

> Extract the author's **explicit ethical guardrails** — what they say you should NOT do, what crosses a line, what damages trust. Tag each to the framework section it belongs to.
>
> Return:
> ```
> boundaries:
>   - section: "<framework section name>"
>     rule: "<the guardrail>"
>     reasoning: "<author's why>"
>     citation: {...}
> ```
>
> If the source lacks explicit ethical guardrails, return `boundaries: []` — do not synthesize generic ethics.

## Job 7 — Author + further reading

> From the author's own pages (publisher, personal site, book jacket) gather: 2–3 sentence bio, other books they've written, official links. Verify ISBNs and Amazon URLs by WebFetch.
>
> Return:
> ```
> author:
>   name: "<name>"
>   bio: "<2-3 sentences, grounded>"
>   bio_citation: {...}
> further_reading:
>   - title: "<title>"
>     url: "<verified URL>"
>     note: "<one line>"
> ```

## Job 8 — Process

> Extract or derive the **end-to-end numbered process** for applying the whole framework. Prefer the author's own sequence. If the author doesn't present an explicit sequence, synthesize one from the framework order — and mark each step with the section it came from.
>
> Return:
> ```
> process:
>   - step: <n>
>     action: "<imperative verb + object>"
>     source_section: "<framework section>"
>     citation: {...}
> ```

## Job 9 — Triggers

> Propose 8–15 **trigger phrases** a user would naturally say that should invoke this skill. Group into: (a) direct names for the framework, (b) problem phrases the framework addresses, (c) artifact phrases (e.g., "landing page copy", "onboarding flow"). Ground (a) and (c) in the source; (b) may be inferred from the audience/problem the author describes.
>
> Return:
> ```
> triggers:
>   direct: [...]
>   problem: [...]
>   artifact: [...]
> ```

## Failure modes to watch

- A sub-agent returns long, well-written prose with no citations — reject and re-run with stricter prompt
- A sub-agent pads the application table with generic industries not in the source — trim before synthesis
- A sub-agent invents numeric values ("$500 value", "3x conversions") not in the source — strip
- Two sub-agents duplicate insights — dedupe in synthesis
