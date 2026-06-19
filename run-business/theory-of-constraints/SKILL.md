---
name: theory-of-constraints
description: Diagnose system bottlenecks and prescribe interventions using Eliyahu Goldratt's Theory of Constraints — Five Focusing Steps (Identify → Exploit → Subordinate → Elevate → Repeat), throughput accounting (T/I/OE), Drum-Buffer-Rope scheduling, and the four constraint types (physical, policy, market, paradigm). Produces a Constraint Diagnosis one-pager naming the system's bottleneck, the type, the evidence, and a sequenced exploit→subordinate→elevate plan. Use when the user mentions "bottleneck", "constraint", "throughput", "flow", "stuck", or "Theory of Constraints". Distinct from `the-one-thing` (personal focus on a single goal) and `good-strategy-bad-strategy` (kernel diagnosis); TOC answers "where in the system is the leverage" for any multi-stage flow — software, sales, hiring, manufacturing, personal.
---

# Theory of Constraints

Diagnose where the system's bottleneck is, then run Goldratt's Five Focusing Steps to fix it without optimizing the wrong thing. Universal lens — works for software flow, sales pipelines, hiring, manufacturing, personal productivity. Anywhere work moves through stages and queues form, TOC applies.

**Output: a Constraint Diagnosis one-pager.** Eight sections, copy-pasteable. The artifact at the end forces every decision through a structure so the user can't skip the hard parts (T/I/OE definitions, evidence, "what's the next constraint after this one moves").

## When to use / when not to use

**Use when** the user says any of: bottleneck · constraint · throughput · flow · stuck · Theory of Constraints · Goldratt · The Goal · Drum-Buffer-Rope · Critical Chain · Five Focusing Steps.

**Disambiguate from neighbors:**
- `the-one-thing` answers "what's *my* single priority?" — TOC answers "what's the *system's* limit?"
- `good-strategy-bad-strategy` writes a strategic kernel — TOC diagnoses the operational flow that strategy must respect.
- `improve-codebase-architecture` is structural (deepen modules) — TOC is flow (where work piles up). Often complementary.
- `faas` ships a feature end-to-end — TOC asks "why does feature shipping keep hitting the same wall?"

## Pace and shape

- **Diagnostic-first.** Don't propose interventions until the constraint is identified and typed.
- **Required reframe before Step 1** — user defines T/I/OE for *their* system. Skip and the rest is unmoored.
- **Tag every move** as *(Goldratt)* or *(workflow)*. Lets the user trust what's TOC canon vs. operationalization.
- **The Four Heresies are a watchlist, not a phase.** Detect them at any step in the user's reasoning and call them out by name.
- **Backtracking allowed.** Constraints move; if the user discovers the constraint moved mid-conversation, replay from Step 1.

---

## Setup — define T/I/OE before Step 1 *(Goldratt)*

Goldratt's measurement system replaces traditional cost accounting. Every TOC decision is judged against:

- **Throughput (T)** — money the system generates *through sales* (sellable output, not gross production).
- **Inventory / Investment (I)** — money tied up in the system (WIP, raw inputs, started-not-finished work).
- **Operating Expense (OE)** — money spent turning I into T (team cost, tooling, overhead per unit time).

A "good" change increases T, decreases I, or decreases OE — for the system as a whole.

**Translations *(workflow)*:**

| Domain | Throughput | Inventory | Operating Expense |
|---|---|---|---|
| Software | Features shipped to users | Started-not-shipped work (WIP, open PRs, half-built features) | Team cost + tooling per unit time |
| Sales | Closed revenue | Pipeline (leads × time-in-stage) | Sales team cost + tooling |
| Hiring | Hires made | Candidates in pipeline | Recruiter time + interviewer time |
| Personal | Outcomes that matter | Open loops, started-not-finished commitments | Your time |

**Required exit:** user writes one line each. T = ___. I = ___. OE = ___. **Don't proceed to Step 1 until these are defined.**

See [`references/throughput-accounting.md`](references/throughput-accounting.md) for why cost accounting misleads and how T/I/OE rewires decisions.

---

## Step 1 — Identify the constraint *(Goldratt)*

**Frame:** "Find the *one* thing that, if relaxed, lets more T flow."

### Type the constraint *(Goldratt)*

The intervention differs by type — diagnose type before fixing.

- **Physical** — a machine, a person, a server. Find the *queue*; the constraint is the resource just downstream.
- **Policy** — a rule. "Every PR needs two reviewers." "No hire without VP approval." "QA can't be cross-trained." Find the rule everyone routes around or waits on.
- **Market** — demand is the constraint. You have excess capacity; the system is starving from outside. Different game: elevate by selling, not producing.
- **Paradigm** — the team *believes* something is the constraint that isn't. Surfaces when fixes don't move T. Needs the [Evaporating Cloud](references/evaporating-cloud.md).

**Diagnostic decision tree *(workflow)*:**
1. Is your output less than market demand? → physical or policy.
2. Is output greater than demand? → market.
3. Where does work pile up (longest queue / oldest WIP)? → constraint is the resource just downstream of the pile.
4. Does the same problem keep returning after each fix? → paradigm or policy. The "physical" diagnosis is wrong.

**The most common TOC failure:** diagnosing physical when the real constraint is policy. ("Our QA is the bottleneck" → real constraint is the *policy* that QA can't be cross-trained. Fix isn't more QAs; it's changing the staffing rule.)

See [`references/four-constraint-types.md`](references/four-constraint-types.md) for worked examples per type.

**Exit:** one sentence — "The constraint is X (type: physical / policy / market / paradigm). Evidence: [queue location / starvation pattern / re-occurring failure]."

---

## Step 2 — Exploit the constraint *(Goldratt)*

**Frame:** "Squeeze maximum throughput from the constraint *as it is*. No new investment yet."

The constraint is a precious resource; don't waste a minute of it. Common exploit moves:

- **Eliminate idle time at the constraint.** Cover lunch breaks, stagger shifts, ensure work is queued so it never starves.
- **Move non-constraint work off the constraint.** If your senior reviewer is the bottleneck, stop having them do work juniors could.
- **Fix constraint-side defects first.** A defect at the constraint costs system throughput; one upstream is much cheaper.
- **Quality-gate *before* the constraint, not after.** The constraint must never spend time on work that turns out to be unusable.
- **Reduce setup/changeover time at the constraint.** Smaller batches if changeover is fast; bigger batches if it isn't.

**Exit:** 2-5 named exploit moves with no new spending.

---

## Step 3 — Subordinate everything else *(Goldratt)*

**Frame:** "The rest of the system serves the constraint's pace. Non-constraint resources slow down or stop when needed — *and that's correct*."

This is where the **utilization fallacy** hits hardest: people resist the idea that non-constraint resources should sit idle some of the time. They will. Forcing them to be 100% utilized creates WIP piles upstream of the constraint, which makes throughput worse, not better.

Subordinate moves:
- **WIP limits upstream** — don't release work into the system faster than the constraint can absorb. (This is the Rope in DBR.)
- **Pull, not push** — downstream stages signal upstream when ready. Upstream doesn't push.
- **Re-task non-constraint resources** to support the constraint (preparing inputs, removing defects, reducing setup time at the constraint).
- **Accept idle time at non-constraints.** It's a feature, not a bug.

**Exit:** named subordinations — what stops, what slows, what re-routes to support the constraint.

---

## Step 4 — Elevate the constraint *(Goldratt)*

**Frame:** "Now invest. Buy capacity, hire, change the policy, expand the market — but only after exploit and subordinate."

Elevating before exploiting is the single most common TOC error. Most "we need to hire" diagnoses dissolve once the team actually exploits and subordinates first.

Elevation moves by type:
- **Physical:** add capacity (hire, buy machine, scale server).
- **Policy:** change the rule (cross-train, drop the approval gate, change the SLA).
- **Market:** invest in demand generation (sales, marketing, new segments).
- **Paradigm:** challenge the belief (Evaporating Cloud, surface assumption, run experiment).

**Exit:** one elevation plan with cost and expected T/I/OE delta.

---

## Step 5 — Repeat. Watch for inertia. *(Goldratt — and Goldratt's main warning)*

**Frame:** "When the constraint is broken, *the constraint moves*. The hardest part is recognizing it has."

After successful elevation, the constraint shifts to the next-weakest link. The new constraint is almost never where you expect. Two dangers:

- **Policies created to subordinate to the *old* constraint become the *new* constraint.** "We hold work back to feed QA" was right when QA was the bottleneck. After hiring, that policy now starves the new bottleneck.
- **Inertia.** Teams keep optimizing the old constraint after it's no longer binding. T plateaus; nobody knows why.

**Exit:** named "watch-for" — the candidate next constraint, and the policies from this round that may need to be rescinded next round.

---

## The Four Heresies — anti-pattern watchlist *(Goldratt)*

Detect these in user reasoning at any step. Name them and push back.

1. **Utilization fallacy** — "Everyone should be 100% busy." False. Non-constraint resources *must* have slack, or WIP piles up at the constraint.
2. **Local-optima fallacy** — "If every step gets cheaper/faster, the system gets better." False. Improvements at non-constraints are invisible to T.
3. **Balance-the-line fallacy** — "Capacity at every stage should be equal." False. TOC says deliberately *unbalance* the line so the constraint is obvious and protected.
4. **Busyness-as-progress fallacy** — "We worked hard, so we made progress." False. T is the only measure of progress; activity that doesn't move T is waste.

See [`references/four-heresies.md`](references/four-heresies.md) for detection patterns and how to call them out cleanly.

---

## Drum-Buffer-Rope — the operational pattern *(Goldratt)*

Once the constraint is identified, *run the system to it*:

- **Drum** — the constraint sets the pace. The whole system syncs to its rhythm.
- **Buffer** — a *time* buffer (not inventory) sits in front of the constraint. Protects it from upstream variability. The constraint must never starve.
- **Rope** — a signal pulling new work into the system at the constraint's rate. Prevents WIP buildup upstream.

**Translations *(workflow)*:**

| Domain | Drum | Buffer | Rope |
|---|---|---|---|
| Software | Slowest stage (often code review or QA) | Small ready-to-execute queue just before bottleneck | WIP limits upstream that throttle new work |
| Sales | Closer's capacity | Qualified-lead pool just before close | SDRs throttle prospecting when closer queue full |
| Personal | Deep-work hours | Small "ready-to-execute" queue | Stop accepting commitments when queue full |

The Rope is the key insight: **don't release work faster than the constraint can absorb.** It's what makes Kanban work; most Kanban users don't realize they're running half of DBR.

See [`references/drum-buffer-rope.md`](references/drum-buffer-rope.md) for deeper mechanics.

---

## Sidebar — Critical Chain (TOC for projects)

Manufacturing flow is repetitive; projects are one-shot. Goldratt's *Critical Chain* adapts TOC for projects. Three signature ideas:

1. **The constraint is the longest *resource-aware* dependency chain.** Not just task dependencies (the critical *path*) — path plus shared-resource conflicts. One person on two parallel branches means those branches aren't actually parallel.
2. **Strip per-task safety; pool it into a project buffer at the end.** Padded estimates get consumed (Parkinson's Law, student syndrome). Estimate aggressively (50%-likely), put a single shared buffer at the project end, manage the buffer.
3. **No multitasking on the critical chain.** Switching between projects multiplies elapsed time of all of them. The project-level utilization fallacy.

When the user is planning a one-shot project (vs. running a steady-state flow), prefer Critical Chain framing. See [`references/critical-chain.md`](references/critical-chain.md).

---

## Optional tool — Evaporating Cloud

When the user is stuck in a "we must do A *and* B but they conflict" deadlock, surface the Evaporating Cloud:

- **Common objective** both actions ultimately serve
- **Need behind A** and **need behind B** (each meets a real underlying requirement)
- **Conflicting actions** A vs. B
- **Hidden assumption** that makes A and B appear mutually exclusive
- **Resolution** — change the assumption, both needs met without the conflict

Surface this only when conflict is detected. Don't force every user through it. See [`references/evaporating-cloud.md`](references/evaporating-cloud.md) for the 5-box method with worked examples.

---

## Output — Constraint Diagnosis one-pager (the deliverable)

Assemble the conversation into this single block. This is what the user copy-pastes:

```
━━━ CONSTRAINT DIAGNOSIS ━━━

System: [one sentence]

Throughput (T):        [definition for this system]
Inventory (I):         [definition]
Operating Expense (OE):[definition]

THE CONSTRAINT
Type:           [physical / policy / market / paradigm]
Identification: [one sentence]
Evidence:       [where the queue is / starvation pattern / re-occurring failure]

EXPLOIT (no new investment)
• [Move 1]
• [Move 2]
• ...

SUBORDINATE (what the rest of the system stops doing)
• [Move 1]
• [Move 2]
• ...

ELEVATE (if needed, what to invest in)
• [Move + estimated cost + expected T/I/OE delta]

WATCH FOR (when the constraint moves)
• Next likely constraint: [where]
• Policies from this round to rescind: [list]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Tell the user: "Constraints move. Re-run this skill in 4-12 weeks (or whenever T plateaus) to find the new one."

---

## Rules

- **No intervention before identification.** If the user wants to skip Step 1, refuse — name what they're skipping.
- **T/I/OE must be defined before Step 1.** Don't proceed without them.
- **Type the constraint before exploiting.** Physical and policy interventions are different.
- **Exploit before elevating.** Most "we need to hire" dissolves once the user actually exploits.
- **Tag every move** as *(Goldratt)* or *(workflow)*.
- **Name the heresy when you see it.** "That's the utilization fallacy" beats vague "I'd reconsider."
- **Constraints move.** Always end with "watch for" — never close as if the work is permanent.

---

## Files

- `SKILL.md` — workflow spine, decision trees, exit criteria, output template
- `references/throughput-accounting.md` — T/I/OE deeper, why cost accounting misleads
- `references/four-constraint-types.md` — physical / policy / market / paradigm with worked examples
- `references/four-heresies.md` — anti-pattern detection patterns
- `references/drum-buffer-rope.md` — DBR mechanics with domain examples
- `references/critical-chain.md` — TOC for projects
- `references/evaporating-cloud.md` — the 5-box conflict-resolution method
- `sources.md` — book references

## Source

Based on the work of Eliyahu M. Goldratt — *The Goal* (1984), *It's Not Luck* (1994), *Critical Chain* (1997), and *Theory of Constraints* (1990). Operational rules tagged *(Goldratt)* are drawn from these sources; rules tagged *(workflow)* are this skill's operationalizations on top.
