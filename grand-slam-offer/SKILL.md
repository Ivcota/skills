---
name: grand-slam-offer
description: Walk through Alex Hormozi's $100M Offers workflow end-to-end to design a Grand Slam Offer from scratch — Dream Outcome → Problems → Solutions → Trim & Stack → Bonuses → Guarantee → Scarcity & Urgency → Pricing → Naming. Produces a complete Offer Card (named, priced, bonus-stacked, guaranteed, with scarcity copy) ready to drop into a sales page. Distinct from `hundred-million-offers` (reference skill) and `value-equation` (scores any artifact on four levers) — this is the build-an-offer workflow specifically. Use when the user says "build a grand slam offer", "design my offer", "package my offer", "create an irresistible offer", "build an offer from scratch", "walk me through making an offer", or wants to construct a complete offer with bonuses, guarantee, scarcity, and pricing in one guided pass.
---

# Grand Slam Offer

Build a complete offer the way the book builds it: nine steps, in book order, mini-interview per step, full Offer Card at the end.

**Output is conversation-only.** No file is saved. The Offer Card at the end is the deliverable — user copy-pastes it.

## Pace and shape

- **Mini-interview per step** — 2-4 targeted questions, not strict one-Q-at-a-time, not a single batched prompt.
- **Generation-heavy** — propose 2-5 concrete candidates, let the user react (kill / keep / edit / add). Don't ask open questions and wait.
- **Each step ends with an explicit exit** carried into the next step.
- **Backtracking allowed** — user can say "go back to Step N" any time. Replay forward from the edited state, don't restart.
- **Tag every move** *(book)* or *(workflow)*. Lets the user trust what's Hormozi vs what's an operationalization.

**Load `PATTERNS.md` once at intake.** Reference it during every step that requires generation (Dream Outcomes, problems, solutions, vehicles, bonus names, guarantee phrasing, scarcity copy, MAGIC names, stack reveal). It contains book-faithful copy patterns, calibrating examples, and the canonical weight-loss exemplar threaded across Steps 2-5.

## Intake (always, before Step 1)

Ask both:

1. **ICP** — "Who's this offer for? Be narrow — vertical, role, situation."
2. **Dream Outcome direction** — "What outcome do they want? (Rough; we sharpen in Step 1.)"

If user has no ICP, point to `validate-icp` or `jobs-to-be-done`, then proceed with whatever they bring. Never proceed silently with a generic ICP.

---

## Step 1 — Dream Outcome

**Frame:** "We pick the single Dream Outcome this offer is built around. One offer, one outcome."

1. **Hybrid candidate generation** — propose 5-8 candidate Dream Outcomes for the ICP. Each in the customer's words, concrete (not "more revenue" — "$30K MRR within 6 months"). User kills, edits, adds.
2. **Refine survivors** — 1-2 questions per kept candidate to sharpen specificity.
3. **Narrow to ONE.** *(book)* The whole offer hangs off this anchor. If user wants to explore alternates, re-run the skill.

**Exit:** one sentence — "The Dream Outcome is X."

---

## Step 2 — List Problems *(book Step #2)*

**Frame:** "We list every obstacle between [ICP] and [Dream Outcome] — chronologically by stage, tagged by which of the 4 value drivers each hits."

1. **Stage proposal** — draft 4-7 chronological stages the customer goes through (e.g. for "land 10 clients": Identify ICP → Get attention → Book calls → Close calls → Deliver → Renew). User confirms / reorders / adds.
2. **Per-stage problem generation** — for each stage, draft 4-8 candidate problems, each auto-tagged by value driver: **DO** (Dream Outcome — won't be worth it), **L** (Likelihood — won't work for me), **E&S** (Effort & Sacrifice — too hard, confusing), **T** (Time — too long). Multi-tagging allowed.
3. **User reacts** — kill / keep / edit / add per stage.
4. **Volume target: ~20-40 problems total.** *(workflow — book targets 32-64; chat compresses.)* If a stage has fewer than 3, push for more.

**Exit:** structured problem list — grouped by stage, each tagged with value driver(s). Carried into Step 3.

---

## Step 3 — Solutions List *(book Step #3)*

**Frame:** "We flip every problem into a 'How to...' solution, dedupe, then name each."

1. **Auto-flip** *(book — "copywriting 101")* — mechanically convert every Step 2 problem into "How to [reverse]" form. Show the full list grouped by stage.
2. **User review** — strike bad ones, edit language, add missing.
3. **Dedupe pass** *(workflow)* — flag near-duplicates, propose merges, user approves each. *(Book says repetition is normal; we dedupe because Step 4 needs clean state.)*
4. **Name each surviving solution** *(book)* — propose short specific names (benefit + ideally avatar/timeframe). User edits.

**Exit:** named, deduped "How to..." solution list, each linked to the original problem(s).

---

## Step 4 — Trim & Stack *(book Step #4)*

**Frame:** "Each solution can be delivered many ways. We pick a vehicle for each, score Value × Cost, and trim what's expensive and low-value."

1. **Vehicle dimensions cheat-sheet:**
   - **Attention:** 1-on-1 / small group / 1-to-many
   - **Effort:** DIY / done-with-you / done-for-you
   - **Format:** live / recorded / written / software / physical
   - **Speed:** sync / async / on-demand
   *(User can mix.)*
2. **Vehicle proposal** — draft 2-3 candidate vehicles per solution, user picks one (or combines).
3. **Quick qualitative score** *(book — Hormozi is qualitative here, axis chart not numeric)* — Value to customer (Low/Med/High) × Cost to deliver (Low/Med/High).
4. **Categorize** *(workflow refinement of book's two buckets)*:
   - **CUT** = High Cost + Low Value
   - **CORE (keep)** = High Value + Low Cost
   - **ANCHOR (keep)** = High Value + High Cost — the headline component, justifies price
   - **DEMOTE** = Low Value + Low Cost — bonus candidate or cut
5. User confirms each call.

**Exit:** offer stack — solution+vehicle pairs categorized as Anchor / Core / Demote / Cut. Carry forward.

---

## Step 5 — Bonuses *(book Section IV)*

**Frame:** "Each bonus targets a specific objection, has a unique name, a justified price, and proof. Total bonus value > eventual core price."

1. **Recycle DEMOTED items from Step 4** *(workflow)* — propose as bonus candidates, but only if they map to a real objection. Reframe each as objection-killer.
2. **Identify remaining objections** *(workflow Q's, book intent)* — 3 questions:
   - "#1 reason a fit prospect would still hesitate?"
   - "Most common 'but what about...' question?"
   - "Closest-to-the-line objection — fix it and they'd buy today?"
3. **Generate bonus candidates per objection** — 1-2 each. **Prefer tools / checklists / templates / swipe files over more training content.** *(book — explicit Hormozi rule.)*
4. **Partner-bonus nudge** *(book)* — single ask: "Any partner whose product you could include at zero cost?"
5. **Name each bonus** *(book)* — pattern: include the benefit, ideally avatar + timeframe (e.g., "The 6-Week Six-Pack Bootcamp for Busy Men"). Length serves clarity, not a fixed cap.
6. **Capture pitch elements per bonus** *(book — Hormozi's literal bonus-pitch rules)*:
   - Objection it kills
   - What it is
   - How you discovered/created it
   - How it improves their life (vivid future picture)
   - Proof point (stat / case study / anecdote) — if available
7. **Assign dollar value, justify it, round down** *(book — "undervalue rather than overvalue")*. No 3x cap; the rule is honest and defensible.
8. **Optional bonus-level scarcity** *(book)* — "Any bonus worth limiting separately? (e.g., first 20 enrollees only.)"
9. **Stack order** — value-descending by default *(workflow)*. User can reorder for narrative.
10. **Volume** — enough to neutralize key objections, typically 3-7. No hard count.

**Exit:** named bonus list, each with objection + description + discovery story + future picture + proof + dollar value, ordered, total value summed.

---

## Step 6 — Guarantee *(book Section IV)*

**Frame:** "Pick a guarantee that fits, name it, make it specific and bold — not vague."

1. **Show the 5 types** *(book)*:
   - **Unconditional** — full refund, no questions (low-ticket)
   - **Conditional** — "Do X, if it doesn't work, refund" (better-fit clients)
   - **Anti-guarantee** — "All sales final" (when demand >> supply, brand strong)
   - **Performance-based** — "We hit [metric] or you don't pay" (ultimate risk reversal)
   - **Stacked** — combine 2+ above
2. **Decision interview** *(workflow)* — 3 questions:
   - Price tier? (sub-$500 → unconditional; $500-5K → conditional; $5K+ → performance/stacked)
   - Result objectively measurable? (yes → performance on the table)
   - Refund tolerance? (high → unconditional; low → conditional with action requirements)
   Recommend a type; user can override.
3. **Generate 2-3 specific candidates** of the chosen type — fitted to user's offer + Dream Outcome.
4. **Specificity check** *(book)* — "money-back" is weak; "Full refund + we pay you $500 for your time" is strong. Push for dollar-figures or measurable metrics. Reject vague.
5. **Name it** *(book)* — e.g., "The 10 Clients in 90 Days Guarantee."
6. **Stack option** *(book)* — "Want to stack — e.g., unconditional 30-day + performance-based at 90?"
7. **Honor-it gate** *(workflow placement of book's ethics)* — user explicitly commits: "Will you honor this with zero friction and no fine print? If not, weaken it."

**Exit:** named guarantee with type tagged, specific terms, commitment-to-honor recorded.

---

## Step 7 — Scarcity & Urgency *(book Section IV)*

**Frame:** "Scarcity = limited quantity. Urgency = limited time. Pair both. Every claim must be true."

1. **Scarcity types** *(book)*: Capacity / Bonus / Tier (founding pricing).
2. **Urgency types** *(book)*: Cohort window / Pricing change / Fast-action bonus / Event-tied.
3. **Combine — 2 questions** *(workflow)*:
   - "Cohort or continuous enrollment?"
   - "Real recurring deadline (price change, season, cohort start)?"
   Recommend a combo.
4. **Generate 2 specific candidates** — fitted copy (e.g., "Only 20 seats per cohort. Next cohort March 15. Enroll by March 1 for founding pricing — $2,500 vs $4,000 after.").
5. **Authenticity gate** *(workflow placement of book's ethics)* — explicit user commitment: "If you say 20 spots, there are 20. Confirm every claim is real."
6. **Anti-pattern hard-reject** *(workflow enforcement of book ethics)* — refuse to generate: countdown timers that reset, evergreen "limited time" with no real end, fake "spots left" with unlimited supply.

**Exit:** one scarcity claim + one urgency claim, both authentic, both tied to a real mechanism.

---

## Step 8 — Pricing *(re-ordered: book treats pricing as upfront mindset; we price last because the 10:1 ratio needs full stack value)*

**Frame:** "Now the full stack is built. We price against total perceived value. Target 10:1 — perceived value 10x your price."

1. **Compute total stack value** — auto-sum: core component values (Step 4) + bonus values (Step 5). Display: "Total stack value: $X." Guarantee + scarcity boost perceived value but aren't summed.
2. **Three anchors** *(book references all three)*:
   - **Stack anchor:** total stack ÷ 10
   - **Status-quo anchor:** cost of doing nothing for 12 months
   - **Alternative anchor:** total cost of partial solutions over 12 months
   Display as a price corridor *(workflow framing)*.
3. **Three-tier price proposal** *(workflow)*:
   - **Premium** (~10% of stack) — book default
   - **Stretch** (~15-20%) — if guarantee + bonuses are exceptionally strong
   - **Floor** (~5-7%) — only for demand testing or low-trust markets
4. **Market ceiling check** *(workflow)* — "Highest comparable in your market?" If recommendation exceeds it, ask: "Hold premium positioning above market, or anchor at ceiling?"
5. **Payment structure** *(book)* — if price ≥ $2K, prompt PIF vs payment plan + PIF discount. Below, default PIF.
6. **Generate stack reveal copy** *(book — pattern straight from Hormozi's worked examples)*:
   ```
   Core: [Component] — $X value
   Bonus 1: [Name] — $X value
   Bonus 2: [Name] — $X value
   ...
   Guarantee: [Named Guarantee]
   ─────────────
   Total value: $X
   Your investment today: $Y
   ```

**Exit:** price + payment structure + stack reveal copy.

---

## Step 9 — Naming + Final Offer Card *(book Section IV — MAGIC)*

**Frame:** "The name does the selling. Use MAGIC. Test variations."

1. **MAGIC formula** *(book)*: **M**agnetic reason why · **A**vatar · **G**oal · **I**ndicate timeframe · **C**ontainer (Blueprint · Accelerator · Bootcamp · Masterclass · System · Formula · Challenge · Method · Playbook).
2. **Auto-populate from prior steps** *(workflow)* — Avatar = ICP, Goal = Dream Outcome, Indicate = timeframe from Step 1.
3. **Generate 5 candidate names** *(book — "test 3-5 variations")* — each using a different MAGIC composition. Show MAGIC element breakdown for each.
4. **Three guardrail checks** *(book)*:
   - **Generic:** "Could this describe any other offer in your space?" → kill if yes.
   - **Promise (ethics):** "Does this accurately represent typical results, not just aspirational?"
   - **Memorability:** "Read once. Now without looking — what does this offer do?" → unclear, rework.
5. **User picks one final name.** Locked.

### Final Offer Card (the deliverable)

Assemble everything into a single block. This is what the user copy-pastes:

```
━━━ GRAND SLAM OFFER ━━━

Name: [Final name]
For: [ICP]
Promise: [Dream Outcome]

THE STACK
• [Anchor component] — $X
• [Core component] — $X
• [Core component] — $X

BONUSES
• [Bonus 1 name] — $X — kills [objection]
• [Bonus 2 name] — $X — kills [objection]
• ...

GUARANTEE
[Named guarantee + specific terms]

SCARCITY & URGENCY
[Specific quantity claim] / [Specific deadline]

─────────────
Total value: $X
Your investment: $Y
Payment: [PIF or plan]

STACK REVEAL COPY
[Sales-page block from Step 8]
━━━━━━━━━━━━━━━━━
```

Tell the user: "Copy this card to your sales page or pitch. To audit it later, run `value-equation` Evaluate against the four levers."

---

## Rules

- **One offer, one Dream Outcome.** Don't carry multiples through. If user wants alternates, re-run.
- **Tag every move** as *(book)* or *(workflow)* so the user knows what's Hormozi vs operationalization.
- **Generation-heavy.** Propose concrete candidates; don't ask open questions and wait.
- **Authenticity gates are hard checkpoints**, not advisory. Refuse to generate fake-scarcity copy.
- **Honest dollar values, round down.** Reject inflated bonus values. The rule is defensibility, not a multiplier cap.
- **Specificity over vagueness** — guarantees, scarcity, names. "Money-back" is weak; "$500 for your time + full refund" is strong.
- **Backtracking is fine.** "Go back to Step 3" replays forward from the edit. Don't restart.
- **Conversation-only.** No file save. The Offer Card is the deliverable.

## Files

- `SKILL.md` — workflow, rules, decision trees, exit criteria
- `PATTERNS.md` — book-faithful copy patterns, calibrating examples (weight-loss exemplar), MAGIC name bank, guarantee phrasing, stack reveal templates

## Source

Based on *$100M Offers: How to Make Offers So Good People Feel Stupid Saying No* by Alex Hormozi. All operational rules tagged *(book)* are drawn directly from the source; rules tagged *(workflow)* are this skill's operationalizations on top.
