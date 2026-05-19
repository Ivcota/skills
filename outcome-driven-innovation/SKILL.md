---
name: outcome-driven-innovation
description: Apply Anthony Ulwick's Outcome-Driven Innovation (ODI) — the eight-step operational method that turns "what customers want" from guesswork into a quantitative process. Silence the Voice of the Customer; capture **Jobs, Outcomes, and Constraints** instead; rank them with the **Opportunity Algorithm** (`importance + max(importance − satisfaction, 0)`); segment by unmet outcomes; and score every concept on the Customer Scorecard before a line of code is written. Use when the user mentions "outcome-driven innovation", "ODI", "Ulwick", "opportunity algorithm", "outcome statement", "desired outcomes", "underserved / overserved", "outcome-based segmentation", "customer scorecard", "jobs to be done" *for product development specifically*, "what customers want", or "Strategyn". Also trigger when planning a new product or feature, auditing why an R&D pipeline is producing duds, designing a customer interview to extract metrics (not opinions), prioritising a backlog of opportunities, segmenting a market that demographics won't split, repositioning a product whose true value is hidden, or evaluating concepts before build.
metadata:
  authors: Anthony W. Ulwick
  source: What Customers Want — Using Outcome-Driven Innovation to Create Breakthrough Products and Services, McGraw-Hill, 2005
  version: 1.0
---

# Outcome-Driven Innovation (ODI)

In any other business process — manufacturing, finance, sales — a 50–90% failure rate would be unacceptable. In innovation, it has been tolerated for decades. Ulwick's claim: that failure rate is not a creativity problem, it is a *process* problem. The customer-driven movement asks customers what they want and dutifully builds it — but customers volunteer **solutions, specifications, needs, and benefits**, none of which are useful inputs for innovation. ODI replaces them with three inputs that *are* — **Jobs, Outcomes, Constraints** — and ranks them with a single equation.

## Core Principle

*"Customers buy products and services to help them get jobs done."* The job is the unit of analysis, not the customer. Customers use **50–150 outcomes (not a handful)** to judge how well any job is getting done — they have them in their minds but seldom articulate them. The job to capture them belongs to the company, not the customer. Once captured, the **Opportunity Algorithm** mathematically reveals which outcomes are *underserved* (high importance, low satisfaction — targets for innovation) and which are *overserved* (low importance, high satisfaction — targets for cost reduction). Everything downstream — segmentation, targeting, messaging, prioritisation, ideation, concept evaluation — becomes derivative of these rankings.

**The mantra:** *Silence the "Voice of the Customer."* The literal voice of the customer sidetracks innovation because customers are not qualified to know what solutions are best — that is the job of the organisation. Listen instead for the metrics customers use to judge value.

## The Eight-Step ODI Process

Apply in order; each step's output is the next step's input.

1. **Formulate Innovation Strategy** — decide which of the four innovation types (Product/Service, New-Market, Operational, Disruptive), which of the four growth options, and which customer in the value chain to target.
2. **Capture Customer Inputs** — collect three input types: **Jobs** (functional + emotional [personal + social]), **Desired Outcomes** (50–150 per job), **Constraints** (roadblocks to getting the job done). See [references/jobs-outcomes-constraints.md](references/jobs-outcomes-constraints.md).
3. **Identify Opportunities** — score every outcome by importance + satisfaction; rank with the Opportunity Algorithm. See [references/opportunity-algorithm.md](references/opportunity-algorithm.md).
4. **Segment the Market** — group customers by *unmet outcomes*, not demographics. Reveals "segments of opportunity" demographics cannot find. See [references/segmentation.md](references/segmentation.md).
5. **Define Targeting Strategy** — choose which underserved outcomes to attack (broad-market or segment-specific) and which overserved outcomes to strip cost from.
6. **Position Current Offerings** — re-message existing products around the underserved outcomes they already satisfy (Cordis went from 1% → 5% market share in six months on messaging alone).
7. **Prioritise the Development Pipeline** — re-rank in-flight projects by how many targeted opportunities they address; kill the rest.
8. **Define Breakthrough Concepts** — focused brainstorming on remaining unmet outcomes; evaluate with the **Customer Scorecard** *before* build. See [references/customer-scorecard.md](references/customer-scorecard.md).

## The Opportunity Algorithm (the load-bearing equation)

```
Opportunity = Importance + max(Importance − Satisfaction, 0)
```

Importance and Satisfaction are each the % of customers rating that outcome 4 or 5 on a 1–5 scale, placed on a 10-point scale (75% → 7.5). Score ≥ 12 = ripe opportunity; 10–12 = worth pursuing; < 10 = ignore. Overserved outcomes (low importance, high satisfaction) become cost-reduction targets, not feature targets. *This single formula replaces the entire debate about what to build next.*

## The Input Taxonomy (this is the whole reframe)

Customers volunteer five things when asked for "requirements"; only the bottom three are useful. Train yourself to translate up the stack.

| Input type | Example (razor) | Useful for ODI? |
|------------|-----------------|-----------------|
| **Solution** | "Add a lubrication strip" | ❌ Customer-as-engineer; produces me-too products |
| **Specification** | "Lighter weight" | ❌ Locks in one implementation |
| **Need** | "Reliable, durable" | ❌ Adjective — un-measurable |
| **Benefit** | "Faster", "easier to use" | ❌ Vague — 21 definitions of "easy to use" in one Motorola study |
| **Constraint** | "Can't get a signal indoors" | ✅ Roadblock to job — innovation target |
| **Job** | "Remove facial hair" | ✅ The unit of analysis |
| **Desired Outcome** | "Minimise the number of nicks when shaving" | ✅ Measurable, stable over time, drives every downstream step |

Outcome statements have a strict format: **Direction (Minimise / Increase) + Unit of Measure (time, number, frequency, likelihood) + Outcome Desired**. *Only "minimise" and "increase"* — words like "reduce", "eliminate", "prevent" measurably skew importance ratings.

## Eight Sources of Variability (what ODI fixes)

The reasons 50–90% of innovation initiatives fail, per Ulwick — every one mapped to an ODI step:

| Failure mode | Fixed by step |
|--------------|---------------|
| Ill-conceived growth strategies | 1. Formulate Strategy |
| Faulty data collection (Voice of the Customer) | 2. Capture Inputs |
| Missed opportunities | 3. Identify Opportunities |
| Poor market segmentation | 4. Segment |
| Wrong growth targets | 5. Target |
| Unfocused marketing / messaging / branding | 6. Position |
| Poorly prioritised development | 7. Prioritise pipeline |
| Scattershot idea generation | 8. Define Concepts |

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| **Asking customers what they want** | Customers offer solutions and benefits, not the metrics they use to judge value. | Ask "how do you measure success at this job?" — extract 20–30 outcomes per interview. |
| **Capturing < 20 outcomes per job** | A handful of outcomes hides the underserved ones — every job has 50–150. | Keep extracting until no new outcomes surface across 20–30 interviews. |
| **Brainstorming first, validating later** | You generate hundreds of ideas, then test them on customers — variability everywhere. | Identify underserved outcomes *first*; generate a handful of ideas aimed at them; evaluate on the Customer Scorecard before build. |
| **Segmenting by demographics, role, or price point** | Age and company size don't predict unmet outcomes — wastes the segmentation. | Segment by *outcome patterns* using cluster analysis on importance/satisfaction data. |
| **Letting the sales force speak for customers** | Salespeople capture inputs as "solutions" and "specs" — solutions in, solutions out. | Let trained researchers go to end users directly; let salespeople sell. |
| **Treating "easy to use" as a requirement** | One Motorola study found 21 distinct desired outcomes hiding behind "easy to use." | Pin every adjective to a measurable outcome statement. |
| **Mixing "eliminate" / "prevent" / "minimise" in outcome statements** | Word choice shifts the importance rating; introduces statistical noise. | Use only "minimise" or "increase" — nothing else. |
| **Q-F-D / House of Quality for innovation** | A manufacturing-reliability tool retrofitted to NPD; people fill out the matrix instead of doing the work. | Use outcome statements directly; the matrix becomes unnecessary. |
| **Skipping Step 6 (Positioning)** | The fastest revenue lift in ODI is re-messaging existing products against newly discovered underserved outcomes — Cordis 1% → 5% in 6 months. | Always run positioning *before* touching the pipeline. |
| **Treating discovered opportunities as suggestions** | Teams revert to favourite projects; the ranked list collects dust. | "Treat the discovered opportunities as sacred" — reward employees for satisfying ranked outcomes, not for ideas. |

## Quick Diagnostic

Audit any product, roadmap, or research effort. *Goal: every row Yes.*

| Question | If No | Action |
|----------|-------|--------|
| Can you state the customer's **job to be done** in one sentence with a functional verb? | You're describing a product, not a job. | Re-frame: "When [circumstance], the customer is trying to [verb + object]." |
| Do you have **50+ outcome statements** for that job, in `min/increase + unit + outcome` format? | You have opinions, not metrics. | Extract outcomes from 20–30 interviews; see [references/jobs-outcomes-constraints.md](references/jobs-outcomes-constraints.md). |
| Have customers rated every outcome on **importance and satisfaction** (1–5)? | You don't know what's underserved. | Quantitative survey (web/phone); ≥ 180 respondents per segment. |
| Have you ranked outcomes with the **Opportunity Algorithm**? | You'll target popular ideas instead of underserved ones. | `Importance + max(Importance − Satisfaction, 0)`. |
| Did you **segment by outcome patterns**, not demographics? | Your "segments" are marketing personas, not innovation targets. | Cluster customers on the outcome-importance matrix. |
| Did you score concepts on the **Customer Scorecard** *before* building? | You'll discover failure after the spend. | Rate each concept's projected impact on every outcome; sum the weighted score. |

## Reference Files

- [jobs-outcomes-constraints.md](references/jobs-outcomes-constraints.md): the three input types, job dissection, outcome statement format, the 1-hour outcome interview.
- [opportunity-algorithm.md](references/opportunity-algorithm.md): the equation, the 10-point scale, the importance/satisfaction matrix, underserved-vs-overserved decisions.
- [segmentation.md](references/segmentation.md): outcome-based vs job-based segmentation, factor analysis + cluster analysis, why "segments of opportunity" beat personas.
- [customer-scorecard.md](references/customer-scorecard.md): focused brainstorming, the five ideation guidelines, evaluating concepts on the full outcome set, the 5–10% vs 20%+ threshold for "breakthrough."

## Further Reading

This skill is based on *What Customers Want — Using Outcome-Driven Innovation to Create Breakthrough Products and Services* by Anthony W. Ulwick (McGraw-Hill, 2005, ISBN 0-07-140867-3). See `sources.md` for the full extraction manifest. For the deeper methodology and Ulwick's later work:

- Ulwick, A. (2002). "Turn Customer Input into Innovation." *Harvard Business Review*, January 2002.
- Ulwick, A. (2016). *Jobs to Be Done: Theory to Practice* — the successor volume that formalises ODI under the JTBD banner.
- Strategyn (Ulwick's firm): `strategyn.com` — case studies, the Outcome-Based Brand library, training in ODI.
- Christensen, C. & Raynor, M. (2003). *The Innovator's Solution* — Ch 3 references Ulwick's outcome-based segmentation directly.

## About the Author

**Anthony W. Ulwick** is the founder and CEO of Strategyn, the consultancy that originated Outcome-Driven Innovation. He began developing ODI in 1984 after the failure of IBM's PCjr (his project at the time) convinced him that the customer-driven approach was structurally broken. Over the next two decades he refined the method across 100+ engagements with Microsoft, Bosch, Johnson & Johnson, Motorola, Pratt & Whitney, Cordis, and others. Harvard's Clayton Christensen called ODI "the most disciplined and predictable approach to innovation I have seen."
