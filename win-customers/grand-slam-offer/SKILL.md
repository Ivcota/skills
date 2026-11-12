---
name: grand-slam-offer
description: Walk through Alex Hormozi's $100M Offers workflow end-to-end to design a Grand Slam Offer from scratch — Dream Outcome → Problems → Solutions → Delivery Vehicles → Trim & Stack → Bonuses → Guarantee → Scarcity & Urgency → Pricing → Naming. Produces a complete Offer Card (named, priced, bonus-stacked, guaranteed, with scarcity copy) ready to drop into a sales page. Distinct from `hundred-million-offers` (reference skill) and `value-equation` (scores any artifact on four levers) — this is the build-an-offer workflow specifically. Use when the user says "build a grand slam offer", "design my offer", "package my offer", "create an irresistible offer", "build an offer from scratch", "walk me through making an offer", or wants to construct a complete offer with bonuses, guarantee, scarcity, and pricing in one guided pass.
---

# Grand Slam Offer

Build a complete offer the way the book builds it: ten steps, mini-interview per step, full Offer Card at the end.

Steps 1–5 are the book's numbered offer-creation sequence: Dream Outcome → Problems → Solutions → Delivery Vehicles → Trim & Stack. Steps 6–10 enhance that offer: Bonuses → Guarantee → Scarcity & Urgency → Pricing → Naming. Pricing is last *(workflow)* so the 10:1 ratio is set against the full stack.

**Output is conversation-only.** No file is saved. The Offer Card at the end is the deliverable — user copy-pastes it.

## Pace and shape

- **Mini-interview per step** — 2-4 targeted questions, not strict one-Q-at-a-time, not a single batched prompt.
- **Generation-heavy** — propose 2-5 concrete candidates, let the user react (kill / keep / edit / add). Don't ask open questions and wait.
- **Each step ends with an explicit exit** carried into the next step.
- **Backtracking allowed** — user can say "go back to Step N" any time. Replay forward from the edited state, don't restart.
- **Tag every move** *(book)* or *(workflow)*. Lets the user trust what's Hormozi vs what's an operationalization.

**Load `PATTERNS.md` once at intake.** Reference it during every step that requires generation (Dream Outcomes, problems, solutions, vehicles, trim quadrants, bonus names, guarantee phrasing, scarcity copy, MAGIC names, stack reveal). It contains book-faithful copy patterns, calibrating examples, and the canonical weight-loss exemplar threaded through every step.

**Pivot:** If the user says "value equation," "pull the levers," or "one lever at a time," stop this workflow. Carry only the ICP and the locked Dream Outcome into `value-equation`. Do not generate the next Grand Slam step. Resume here only when they say "back to Grand Slam step N."

## Intake (always, before Step 1)

Ask both:

1. **ICP** — "Who's this offer for? Be narrow — vertical, role, situation."
2. **Dream Outcome direction** — "What outcome do they want? (Rough; we sharpen in Step 1.)"

If user needs guidance selecting a market or ICP, reference `PATTERNS.md → Intake — ICP Selection` (three-market framework, sub-niche examples, three qualification gates), then proceed with whatever they bring. For deeper research, point to `validate-icp` or `jobs-to-be-done`. Never proceed silently with a generic ICP.

---

## Step 1 — Dream Outcome

**Frame:** "We pick the single Dream Outcome this offer is built around. One offer, one outcome."

1. **Hybrid candidate generation** — propose 5-8 candidate Dream Outcomes for the ICP. Each in the customer's words, concrete (not "more revenue" — "$30K MRR within 6 months"). User kills, edits, adds.
2. **Refine survivors** — 1-2 questions per kept candidate to sharpen specificity.
3. **Narrow to ONE.** *(book)* The whole offer hangs off this anchor. If user wants to explore alternates, re-run the skill.

**Exit:** one sentence — "The Dream Outcome is X."

---

## Step 2 — List Problems *(book Step #2)*

**Frame:** "We list every obstacle between [ICP] and [Dream Outcome] — chronologically by stage, tagged by which Value Equation lever each hits."

**Lever map** *(workflow — same four parts as `value-equation`)* — Value = (Dream Outcome × Likelihood) / (Time Delay × Effort & Sacrifice). Numerators should go up; denominators should go down toward 1.

| Tag | Lever | Problem sounds like | Solving it does |
|---|---|---|---|
| **DO** | Dream Outcome | result feels weak, vague, not *for me*, or not life-changing enough | raise the result |
| **L** | Likelihood | "won't work for someone like me" | raise the belief |
| **T** | Time Delay | "takes too long / no early win" | shrink the wait |
| **E&S** | Effort & Sacrifice | hard, confusing, costly, identity cost — money they give up lives here, not under DO | shrink the work |

1. **Stage proposal** — draft 4-7 chronological stages the customer goes through (e.g. for "land 10 clients": Identify ICP → Get attention → Book calls → Close calls → Deliver → Renew). User confirms / reorders / adds.
2. **Per-stage problem generation** — for each stage, draft 4-8 candidate problems, each auto-tagged with the lever map above. Multi-tagging allowed when a problem truly hits more than one lever. Do not file "too expensive" or other cost-to-buyer under **DO**.
3. **User reacts** — kill / keep / edit / add per stage.
4. **Volume target: ~20-40 problems total.** *(workflow — book targets 32-64; chat compresses.)* If a stage has fewer than 3, push for more. If a stage is missing a lever, draft at least one problem for that lever.

**Exit:** structured problem list — grouped by stage, each tagged with lever(s). Tags carry into Steps 3–6 so solutions, vehicles, trim, and bonuses pull the right lever.

---

## Step 3 — Solutions List *(book Step #3)*

**Frame:** "We flip every problem into a 'How to...' solution that pulls its tagged lever, dedupe, then name each."

1. **Auto-flip** *(book — "copywriting 101")* — mechanically convert every Step 2 problem into "How to [reverse]" form. Keep the lever tag on each flip. Show the full list grouped by stage. Load `PATTERNS.md → Step 3` for lever-specific flip templates.
2. **User review** — strike bad ones, edit language, add missing.
3. **Dedupe pass** *(workflow)* — flag near-duplicates, propose merges, user approves each. *(Book says repetition is normal; we dedupe because Step 4 writes a vehicle list per solution, and near-duplicates multiply that list.)* Prefer the merge that still names the lever the survivor pulls.
4. **Name each surviving solution** *(book)* — propose short specific names (benefit + ideally avatar/timeframe). User edits.

**Exit:** named, deduped "How to..." solution list, each linked to the original problem(s) and lever tag(s).

---

## Step 4 — Delivery Vehicles *(book Step #4 — "The How")*

**Frame:** "For every solution, list everything you could possibly deliver. This is what they get in exchange for money. Divergent first. Whether you would actually do it is not the filter. The filter is whether they would say: all that? Seriously? Yes, I'm in."

1. **Delivery cheat codes** *(book — the Delivery Cube)* — vary each solution across all six:
   - **Attention:** one-on-one / small group / one-to-many
   - **Effort:** DIY / done-with-you / done-for-you
   - **Live medium:** in person / phone / email / text / Zoom / chat
   - **Recorded consumption:** audio / video / written
   - **Reply speed:** 24/7 / business hours / within 5 minutes / within an hour / within 24 hours
   - **10× / 1/10th:** what you would deliver if they paid 10× (or $100,000); what would still make them successful at 1/10th the price
2. **Per-solution generation** *(book)* — group each list by attention level, the way the grocery example does: one-on-one, then small group, then one-to-many. Cover more than one effort level. Include at least one 10× idea and one 1/10th idea. Bias vehicle ideas toward the solution's lever tag *(workflow)*: **DO** → vivid outcome proof and identity-level framing; **L** → hand-holding, proof, live support; **T** → faster reply, first-win formats, done-for-you speed; **E&S** → DIY tools that remove decisions, DWY coaching, or DFY. Load `PATTERNS.md → Step 4` for the grocery exemplar before generating. Chat compresses *(workflow)*: draft 6–10 vehicles per solution. If a solution only varies format inside one attention level, push for the other levels.
3. **User reacts** — kill / keep / edit / add. Cost is not a reason to kill yet. Trimming is Step 5.
4. **Solve every perceived problem** *(book)* — one unsolved problem is often why someone doesn't buy. If a Step 3 solution has no vehicles, add them before exiting.

**Exit:** untrimmed vehicle list, grouped by solution and attention level. Carried into Step 5.

---

## Step 5 — Trim & Stack *(book Step #5)*

**Frame:** "Now we trim. High value to them, lower cost to you. Over-deliver at first to create cash flow, then build systems that create the same value for less. The piece that makes them say yes stays, even when it costs more to deliver."

1. **Score each kept vehicle** *(book — qualitative, axis chart not numeric)* — Value to customer (Low/Med/High) × Cost to deliver (Low/Med/High). Value is high when the vehicle clearly pulls its tagged lever (bigger result, stronger belief, shorter wait, or less work).
2. **Categorize** *(workflow refinement of the book's high-value/low-cost trim)*:
   - **CUT** = High Cost + Low Value
   - **CORE (keep)** = High Value + Low Cost
   - **ANCHOR (keep)** = High Value + High Cost — the headline component, justifies price
   - **DEMOTE** = Low Value + Low Cost — bonus candidate or cut
3. **Sales-fulfillment check** *(book)* — for each ANCHOR, ask whether a system could deliver the same customer value at lower cost later. Keep the value now. Note the later system as an ops note, not a reason to cut the promise.
4. User confirms each call. One vehicle, or a deliberate combination, per solution that stays.

**Exit:** offer stack — solution+vehicle pairs categorized as Anchor / Core / Demote / Cut. Carry the kept pieces forward whole. Step 6 breaks that stack apart into bonuses; demoted items are a later bonus source only when they kill an objection.

---

## Step 6 — Bonuses *(book Section IV)*

**Frame:** "A single offer is worth less than the same offer broken into its parts and stacked as bonuses. We anchor the price on one core. Every other piece they already get gets its own name, its own price, and a 'but wait.' Then we add whatever still kills the reason they would say no. Close a price gap by adding a bonus. The core price stays put."

Load `PATTERNS.md → Step 6` before generating names or the breakout.

1. **Splinter the stack** *(book — products and services already inside the offer, broken out and stacked)*. Take the kept Anchor + Core deliverables from Step 5. Pick one price-anchor core, usually the headline vehicle. Break every other kept deliverable into its own bonus. Each piece was already in the offer; naming it and pricing it is what makes it visible. Propose the breakout in one pass: what stays the core, and each splinter with a benefit-first name plus the problem it was already solving. User kills / keeps / edits the *presentation*. A splinter still ships. You are changing how it is shown, not whether they receive it.
2. **Next logical need** *(book)* — 1-2 bonuses for the problem they hit the moment the Dream Outcome arrives, before they know to ask. These are new pieces, beyond the splinter.
3. **Recycle DEMOTED items from Step 5** *(workflow)* — propose one only when it maps to a real objection. Reframe it as an objection-killer. Tag the lever it kills (**L** and **E&S** are the usual ones; **T** for "I'll start later"; **DO** only when the result still feels too small).
4. **Identify remaining objections** *(workflow Q's, book intent)* — 3 questions:
   - "#1 reason a fit prospect would still hesitate?"
   - "Most common 'but what about...' question?"
   - "Closest-to-the-line objection — fix it and they'd buy today?"
   Map each answer to a lever before generating. Skip an objection a splinter or next-need bonus already kills.
5. **Generate one added bonus per remaining objection.** **Prefer tools / checklists / templates / swipe files over more training content.** *(book)* Tools and checklists beat another training because effort and time drop, so perceived value rises.
6. **Partner-bonus nudge** *(book)* — single ask: "Any adjacent business whose product you could include at zero cost, in exchange for sending them customers?" High-value to the buyer, free to you. Direct competitors stay out.
7. **Name each bonus** *(book)* — benefit in the title, ideally avatar + timeframe (e.g., "The 6-Week Six-Pack Bootcamp for Busy Men"). A splinter sheds its internal label ("weekly group call" becomes a named bonus). Length serves clarity, not a fixed cap.
8. **Capture pitch elements per bonus** *(book — Hormozi's bonus-pitch rules)*:
   - How it relates to their issue (the objection or obstacle it kills)
   - What it is
   - How you discovered or created it — for a splinter, the story is that this was buried inside the offer until it was pulled out and named
   - How it improves their life (vivid future picture: faster, easier, or less sacrifice)
   - Proof point (stat / past client / personal experience) — if available
   - The dollar value, and why that number is fair
9. **Assign a dollar value to every bonus, justify it, round down** *(book — "undervalue rather than overvalue")*. The rule is honest and defensible. Sum of bonus values eclipses the stated value of the price-anchor core *(book)*.
10. **Optional bonus-level scarcity or urgency** *(book)* — scarcity: only people who buy get a piece that exists nowhere else, or the last N seats of something real. Urgency: the bonus arrives only if they buy today. "Any bonus worth limiting on its own?" Confirm the limit is real. Step 8 still owns offer-level scarcity.
11. **Stack order** — state the core and its price first, then expand *(book — price anchor, then "but wait")*. Within the bonuses, value-descending *(workflow)*. User can reorder for the story.
12. **Volume** — every kept deliverable outside the core is broken out. Added bonuses cover the objections that breakout left standing. No fixed count.
13. **One-to-one reveal** *(book)* — on a sales call, ask for the sale on the core first. If they say yes, reveal the bonuses after the yes. If they say no, bring the one bonus that matches the obstacle they just named, then ask again.

**Exit:** ordered bonus list. Each row tagged `splinter`, `next need`, `demoted`, `tool`, or `partner`, with objection + description + discovery story + future picture + proof + dollar value. Total bonus value summed, and greater than the core's stated value.

---

## Step 7 — Guarantee *(book Section IV)*

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

## Step 8 — Scarcity & Urgency *(book Section IV)*

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

## Step 9 — Pricing *(re-ordered: book treats pricing as upfront mindset; we price last because the 10:1 ratio needs full stack value)*

**Frame:** "Now the full stack is built. We price against total perceived value. Target 10:1 — perceived value 10x your price."

1. **Compute total stack value** — count each deliverable once. Price-anchor core value + every Step 6 bonus (splintered components and added bonuses). Display: "Total stack value: $X." A piece moved into bonuses in Step 6 is already inside that bonus total. Guarantee + scarcity boost perceived value but aren't summed.
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
   Core: [Price-anchor] — $X value
   Bonus 1: [Splintered piece or added bonus] — $X value
   Bonus 2: [Splintered piece or added bonus] — $X value
   ...
   Guarantee: [Named Guarantee]
   ─────────────
   Total value: $X
   Your investment today: $Y
   ```

**Exit:** price + payment structure + stack reveal copy.

---

## Step 10 — Naming + Final Offer Card *(book Section IV — MAGIC)*

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

Assemble everything into a single block. THE STACK is the price-anchor core only. Pieces broken out in Step 6 sit under BONUSES and are counted once. This is what the user copy-pastes:

```
━━━ GRAND SLAM OFFER ━━━

Name: [Final name]
For: [ICP]
Promise: [Dream Outcome]

THE STACK
• [Price-anchor core] — $X

BONUSES
• [Named piece broken out of the offer] — $X — kills [objection]
• [Added bonus] — $X — kills [objection]
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
[Sales-page block from Step 9]
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
