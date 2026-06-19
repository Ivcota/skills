---
name: validate-icp
description: Mines public communities (Reddit, HN, X, IndieHackers, Trustpilot, Discord, forums) for verbatim first-person pain quotes to validate whether an ICP exists publicly before the user commits to customer interviews. Spawns parallel agents across named sources and returns raw quotes (source-linked, categorized by JTBD dimensions and Forces of Progress), a named DM list for interviews, a reachability scorecard, and a VALIDATED / WEAK / NOT FOUND verdict. Use when the user has an ICP hypothesis and needs voice-of-customer evidence before interviews, or when asked to validate an ICP, prove a customer segment exists, find verbatim pain quotes, or check whether a target market is reachable publicly. Typically runs after `jobs-to-be-done` (produces the ICP hypothesis) and before `mom-test` (needs interview targets and verbatim language to avoid leading questions).
---

# Validate ICP

Prove an ICP hypothesis exists publicly — in their own words — before asking the user to invest in interviews.

## Goal

**VALIDATED verdict backed by 25+ verbatim quotes, 10+ named individuals to DM, and a reachability scorecard.**

WEAK or NOT FOUND verdicts are equally valid outputs. A NOT FOUND result backed by evidence saves the user weeks of interview work and routes them to pivot ICP or run cold outreach instead.

## Workflow

### Phase 1 — Lock the ICP hypothesis

Confirm three elements before searching. If any are vague, tighten with the user first.

- [ ] **Who** — role/profile, not demographics (e.g. "indie SaaS founder who shipped on Lovable" not "startup founder")
- [ ] **Circumstance** — when the job arises (e.g. "already shipped, between weeks 1–90")
- [ ] **Hypothesized pain** — what they're struggling with (gives the search its verbs)

### Phase 2 — Map the search surface

Default surfaces — skip any the ICP doesn't live on:

- **Reddit** — named subs (r/SideProject, r/SaaS, r/indiehackers, r/Entrepreneur, or vertical-specific)
- **Hacker News** — Algolia search (hn.algolia.com) + known thread IDs
- **X / Twitter** — named accounts + quote-tree mining of canonical incidents
- **IndieHackers** — post + comment search
- **Trustpilot / G2 / Capterra** — if ICP uses specific tools with reviews (filter 1–3 star)
- **LinkedIn** — public posts + Pulse long-form (Google Site Search only)
- **Discord / Slack** — only publicly indexed transcripts
- **Facebook Groups** — only public groups via Google Site Search
- **Niche forums** — domain-specific (BiggerPockets, PracticalMachinist, etc.)

### Phase 3 — Spawn parallel agents (one per surface)

Use the **agent brief template** in [REFERENCE.md](REFERENCE.md#agent-brief-template). Every brief MUST:

- Front-load 300–400 words of ICP context (agents start cold)
- Name specific search targets (subreddits, usernames, thread IDs, product URLs)
- Specify output format (raw quotes, source-linked, categorized by 6 buckets)
- Include the anti-instruction: **"Do not synthesize or paraphrase. Return verbatim quotes."**

**Fetch strategy — tracer bullet + fail fast.** Most high-value surfaces (Reddit, X, G2, Capterra, LinkedIn) block direct agent fetches. Every agent brief MUST include the fetch protocol from [REFERENCE.md](REFERENCE.md#fetch-strategy--tracer-bullet--fail-fast):

1. Before the sweep, run **one tracer-bullet fetch** against a known-good URL on the surface using the top of that surface's loophole ladder.
2. If it works, **commit** to that method. If it fails, drop one rung and retry the same tracer URL.
3. Descend until one rung works, or until the full ladder fails on the tracer — then **abort the surface** and report `BLOCKED`. Never fabricate. Never burn more than ~3 attempts on a blocked URL.
4. Mid-sweep, after 2 consecutive failures on the committed method, re-run the tracer from the top.

Per-surface loophole ladders (Reddit, X, G2/Capterra, LinkedIn, Discord, Facebook) live in [REFERENCE.md](REFERENCE.md#community-specific-search-tactics).

Run agents in parallel — surfaces are independent.

### Phase 4 — Synthesize into verdict

Consolidate outputs into the **report template** in [REFERENCE.md](REFERENCE.md#output-report-template). Score on four axes (0–3 each, full rubric in REFERENCE):

- **Pain visibility** — how loudly they talk about the pain publicly
- **Reachability** — which channels yield named individuals at scale
- **Purchasing power signals** — evidence of budget (MRR mentions, tool spend, titles)
- **Population size** — rough count of distinct voices found

Render verdict: **VALIDATED** (≥9, no axis at 0), **WEAK** (5–8 or any 0), **NOT FOUND** (≤4).

## When to stop and pivot

If the full sweep yields fewer than 10 distinct verbatim quotes, the ICP may only exist privately (common for enterprise buyers, regulated industries, shy verticals). Report NOT FOUND and route to:

- **Cold outreach** — ICP is targetable but not vocal
- **Pivot ICP** — hypothesis is wrong; re-tighten and rerun
- **Proxy interview** — ICP is gated; interview an adjacent role

## Ethical boundaries

- **Never fabricate quotes.** No source URL = no inclusion.
- **Always link the source.** Include date where visible.
- **Don't contact anyone.** Produce the DM list — the user decides who to reach.
- **Respect platform norms.** Public commentary is fair to quote; paid/gated community content is not.

## Composition with other skills

- Runs **after** `jobs-to-be-done` (consumes the ICP hypothesis)
- Runs **before** `mom-test` (produces interview targets + non-leading language)
- Feeds `hundred-million-offers`, `storybrand-messaging`, `obviously-awesome` (verbatim pain becomes copy)

## Advanced

See [REFERENCE.md](REFERENCE.md) for:
- Full agent brief template (copyable)
- Community-by-community search tactics
- Scoring rubric
- Output report template
- Strong-vs-weak signal classification

See [EXAMPLES.md](EXAMPLES.md) for a worked example.
