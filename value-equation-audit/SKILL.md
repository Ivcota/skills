---
name: value-equation-audit
description: Score any offer, product, or feature against Hormozi's Value Equation (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort & Sacrifice), rate each lever 1-10 with a rubric, compute a composite value score, identify the weakest lever, and generate a concrete step-by-step path to 10/10. Use when the user says "audit my offer", "rate this offer", "value equation", "is this a good offer", "why isn't this converting", "what's my offer worth", "path to 10/10", or wants to diagnose weak spots in a product, package, feature, or value proposition.
---

# Value Equation Audit

Diagnose an offer's value and produce a concrete upgrade path. Do not restate the user's offer back to them — evaluate it, score it, find the weakest lever, and ladder it to 10.

## Workflow

### Step 1 — Intake the offer (interview)

Ask the user for, in this order. Do not move on until you have all five:

1. **What is the offer?** (product/service/feature, in one sentence)
2. **Who is it for?** (the target avatar — role, stage, pain)
3. **What does the buyer get, concretely?** (deliverables, access, outcomes)
4. **What do they pay?** (price, terms, guarantees)
5. **What proof exists?** (testimonials, case studies, metrics, credentials)

If the user gives vague answers, push once for specifics (Mom-Test style — ask about the last time a real customer bought, not hypothetical). Do not guess or fill in gaps silently.

### Step 2 — Score each lever 1-10

Load the rubric from [RUBRICS.md](RUBRICS.md). For each of the four levers:

- Quote the rubric band the offer lands in
- Cite the specific evidence from Step 1 that justifies the score
- Give a single integer score 1-10

Levers:
1. **Dream Outcome** (emotional, specific, quantified end state)
2. **Perceived Likelihood of Achievement** (proof, guarantees, system specificity)
3. **Time Delay** (speed to first win and speed to full result — higher score = faster)
4. **Effort & Sacrifice** (cognitive load, time, identity cost — higher score = easier)

Be honest. Rubber-stamping 8s helps nobody. If you cannot justify a score from the evidence, score lower and say what evidence would raise it.

### Step 3 — Compute composite

Formula: `(Dream Outcome × Perceived Likelihood) / ((11 - Time Delay) × (11 - Effort))`

Note: Time Delay and Effort scores are already inverted in the rubric (10 = fast/easy), so use `(11 - score)` as the denominator weight so that a 10 contributes minimally (1) and a 1 contributes maximally (10). A perfect offer: (10×10)/(1×1) = 100. Present the raw math.

Interpret using the bands in RUBRICS.md (Grand Slam, Strong, Average, Weak).

### Step 4 — Identify the weakest lever

The weakest lever is the one with the largest gap to 10 AND the biggest leverage on the composite. If two levers tie, pick the one in the denominator (Time Delay or Effort) — denominators have outsized impact.

State it plainly: "Your weakest lever is X at Y/10. Moving it to 10 would raise your composite from A to B."

### Step 5 — Path to 10/10

Load [PATHS.md](PATHS.md) and produce a tailored ladder for the weakest lever:

- **Current state**: the score and why
- **Next rung** (one score up): the smallest change that moves it
- **Each subsequent rung** up to 10: concrete tactic, rough effort, expected lift
- **First action this week**: one thing the user can do in the next 7 days

Then do the same — briefly — for the second-weakest lever, so the user has a full plan.

### Step 6 — Re-score projection

Show a projected composite if the user executes the path: "Today: X. After Week 1 actions: Y. After full path to 10 on weakest lever: Z."

## Output format

Produce a single report with these sections, in this order:

1. **Offer summary** (2-3 lines, their words)
2. **Scores** (table: lever | score | rubric band | evidence)
3. **Composite** (math + interpretation band)
4. **Weakest lever diagnosis**
5. **Path to 10/10** (ladder for weakest lever, brief for second)
6. **This week** (one concrete action)
7. **Projected composite**

Keep it tight. The user wants a diagnosis and a move, not a lecture.

## Rules

- Never score without cited evidence from the intake
- Never skip the intake — guessing produces a worthless audit
- If the offer is pre-launch with no proof, Perceived Likelihood caps at 4; say so
- If the user pushes back on a score, ask what evidence would justify a higher one; do not capitulate
- The path to 10 must be concrete (specific tactics, not "improve your marketing")

## References

- [RUBRICS.md](RUBRICS.md) — the four scoring rubrics + composite interpretation
- [PATHS.md](PATHS.md) — rung-by-rung ladders from 1 to 10 for each lever
