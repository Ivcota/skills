# Scoring Rubrics

Universal 1-10 bands for each lever. Cite evidence from intake to justify the score. Use the **Calibrating examples by type** at the bottom to translate the bands into the user's specific artifact.

## Lever 1: Dream Outcome

The end state the audience wants. Bigger, more specific, more emotional, more identity-relevant = higher score.

| Score | Description |
|-------|-------------|
| 1-2 | Vague, generic, low emotional charge |
| 3-4 | Somewhat specific, moderate desire |
| 5-6 | Specific and desirable, but common |
| 7-8 | Highly specific, emotionally charged, quantified or vividly named |
| 9-10 | Life-changing, deeply emotional, identity-shifting, uniquely articulated |

## Lever 2: Perceived Likelihood of Achievement

How confident the audience is that *they specifically* will get the result. Proof, named system, guarantees, track record = higher score.

| Score | Description |
|-------|-------------|
| 1-2 | No proof, no system, no precedent |
| 3-4 | Thin proof or vague process |
| 5-6 | Solid proof + clear methodology |
| 7-8 | Extensive proof, named system, partial guarantee or track record |
| 9-10 | Overwhelming proof, performance guarantee, public metrics |

## Lever 3: Time Delay (higher = faster)

Gap between commit (purchase / press play / start using) and first/full result. Score is inverted so 10 = immediate. When computing composite, use `(11 - score)` as the denominator weight.

| Score | Description |
|-------|-------------|
| 1-2 | Long delay, no early signals |
| 3-4 | Slow, faint quick wins |
| 5-6 | Moderate, with clear milestones |
| 7-8 | Fast first win, full result soon after |
| 9-10 | Immediate or same-session result |

## Lever 4: Effort & Sacrifice (higher = easier)

Everything the user must do, learn, endure, or give up — including cognitive load and identity cost. Score is inverted so 10 = zero effort. When computing composite, use `(11 - score)` as the denominator weight.

| Score | Description |
|-------|-------------|
| 1-2 | High effort, steep curve, major sacrifice |
| 3-4 | Significant effort, some hand-holding |
| 5-6 | Moderate effort, clear instructions, some automation |
| 7-8 | Low effort, mostly done-for-them |
| 9-10 | Zero effort, fully done-for-them, no sacrifice |

## Composite

**Formula:** `(Dream × Likelihood) / ((11 - Time Delay) × (11 - Effort))`

Perfect: (10 × 10) / (1 × 1) = **100**.
Poor: (2 × 2) / (9 × 9) ≈ **0.05**.

| Composite | Band | Meaning |
|-----------|------|---------|
| 50-100 | **Grand Slam** | Premium pricing/attention/adoption justified. Focus on distribution, not the artifact. |
| 20-49 | **Strong** | Good. One or two levers worth optimizing. |
| 5-19 | **Average** | Multiple levers need work. Likely to compete on price/attention. |
| Below 5 | **Weak** | Fundamental redesign needed before more spend or distribution. |

## Diagnosis rules

- **Weakest lever** = largest gap to 10.
- On ties, pick a **denominator** (Time Delay or Effort) — denominators have outsized impact on the composite.
- **Dream Outcome below 5** = nothing else matters until the "what" is clear.
- **Perceived Likelihood below 5 with no audience yet** = trust gap; first move is proof, not copy.

---

## Calibrating examples by artifact type

Use these to anchor the universal bands in the artifact's domain. Read the row matching the user's artifact type before scoring.

### OFFER (paid product/service/package/course/coaching)

| Lever | 1-2 | 5-6 | 9-10 |
|-------|-----|-----|------|
| Dream Outcome | "Improve your marketing" | "Generate 50 qualified leads/month" | "Replace your 9-to-5 income in 120 days and never miss another school pickup" |
| Likelihood | "Trust me, this works" | 20+ testimonials + named framework | 500+ case studies, performance guarantee, public dashboard |
| Time Delay | Results in 6+ months, no quick wins | First result in 30 days, full in 90 | Set up in 1 hour, first leads same day |
| Effort | 200-hour cert + DIY implementation | 10-step playbook with templates | Done-for-you; 3 decisions total |

### CONTENT (video/essay/post/talk/thread/podcast)

| Lever | 1-2 | 5-6 | 9-10 |
|-------|-----|-----|------|
| Dream Outcome | Vague "useful info" | "You'll learn how X works" | A reframe that changes how the viewer sees X for years |
| Likelihood | No credibility, no examples | Author bio + 1-2 examples | Specific case + numbers + named track record + receipts shown |
| Time Delay | Payoff in last paragraph after long preamble | Hook by 30s, payoff by minute 2 | First insight in first 3 seconds; one quotable line per minute |
| Effort | Dense, requires re-reading, demands prerequisites | Skimmable with headers and visuals | Single read; no jargon; visual aids do the heavy lifting |

### FEATURE (capability/tool/component inside a product)

| Lever | 1-2 | 5-6 | 9-10 |
|-------|-----|-----|------|
| Dream Outcome | "Manage your X" | "Send a report in 3 clicks" | "Ship the deal — every objection auto-handled, contract auto-drafted, nothing falls through" |
| Likelihood | Empty UI, no examples, no signal | Sample data, helper text, in-app docs | Live preview, success stories in-product, real-time success counter |
| Time Delay | First value after multi-step setup and config | Value within first session after onboarding | Value within 10 seconds of opening; zero-config |
| Effort | Forces a new mental model | Familiar pattern, light learning | Invisible — works the way the user already thinks |

### IDEA (concept/strategy/pitch/hypothesis/framework)

| Lever | 1-2 | 5-6 | 9-10 |
|-------|-----|-----|------|
| Dream Outcome | "It'd be cool if..." | "Solves a known problem for a real segment" | Reframes a category — if true, makes existing alternatives look obsolete |
| Likelihood | No precedent, no analogies | Adjacent precedents exist | Adjacent precedents + early signal (waitlist, paid pilot, organic pull) |
| Time Delay | Years to first signal | Signal in weeks | Signal achievable this week with a 1-day test |
| Effort | Requires building a platform first | Requires a small experiment | Test runnable today with no engineering |
