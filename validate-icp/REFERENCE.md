# validate-icp — Reference

## Agent brief template

Copy and adapt per surface. Agents start cold — front-load everything. Target ~400 words of setup before the question.

```
Context: [user's business one-liner, 1–2 sentences].

ICP hypothesis: [one sentence — who, circumstance, pain].

Specifically, this ICP tends to:
- [behavior 1 — what they do / what tools they use]
- [behavior 2 — where they hang out]
- [behavior 3 — what vocabulary they use]
- [behavior 4 — what incidents have happened to them publicly]

Your job: find VERBATIM QUOTES from this exact ICP in [timeframe, e.g. 2025–2026].
Raw words, not analyst paraphrases. We'll use these for landing-page copy and
to avoid leading questions in customer interviews.

Where to look:
- [Named subreddit 1]: search terms "[X]", "[Y]"
- [Named subreddit 2]: search terms "[X]"
- Hacker News: threads [ID], [ID], plus Algolia search "[keyword]"
- X / Twitter: [@handle], [@handle], plus search "[exact phrase]"
- [Other surface]: [specific target]

Fetch strategy — tracer bullet + fail fast:

Before sweeping the full target list, pick ONE known-good URL on this surface
and run a tracer-bullet test. Try the top-of-ladder method (see surface-specific
ladder below). If it returns readable content with the expected quote, COMMIT to
that method for the rest of the sweep. If it fails (403 / 429 / login wall /
empty body / Cloudflare challenge), drop to the next rung and retry the same
tracer URL. Descend until one rung works — that becomes the committed method.

Fail fast: after 2 consecutive failures mid-sweep, re-run the tracer from the
top of the ladder. If the full ladder fails on the tracer, ABORT this surface
and report `BLOCKED: tried [methods], none returned content`. Do not fabricate
or substitute quotes. Never burn more than ~3 attempts on a single blocked URL.
Report the winning method in your output.

Surface-specific loophole ladders (use in order):
- Reddit: (1) Google Site Search `site:reddit.com/r/<sub> "[phrase]"` →
  (2) follow result URLs to `old.reddit.com` (not `www.reddit.com`).
- X / Twitter: (1) `site:x.com "[phrase]"` via Google → (2)
  `syndication.twitter.com/srv/timeline-profile/screen-name/<handle>` JSON →
  (3) `nitter.net/<handle>` → (4) `threadreaderapp.com` → (5) `web.archive.org`.
- G2 / Capterra: (1) direct fetch (Trustpilot usually works) → (2)
  `site:g2.com "[product]"` / `site:capterra.com` via Google → (3)
  `web.archive.org` snapshot.
- LinkedIn: (1) `site:linkedin.com/posts "[phrase]"` via Google → (2)
  `site:linkedin.com/pulse` → (3) `web.archive.org`. Never fetch profiles direct.
- Discord: (1) `disboard.org` → (2) `site:reddit.com "discord screenshot"`.
- Facebook Groups: only `site:facebook.com/groups "[phrase]"` via Google.

Generic fallback when no ladder rung works: Google Site Search → archive.org →
cached syndication/RSS → give up and log `BLOCKED`.

Extract at minimum 20 quotes, categorized into:

**Functional pain** — what is literally broken
**Emotional pain** — how they feel
**Social pain** — reputation / identity
**Push forces** — the incident/frustration that would drive them to hire help
**Anxiety about solutions** — why they DON'T get help
**Habit** — what they do instead of getting help

For each quote: include source URL, date if visible, and one sentence
on who the person is (e.g. "indie SaaS founder, $2k MRR, built on Lovable").

Report format: markdown with the 6 categories as headers, quotes as
nested bullets with source links. Under [word budget] words.

Hard rule: do NOT synthesize, summarize, or paraphrase. Return verbatim quotes.
If a quote is clearly paraphrased by a third-party summary, mark it [paraphrase]
and include the summarizing source.

If you cannot find quotes in a category, say so explicitly — do NOT invent to fill.
```

## Community-specific search tactics

### Reddit
- **Default path: Google Site Search.** Reddit native search is flaky and direct fetches to `www.reddit.com` are frequently blocked or 429'd from agent runtimes. Use `site:reddit.com/r/<sub> "[phrase]"` (or `site:reddit.com "[phrase]"` across subs) as the primary discovery method, not a fallback.
- **Fetch target: `old.reddit.com`.** Once you have a thread URL, swap the host to `old.reddit.com` — lighter HTML, survives agent fetches better, and often returns when `www.reddit.com` 429s.
- Startup-generic: r/SideProject, r/SaaS, r/indiehackers, r/Entrepreneur, r/smallbusiness
- Add vertical subs based on ICP (r/realestate, r/dentistry, r/webdev, r/freelance, etc.)
- High-yield phrases: "anyone else", "I'm stuck", "I gave up", "ended up paying", "tried X but", "wish I'd known"

### Hacker News
- Use hn.algolia.com — much better than HN's native search
- Canonical incident threads (big breaches, viral fails) have the richest comment trees
- Comments > submissions. Real voices live in comments.

### X / Twitter
- **Direct fetches almost always hit the login wall.** Don't start there.
- **Loophole ladder** (try in order, stop at first that works on a tracer URL — see "Fetch strategy" below):
  1. `site:x.com "<phrase>"` / `site:twitter.com "<phrase>"` via Google — snippets alone often contain the quote verbatim
  2. `https://syndication.twitter.com/srv/timeline-profile/screen-name/<handle>` — returns JSON without auth
  3. `nitter.net/<handle>` (and mirror instances — spotty, rotate if one's down)
  4. `threadreaderapp.com` for unrolled threads
  5. `web.archive.org/web/*/x.com/<handle>/status/<id>` for specific tweets
- Quote-tweet trees of canonical incidents concentrate ICP voices
- Search patterns: `"I built"`, `"my saas"`, `"I shipped"` + pain keyword

### IndieHackers
- Post + comment search; comments are often more honest than posts
- Posts with high engagement but low karma signal divisive / raw complaints
- Usually fetches cleanly — start direct, no loophole needed

### Trustpilot / G2 / Capterra
- When ICP uses a specific tool, filter 1–3 star reviews specifically
- Highest density of verbatim pain in the entire internet for product-specific ICPs
- **G2 and Capterra front Cloudflare challenges; Trustpilot is usually the least-protected — try direct first.**
- **Loophole ladder** for G2/Capterra when direct fetch 403/429s:
  1. `site:g2.com "<product>"` / `site:capterra.com "<product>"` via Google — result snippets often contain the 1-star quote
  2. `web.archive.org` snapshot of the product's review page
  3. `webcache.googleusercontent.com` (where still available)

### LinkedIn
- Direct fetches of profiles/posts are heavily blocked. Never start there.
- **Loophole ladder:**
  1. `site:linkedin.com/posts "<phrase>"` via Google — snippets alone often yield the quote
  2. `site:linkedin.com/pulse "<phrase>"` for long-form complaint posts
  3. `web.archive.org` snapshot for specific post URLs

### Discord / Slack
- Only publicly indexed transcripts — never quote gated/paid community content
- **Loophole ladder:**
  1. `disboard.org` public server index
  2. `site:reddit.com "discord screenshot" "<phrase>"` — users often screenshot and repost discord drama to Reddit
  3. Community-run log sites for truly public servers

### Facebook Groups
- Private groups are unreachable — don't try
- **Loophole:** `site:facebook.com/groups "<phrase>"` via Google; only public-group posts are indexed (which is what we want anyway)

### Niche forums
- Identify via `"[vertical] forum"` search — many industries have long-running forums with decades of complaints
- Also: subreddit sidebars often link to the real forum where the pros are
- Most are unprotected phpBB/Discourse — direct fetch works. If Cloudflare-protected, drop to Google Site Search.

## Fetch strategy — tracer bullet + fail fast

Every agent MUST use this protocol instead of grinding against blocked endpoints.

**Tracer bullet test** (before the full sweep):
1. Pick ONE known-good URL on the surface (e.g. a specific Reddit thread, a specific tweet ID, a specific G2 product page).
2. Attempt the top-of-ladder method. If it returns readable content with the expected quote → **commit to that method for the rest of the sweep.**
3. If it fails (403, 429, login wall, empty body, Cloudflare challenge page) → drop to the next rung of the loophole ladder and retry the same tracer URL.
4. Keep descending until one rung works. That becomes the committed method.

**Fail fast** (during the sweep):
- After **2 consecutive failures** on the committed method mid-sweep → re-run the tracer from the top of the ladder (the platform may have rotated blocks).
- After **the full ladder fails on the tracer** → abort the surface. Report `BLOCKED: tried [methods], none returned content` in the agent output. Do NOT fabricate or substitute.
- Never spend more than ~3 attempts on a single blocked URL. Move on.

**Report the winning method** in the agent's output so future runs skip the ladder.

## Scoring rubric

Score each axis 0–3. Sum determines verdict.

### Pain visibility (0–3)
- **0** — No public complaints about the hypothesized pain
- **1** — Scattered, mostly generic
- **2** — Multiple threads with specific language matching the hypothesis
- **3** — Canonical incidents, named victims, viral threads with the exact pain

### Reachability (0–3)
- **0** — No findable public presence for this ICP
- **1** — 1–2 channels yield occasional voices
- **2** — 3+ channels yield voices regularly
- **3** — Dense, active, cross-platform — could fill an interview schedule this week

### Purchasing power signals (0–3)
- **0** — No evidence of budget (hobby, students, unemployed)
- **1** — Mixed — some hobbyists, some earners
- **2** — Clear earning signals (MRR mentions, tool spend, job titles)
- **3** — Documented spending behavior (paid tools, paid services, high-ticket purchase complaints)

### Population size (0–3)
- **0** — <10 distinct voices found
- **1** — 10–25
- **2** — 25–100
- **3** — 100+ across sources

### Verdict thresholds
- **VALIDATED** — total ≥9, no axis at 0
- **WEAK** — total 5–8, or any axis at 0
- **NOT FOUND** — total ≤4

## Output report template

```md
# ICP Validation Report: [ICP name]

**Verdict:** VALIDATED / WEAK / NOT FOUND
**Score:** X/12 (Pain: X, Reach: X, Money: X, Size: X)

## Summary

[2–3 sentences: where this ICP lives, how loud they are, strongest signal found.]

## Verbatim quotes

### Functional pain
- "[quote]" — [person, role, MRR if known], [source + date]
- ...

### Emotional pain
- ...

### Social pain
- ...

### Push forces
- ...

### Anxiety about solutions
- ...

### Habit
- ...

## Named individuals to DM (for mom-test)

| Handle | Platform | Context | Most recent pain signal |
|---|---|---|---|
| @X | X | [1-sentence who] | [link to tweet/post] |

Target 10+ individuals with public handles and recent (≤6 mo) pain posts.

## Reachability scorecard

| Channel | Signal density | Best use |
|---|---|---|
| X | HIGH/MED/LOW | [landing-page quotes / DM targets / long-form context] |

## Recommended next action

ONE of:
- **Proceed to `mom-test`** with the DM list above (verdict: VALIDATED)
- **Pivot ICP** — hypothesis didn't surface; retry with [specific re-tightening]
- **Cold outreach** — ICP exists but doesn't post; try [specific channel]
- **Proxy interview** — ICP is gated; interview [adjacent role] instead
```

## Strong vs weak signal classification

| Signal attribute | Strong | Weak |
|---|---|---|
| Voice | Named individual, real handle | Anonymous, burner account |
| Specificity | Names tools, amounts, dates | Generic "it sucks" |
| Recency | <6 months | >2 years |
| Context | Clear role / situation | Ambiguous |
| Reachability | Active on the platform | Dormant account |

Strong signals → quote section AND DM list.
Weak signals → quote section only (pattern evidence, not interview target).

## Failure modes to avoid

| Failure | Symptom | Fix |
|---|---|---|
| Analyst mode | Agents return summaries instead of quotes | Re-emphasize "verbatim, not synthesis" and give an example of good vs bad output |
| Generic pain | Quotes are "it sucks" vibes, not specific | Tighten ICP — the pain may be too broad |
| Wrong timeframe | Quotes are 2+ years old | Specify year range in every brief |
| Single-source dominance | 80% of quotes from one subreddit | Force distribution — cap per surface |
| Confirmation bias | Agent only returns quotes matching the hypothesis | Explicitly ask for counter-evidence ("quotes that contradict the pain hypothesis") |
