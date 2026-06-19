---
name: value-equation
description: Apply Hormozi's Value Equation as a thinking tool to evaluate or create high-value artifacts of any kind — offers, content (video/essay/post/talk), product features, or ideas. Two modes. Evaluate scores an existing artifact against the four levers (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort & Sacrifice), finds the weakest lever, and produces a concrete path to 10/10. Create runs a lever-by-lever design interview that produces a saved brief at ./value-equation-briefs/<slug>.md with operational sections on top and a projected composite below. Use when the user says "audit my offer", "rate this offer", "value equation", "is this a good offer/video/feature/idea", "why isn't this working", "path to 10/10", "make this 10/10", "design something high-value", "value-audit this video", "score this idea", "what's weak about my [thing]", or wants to diagnose weak spots in or design from scratch a product, package, feature, video, essay, or concept.
---

# Value Equation

Two modes, four artifact types, one set of levers.

**Levers (Hormozi):**
1. **Dream Outcome** — the end state the audience wants
2. **Perceived Likelihood of Achievement** — confidence *they specifically* will get it
3. **Time Delay** — gap between commit and first/full result (higher score = faster)
4. **Effort & Sacrifice** — what they must do/learn/endure/give up (higher score = easier)

**Composite formula:** `(Dream × Likelihood) / ((11 - Time Delay) × (11 - Effort))`. Perfect = 100.

## Workflow

### Step 1 — Intake (always two questions, in order)

Ask both before doing anything else. Do not assume.

1. **Mode** — "Are we evaluating something that exists, or designing something new?"
2. **Type** — "What type — offer, content, feature, or idea?"
   - **offer**: paid product/service/package/course/coaching
   - **content**: video, essay, post, talk, thread, podcast
   - **feature**: UX flow, capability, tool, or component inside a product
   - **idea**: concept/strategy/pitch/hypothesis/framework before it has form

If the artifact straddles types, pick the closest and proceed. Load `RUBRICS.md` and `PATHS.md` once mode and type are known.

Then branch.

---

## EVALUATE mode

### E1 — Intake the artifact (5 questions, type-tuned)

Push once for specifics if vague (Mom-Test style — concrete past instances, not hypotheticals). Do not fill gaps silently.

**If OFFER:** what is it / who for / what they get / what they pay / what proof exists.
**If CONTENT:** subject + format / target reader-viewer / promise (what they walk away with) / length and structure / hook + proof + pattern interrupt.
**If FEATURE:** what it does / who uses it and when in their workflow / outcome it produces / how invoked and completed / evidence it works (data, metrics, before/after).
**If IDEA:** the concept in one sentence / who would adopt it / what changes if it works / smallest test that would validate it / what adjacent precedents exist.

### E2 — Score each lever 1-10

Load `RUBRICS.md`. For each lever:

- Quote the rubric band the artifact lands in
- Cite the specific intake evidence that justifies the score
- Give a single integer 1-10

Use the type's calibrating examples in RUBRICS.md as anchors. Be honest. If you can't justify a score from evidence, score lower and say what evidence would raise it.

**Caps:**
- Pre-launch / no audience yet: Perceived Likelihood caps at 4
- Idea-mode artifacts (no users): Likelihood judged on adjacent precedent; caps at 5

### E3 — Compute composite

`(Dream × Likelihood) / ((11 - Time Delay) × (11 - Effort))`

Show the math. Interpret using the bands in RUBRICS.md (Grand Slam / Strong / Average / Weak).

### E4 — Identify the weakest lever

Largest gap to 10. On ties, pick a denominator (Time Delay or Effort) — denominators have outsized impact.

State plainly: "Your weakest lever is X at Y/10. Moving it to 10 raises composite from A to B."

### E5 — Path to 10/10

Load `PATHS.md`. Build a tailored ladder for the weakest lever:

- **Current state**: score + why
- **Next rung** (one up): smallest change that moves it
- **Each subsequent rung** to 10: concrete tactic, rough effort, expected lift
- **First action this week**: one thing doable in 7 days

Brief ladder for the second-weakest lever after.

### E6 — Re-score projection

"Today: X. After Week 1 actions: Y. After full path to 10 on weakest lever: Z."

### Evaluate output (chat report)

In this order:

1. **Artifact summary** (2-3 lines, in their words)
2. **Scores** (table: lever / score / rubric band / evidence)
3. **Composite** (math + band)
4. **Weakest lever diagnosis**
5. **Path to 10/10** (full ladder weakest, brief for second)
6. **This week** (one concrete action)
7. **Projected composite**

Tight. Diagnosis and a move, not a lecture.

---

## CREATE mode

### C1 — Intake the seed (3 questions)

1. **Subject/goal** — what's the rough thing you want to make?
2. **Audience** — who is it for?
3. **Constraints** — time / effort / format / channel envelope

### C2 — Lever-by-lever design interview

Walk the four levers in order: **Dream → Likelihood → Time Delay → Effort**. For each, do not skim past — make the user lock in a design choice before moving on.

For each lever:

1. Quote the rubric: what does 9-10 look like for *this artifact type* (use type anchors in RUBRICS.md)
2. Offer **2-3 candidate moves** drawn from PATHS.md, tuned to the artifact type. Make them concrete, not abstract.
3. Ask the user to pick, edit, or propose their own
4. Lock in the design choice with a target score

This is generative, not interrogative. You should be suggesting moves the user can react to, not asking open questions and waiting.

### C3 — Draft the brief

Save to `./value-equation-briefs/<slug>.md` (slug from subject/goal, kebab-case). Structure:

```markdown
# <Title>

> <One-line promise>

## Operational

**Goal** — what success looks like, concretely
**Audience** — who, in their voice
**Promise** — the one-line dream outcome they walk away with
**Hook** — first 3-10 seconds / opening line / first interaction
**Structure** — outline, spec, or build steps
**Distribution / Placement** — where it lives, how it reaches them

## Lever Rationale

### Dream Outcome — target N/10
- Design move: <chosen tactic>
- Why this hits: <evidence/principle>

### Perceived Likelihood — target N/10
- Design move: <chosen tactic>
- Why this hits: <evidence/principle>

### Time Delay — target N/10
- Design move: <chosen tactic>
- Why this hits: <evidence/principle>

### Effort & Sacrifice — target N/10
- Design move: <chosen tactic>
- Why this hits: <evidence/principle>

## Projected Composite

(<Dream> × <Likelihood>) / ((11 - <TimeDelay>) × (11 - <Effort>)) = **<value>** — <band>

**Weakest projected lever:** <lever> at <N>/10. If under-delivered, drops composite to <X>.

## First Build Action

<one thing, ≤5 hours, visible artifact, advances exactly one lever>
```

### C4 — Confirm save

Print the path. Tell the user they can run **evaluate mode** on the eventual artifact and compare to the projected composite.

---

## Rules

- Never score without cited evidence from intake.
- Never skip intake — guessing produces a worthless audit or vague brief.
- In create mode, force one lever at a time. Don't let the user skim past a lever without a locked decision.
- Path/design moves must be concrete (specific tactics, not "improve the marketing").
- If the user pushes back on a score, ask what evidence would justify higher; do not capitulate.
- The "this week" action must take ≤5 hours, produce a visible artifact, and move exactly one lever exactly one rung.

## References

- [RUBRICS.md](RUBRICS.md) — universal lever bands + type-tagged calibrating examples + composite interpretation
- [PATHS.md](PATHS.md) — universal 1→10 ladders for each lever + per-type anchor moves
