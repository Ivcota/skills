# The Opportunity Algorithm

The single equation that turns innovation from art into arithmetic. Once you have outcome statements rated by customers on importance and satisfaction, this formula tells you exactly where to invest, where to cut cost, and what to ignore.

## The Formula

```
Opportunity = Importance + max(Importance − Satisfaction, 0)
```

The second term **cannot go below zero** — over-satisfaction does not deduct from importance, it simply stops contributing. Over-satisfied outcomes are a *separate signal* (cost-reduction targets), not a negative.

## The 10-Point Scale

Importance and Satisfaction each enter the formula as a number 0–10 derived from a 1–5 customer rating.

For each outcome, ask N customers:
- *How important is this outcome to you?* (1 = not at all, 5 = extremely)
- *How satisfied are you with current solutions on this outcome?* (1 = not at all, 5 = extremely)

The score = **percentage of respondents rating it 4 or 5, expressed on a 10-point scale**.

| % rating 4 or 5 | Score |
|-----------------|-------|
| 90% | 9.0 |
| 75% | 7.5 |
| 50% | 5.0 |
| 30% | 3.0 |

This is sometimes called the "Top-2-Box" percentage. ≥ 180 respondents per segment is Strategyn's working minimum for stable scores.

## Reading the Opportunity Score

| Score | Interpretation | Action |
|-------|----------------|--------|
| **≥ 15** | Extreme opportunity — almost never seen | Drop everything; this is a category-defining gap |
| **12 – 15** | Ripe opportunity | Top priority for innovation / R&D |
| **10 – 12** | Worth pursuing | Include in roadmap |
| **< 10** | Not worth pursuing | Ignore for innovation; may still be cost-reduction targets |

The highest possible score is 20 (importance = 10, satisfaction = 0). Anything in the 12+ band is rare and load-bearing.

## Underserved vs. Overserved

The Opportunity Algorithm splits the outcome list into three zones:

| Zone | Definition | Innovation move |
|------|------------|-----------------|
| **Underserved** | Important *and* unsatisfied | Add function/performance — even at higher cost. This is where breakthrough products live. |
| **Appropriately served** | Importance ≈ Satisfaction | Maintain; do not waste R&D here |
| **Overserved** | Unimportant *and* highly satisfied | Strip cost, strip features. This is where **disruptive innovation** lives — a cheaper, "good-enough" version wins. |

**Disruption is just over-served outcomes targeted by a cheaper player.** Christensen-style disruption is mathematically detectable from the opportunity scoreboard, not just narratively. When mainstream products keep adding performance to outcomes that are already over-served, an upstart with a cheaper, simpler product attacks from below.

## The Importance / Satisfaction Matrix

Plot every outcome on a 2D map:

```
            High Satisfaction →
   ┌────────────────────────────┐
H  │  Appropriately served      │  ← Maintain
i  │                            │
g  │                            │
h  │  ★ UNDERSERVED ★           │  ← Innovate
   │  (high I, low S)           │
↑  │                            │
I  ├────────────────────────────┤
m  │                            │
p  │                            │
o  │  Ignore                    │  OVERSERVED
r  │                            │  ← Cut cost / disrupt
   └────────────────────────────┘
```

The 45° line from origin = appropriately served. Distance *above* the line in the high-importance band = opportunity. Distance *above* the line in the low-importance band = waste.

## Worked Example (drug-infusion pump, p. xviii)

90% of pain-management nurses rated "minimise the time it takes to implement a dose change" 4 or 5 for importance. Only 15% rated it 4 or 5 for satisfaction.

```
Importance = 9.0
Satisfaction = 1.5
Opportunity = 9.0 + max(9.0 − 1.5, 0) = 9.0 + 7.5 = 16.5
```

Opportunity score = **16.5** — extreme. The R&D team now knows two things: *where* to focus creativity, *and* that the time spent will produce ideas worth pursuing. Most of the eighty-plus outcomes on a typical job will fall under 10; only a handful (5–15) will cross 12. Those handful are the entire roadmap.

## Three Mistakes That Wreck the Algorithm

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Using fewer than 180 respondents per segment | Importance/Satisfaction scores wobble; rankings flip on rerun | Run a power-analysis; oversample if niche segments |
| Mixing direction words ("eliminate" vs "minimise") in the same survey | Word choice shifts the importance rating; signal becomes noise | Lock all outcomes to "Minimise" or "Increase" before data collection |
| Reading the score for one customer | Hides segment-level opportunity (an outcome can be 16 in one segment, 6 in another) | Always score *per segment*; then look for outcomes that are 12+ in *any* segment — those are segment-specific opportunities |

## What to Do With the Output

1. **Sort all outcomes by opportunity score, descending.** This single list replaces every backlog, roadmap, and idea-board you have.
2. **Pull the top 5–15 ranked above 12.** These are your underserved targets.
3. **Pull the bottom-quartile high-satisfaction outcomes.** These are cost-reduction targets — strip features here.
4. **Hand the underserved list to:**
   - Marketing (re-message existing products that already satisfy them — Step 6)
   - Pipeline (re-rank in-flight projects by how many they hit — Step 7)
   - Ideation (focused brainstorming on whatever's left — Step 8)
   - R&D / acquisitions (technologies needed to hit outcomes nothing yet addresses)

## Why this is the load-bearing piece

Every other ODI step uses this output. Segmentation clusters customers by *opportunity pattern*. Targeting picks subsets of these rankings. Positioning matches features to high-opportunity outcomes. The Customer Scorecard sums concept-impact across the *same outcome list*. If the algorithm is wrong, everything downstream compounds the error. If it's right, the rest of ODI almost runs itself.
