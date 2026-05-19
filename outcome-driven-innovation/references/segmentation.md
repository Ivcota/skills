# Outcome-Based Segmentation

The premise: **demographics, role, age, company size, and price point cannot predict unmet outcomes.** Two 45-year-old women in the same income bracket buying paint for their houses can have entirely different desired outcomes — and grouping them together hides every innovation opportunity. ODI segments on *outcome patterns* instead.

## Why traditional segmentation fails for innovation

Traditional segments are useful for marketing, sales, and ad targeting — *not* for innovation. They group customers by who they *are*, not by what they're trying to *get done*. The result is a "segment" of forty-something men who want completely different things from your product.

Ulwick's claim: the only way to find a group of customers with a *common set of underserved outcomes* is to use the outcomes themselves as the segmentation variable. Everything else is decoration.

## Outcome-Based Segmentation (existing markets)

**Goal:** find groups *within your current market* who share the same underserved outcomes — segments of opportunity.

**Method:**

1. **Capture all outcomes** for the job (50–150 per [jobs-outcomes-constraints.md](jobs-outcomes-constraints.md)).
2. **Survey** ≥ 180 respondents on importance + satisfaction for every outcome (1–5 scale).
3. **Factor analysis** identifies which outcomes co-vary — if two outcomes are consistently rated in parallel, they collapse into one factor. This compresses 100+ outcomes into ~10–20 dimensions usable for clustering.
4. **Cluster analysis** on the importance/satisfaction matrix groups respondents into segments who *value the same outcomes the same way*.
5. **Profile** the segments to learn who they are (which is often a surprise — segments rarely align with demographic preconceptions).
6. **Apply the Opportunity Algorithm per segment.** An outcome scored 6 overall might be 14 in one segment.

**Output:** typically 3–6 outcome-based segments per market, each with its own opportunity ranking.

**Kurtosis tip:** outcomes with high kurtosis (sharply peaked importance distribution) make the best segmentation variables — they cleanly separate respondents into "this matters a lot to me / not at all." Flat distributions don't discriminate.

## Job-Based Segmentation (new markets)

**Goal:** find groups of *nonconsumers* who are struggling to get a related job done — discover an entirely new market.

**Method:** use *job statements* (not outcomes) as the clustering variable. Score how important each related job is and how satisfied current solutions are. Cluster on those.

**Why this is different:** outcome-based segmentation finds opportunities *within* a known job. Job-based segmentation finds *new* jobs to enter — often jobs being done badly or not at all by anyone.

**Example:** clustering on "jobs adjacent to listening to music" — download, organise, share, discover, learn about the artist — revealed segments of people frustrated with the *workflow* around music. Apple targeted that cluster with iPod + iTunes. The MP3 player itself was a commodity; the *job cluster* was the new market.

## When to use which

| If you want to... | Use |
|-------------------|-----|
| Improve an existing product / category | **Outcome-based** segmentation |
| Find segments to disrupt with a cheaper offering (over-served) | **Outcome-based** |
| Re-position existing products (Step 6) | **Outcome-based** |
| Enter a brand-new market | **Job-based** segmentation |
| Identify nonconsumers (people who avoid the category) | **Job-based** |
| Decide whether to launch ancillary products | **Job-based** |

## What "segments of opportunity" look like

In the angioplasty-balloon market, Cordis found 15 underserved outcomes by overall score. Outcome-based segmentation revealed three sub-segments, each with a distinct top-5. Cordis then:
- Re-messaged existing products to each segment's top outcomes (positioning lift)
- Re-prioritised the pipeline — the *stent* (one of forty pipeline projects) was the only project hitting the most underserved outcome ("minimise restenosis") in the largest segment. Cordis poured resources into the stent, became first to market, and created a billion-dollar business in two years.

Demographics could not have surfaced this. The stent already existed in the pipeline; the segmentation told the company *which* project mattered.

## Common Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Segmenting on demographics first and *then* measuring outcomes | Pre-decides what segments exist; misses real ones | Let cluster analysis on outcomes form the segments |
| Using needs-based segmentation ("the value-seeker," "the convenience-lover") | Inputs are adjectives, not metrics — segments are personas, not innovation targets | Replace adjectives with the underlying outcomes; segment on those |
| Treating outcome segments as marketing personas | Personas tell you *who* to sell to; outcome segments tell you *what to build* | Use both — keep them separate — and never merge their definitions |
| Skipping factor analysis | 100+ outcomes is too many dimensions to cluster cleanly | Compress with factor analysis first |
| Running one segmentation across multiple jobs | Each job has its own outcome set; mixing them produces meaningless segments | One segmentation per job |

## The deliverable

After this step you should have:

1. A list of 3–6 segments, each defined by an outcome-importance pattern
2. The Opportunity Algorithm re-run per segment
3. The "common opportunities" (high score in *all* segments) — broad-market targets
4. The "segment-specific opportunities" (high score in one segment, low in others) — focused targets
5. A profile of who is in each segment (demographic / firmographic / behavioural) — for go-to-market planning only

Steps 5 (Targeting) and 6 (Positioning) of ODI take this segmentation as their input.
