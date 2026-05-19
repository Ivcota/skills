# Focused Brainstorming & the Customer Scorecard

The final ODI step. Most companies brainstorm hundreds of ideas and then try to figure out which are good — wasting time on volume and producing me-too concepts. ODI inverts the process: brainstorm a small number of ideas *aimed at specific underserved outcomes*, then evaluate each on the entire outcome set before a single dollar of build cost is spent.

## Why traditional brainstorming fails

Three failure modes:
1. **Unfocused creativity** — generating ideas with no specific target, hoping volume produces a winner
2. **Too many ideas** — managers cannot evaluate hundreds of concepts; quality drowns in quantity
3. **No objective evaluation** — concepts are judged by enthusiasm, internal politics, or "fit with current business model" instead of customer-value impact

Result: 50–90% of innovation initiatives fail. The cure is *constraint*: focus on the ranked underserved outcomes; aim ideation at *those* and nothing else.

## Focused Brainstorming — Five Guidelines

1. **Stay focused on the targets.** One ideation session per underserved outcome (or tight cluster). Do not allow drift.
2. **Aim for breakthrough improvement.** A target = a 20%+ jump in satisfaction on the outcome. Anything less is incremental and goes into the maintenance pipeline.
3. **Constrain thinking to enhance creativity.** Counter-intuitive — but unbounded brainstorming produces bland ideas. Constraints (cost ceilings, form-factor limits, regulatory boundaries) force novel combinations.
4. **Eliminate bad ideas quickly.** Score against the outcome targets in the room; kill ideas that don't move the needle.
5. **Optimise the best idea for cost, effort, risk, and sustainability.** Iterate on the survivor — combine sub-ideas, add features that satisfy adjacent outcomes — before declaring it final.

Volume is *not* the goal. The Pratt & Whitney team generated about a dozen ideas (not hundreds) across all their targeted outcomes and selected the five highest-value combinations.

## The Customer Scorecard

A quantitative tool that scores any concept's customer value *before build*. Replaces gut-feel evaluation and concept testing in focus groups.

### Setup

1. **Take the ranked outcome list** from the Opportunity Algorithm (top 15–30 outcomes for the target segment).
2. **Weight each outcome by its opportunity score** (importance + max(I − S, 0)). Outcomes with score 14 carry more weight than outcomes with score 11.
3. **For each candidate concept, estimate the projected satisfaction lift** on each outcome (–10 to +10 scale; positive = improves, negative = degrades).
4. **Score = Σ(weight × projected lift) across all outcomes.** Sum is the concept's projected customer-value impact.
5. **Compare concepts head-to-head, including the current product and competitors.**

### Reading the score

| Concept score vs. current product | Category |
|-----------------------------------|----------|
| ≥ 20% improvement | **Breakthrough** — pursue aggressively |
| 5–10% improvement | Incremental — pipeline-worthy if cheap |
| 0–5% improvement | Me-too — kill or rework |
| Negative on important outcomes | Hidden regression — fix or kill |

### Pratt & Whitney example (Ch 8)

P&W ran focused brainstorming on each top opportunity. The team rated their leading concept against the current offering and the top competitor. Customer Scorecard projected **66.7% of total available value** — 38% better than P&W's current offering, 25% better than the competitor's. They built it. One year later, real customer satisfaction had risen 35% — almost exactly the model's prediction. Within two years, P&W regained lost market share *and* captured five points more.

The lesson: with a complete outcome list and disciplined scoring, you can predict commercial outcomes well enough to make the build/no-build call without prototyping.

## When the Scorecard Reveals "We Can't Hit This"

If no candidate concept lifts a high-opportunity outcome by 20%+, you have a *technology* gap. Three responses:

| Gap source | Response |
|------------|----------|
| Need a new technology that doesn't exist | Send the outcome to **R&D** as a technology-development target (Motorola did this for "superior voice command" — assigned to long-term mobile-radio R&D) |
| Technology exists outside the company | Send to **acquisition** team — buy the technology rather than build it |
| Outcome is unsolvable with current physics | De-prioritise; revisit annually |

This converts ODI into an *operating system* for R&D and M&A, not just product development.

## Definition: "Breakthrough Concept"

> A concept that will deliver customers significant new value. Most successful new products improve the satisfaction of underserved outcomes between 5 and 10 percent, while breakthrough products typically improve the satisfaction level by 20 percent or more.

The 20% threshold is the operational definition of "breakthrough" in ODI. Use it. Stop calling 5% wins "breakthrough."

## Common Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Brainstorming with no outcome target | 200 ideas, none aimed at value | One outcome (or tight cluster) per session |
| Scoring concepts on a subset of outcomes | Hidden regression on un-scored outcomes kills the launch | Score the *entire* outcome list — usually 50+ items — not just the targeted ones |
| Testing concepts in focus groups | Customers like prototypes for emotional reasons that don't predict purchase | Replace focus-group concept testing with Scorecard analysis |
| Letting customers score the concept | They don't know how a technology will affect outcomes they haven't experienced | Internal experts score; customer data is for *importance and satisfaction* of the underlying outcomes |
| Ignoring overserved outcomes when scoring | Concepts may add cost without value (over-engineering) | Penalise concepts that lift already-satisfied outcomes — those increases add cost, not value |
| Optimising the *first* idea instead of the *best* | Anchoring kills better candidates | Generate the small set first, score, *then* optimise the survivor |

## The Output of Step 8

After this step you should have:

1. **A short list of ideas** (≤ 12) per targeted underserved outcome
2. **Customer Scorecard scores** for each idea against the full outcome set
3. **A clear winner** (or "no idea hits 20% — escalate to R&D / acquisitions")
4. **A financial justification** built on the projected satisfaction lift (which predicts revenue better than ROI projections)
5. **A go/no-go decision** made *before* build — not after launch

This is what "transforming innovation into a predictable discipline" actually means: the decision to build is now defensible on numbers that correlate with commercial success.
