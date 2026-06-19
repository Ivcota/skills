# The Four Constraint Types

The intervention differs by type — diagnose type before fixing. The single most common TOC failure is treating a policy or paradigm constraint as a physical one (and then "elevating" by hiring or buying capacity that doesn't help).

## Physical

A resource — a machine, a person, a server, a piece of equipment — that's the slowest stage in the flow.

**Tells:**
- Work piles up just upstream of the resource (the queue).
- Stages downstream of the resource sit idle waiting for output.
- Adding capacity to non-physical-constraint stages doesn't move T.

**Examples:**
- Manufacturing: a CNC machine that's slower than the rest of the line.
- Software: a single staging environment shared by the whole team.
- Sales: one closer who handles all final pitches.
- Hiring: one hiring manager doing all final interviews.

**Intervention progression:** Exploit (squeeze full capacity from the resource) → Subordinate (don't release work faster than it can absorb) → Elevate (add a second resource, hire, scale).

## Policy

A *rule* — written or unwritten — that limits flow even though physical capacity exists.

**Tells:**
- People route around the rule with workarounds.
- Capacity is sitting idle but blocked by the rule from being used.
- Hiring or adding capacity doesn't fix it (the new capacity hits the same rule).
- Same problem returns after each "fix."

**Examples:**
- "Every PR needs two reviewers" — when reviews queue up because the second reviewer is scarce, the rule is the constraint, not the reviewers.
- "No hire without VP approval" — VP becomes a hiring bottleneck even though recruiters and interviewers have capacity.
- "QA can't be cross-trained" — a "QA shortage" that's actually a staffing-policy constraint.
- "Sales can't quote discounts above 10% without director approval" — director becomes the throughput limiter.
- Personal: "I don't take calls before noon" creating an artificial scarcity of meeting slots.

**Intervention progression:** *Don't try to exploit a policy constraint by squeezing harder — the rule is the squeeze.* Go straight to challenging the rule. Subordinate becomes "what would change if the rule were relaxed?" Elevate is "change the rule" (often free, sometimes politically expensive).

**Why this matters:** policy constraints are *cheap to elevate* (a meeting and a memo) but *politically expensive* (someone owns the rule and benefits from it). Most organizations would rather hire than change a rule. TOC says: change the rule first, then see if you still need to hire.

## Market

Demand is the constraint. The system has more capacity than the market wants.

**Tells:**
- Excess capacity. Resources sit idle. No queues anywhere internally.
- Sales pipeline is the slowest stage; everything downstream is starving.
- Adding internal capacity makes things *worse* (higher OE, no more T).

**Examples:**
- Manufacturing: factory running at 60% utilization with no queue.
- Software: features ship faster than users adopt them.
- Sales: sales team can close more than the lead gen team brings in.
- Personal: you have more available hours than commitments worth your time.

**Intervention progression:** Exploit = get more value from existing demand (upsell, retain, cross-sell). Subordinate = don't add internal capacity (resist the urge to "stay busy"). Elevate = invest in *demand generation* (sales, marketing, new segments, new products). This is the only constraint type where the intervention is *outside* the system.

**Goldratt's note:** when the market becomes the constraint, most companies forget how to sell because they spent years optimizing production. They hire more producers when they need salespeople. (Goldratt's *It's Not Luck* is largely about this transition.)

## Paradigm

The team *believes* something is the constraint that isn't. The mental model itself is the bottleneck.

**Tells:**
- Fixes don't move T. The "constraint" gets elevated repeatedly, T doesn't budge.
- The team disagrees about what the constraint is.
- Recurring crises in the same place despite multiple "solutions."
- The diagnosis matches a popular industry narrative ("we need more engineers", "we need more leads") rather than evidence in your specific system.

**Examples:**
- "We need more engineers" — when the real constraint is a policy that batches deploys to once a week.
- "We need more leads" — when the real constraint is a sales process that disqualifies fits.
- "We need a better PM" — when the real constraint is no decision-making authority.
- Personal: "I don't have enough time" — when the real constraint is over-commitment driven by a "say yes by default" rule.

**Intervention progression:** Cannot exploit / subordinate / elevate a paradigm directly. Must surface the underlying assumption and break it. The [Evaporating Cloud](evaporating-cloud.md) is the TOC tool for this — it externalizes the conflict between competing needs and surfaces the wrong assumption underneath.

## Diagnostic decision tree

1. **Is your output less than market demand?** → physical or policy.
2. **Is output greater than demand?** → market.
3. **Where does work pile up (longest queue / oldest WIP)?** → constraint is the resource just downstream of the pile.
4. **Does the same problem keep returning after each fix?** → paradigm or policy. The "physical" diagnosis is wrong.
5. **Have you elevated capacity once already and T didn't move?** → almost certainly policy or paradigm.

## Why typing matters

Every wrong typing wastes an elevation cycle:
- Treating policy as physical → you hire and the new hires hit the same rule. T unchanged. OE up.
- Treating paradigm as physical → you hire and the team finds a new "constraint" to point at. T unchanged. OE up.
- Treating market as physical → you produce more inventory you can't sell. T unchanged. I up.
- Treating physical as policy → you change rules and the bottleneck stays. Productivity theatre.

**Rule:** before elevating, force the typing exercise. Wrong typing is more expensive than slow diagnosis.
