# The Four Heresies

TOC contradicts four standard managerial beliefs. These show up constantly in the user's reasoning. Detect them, name them, and push back.

The skill's job isn't to be combative — it's to make the heresy visible so the user can choose. Most people drift back into these defaults under pressure. Naming the fallacy out loud is what breaks the drift.

---

## 1. Utilization fallacy

**The belief:** "Everyone should be 100% busy. Idle resources are waste."

**Why it's wrong:** Forcing 100% utilization at non-constraint resources creates WIP piles upstream of the constraint. The system's throughput is set by the constraint's capacity — extra production from non-constraints just becomes inventory waiting at the bottleneck. WIP up, T flat, system worse.

**Detection patterns:**
- "We need to keep the team fully utilized."
- "If they're not at 100%, we're paying for nothing."
- "Why is this engineer/AE/recruiter not booked solid?"
- Resource utilization is the headline metric in a dashboard.

**How to call it out:** "That's the utilization fallacy. A non-constraint resource at 100% will starve, queue, or break the constraint downstream. Some idle time at non-constraints is *correct.*"

---

## 2. Local-optima fallacy

**The belief:** "If every step gets cheaper or faster, the system gets better."

**Why it's wrong:** Improvements at non-constraint stages are invisible to system throughput. Making a non-bottleneck twice as fast just means it sits idle twice as much. Cost cuts at non-constraints are paper savings — the system's pace is unchanged because the bottleneck is unchanged.

**Detection patterns:**
- "Every team should be improving their KPIs."
- "We saved 20% on stage X."
- "Our department's metrics are great — why isn't the company growing?"
- Rolling up a sum of stage-level improvements as if they added.

**How to call it out:** "That's the local-optima fallacy. Improvements at non-constraints don't move T. Where is the constraint? Did this change touch it?"

---

## 3. Balance-the-line fallacy

**The belief:** "Capacity should be balanced across all stages — no one is the bottleneck."

**Why it's wrong:** Variability in real systems means a balanced line *constantly* shifts which stage is the bottleneck. Every stage takes turns starving the others. TOC says: deliberately *unbalance* the line so the constraint is obvious, then protect it. A clear bottleneck with a buffer in front of it produces *more* than a balanced line with no buffer.

**Detection patterns:**
- "We should hire a second [reviewer / SDR / interviewer] so each stage has equal capacity."
- "Why is one team always the bottleneck? Let's spread the load."
- "Our process should flow evenly."
- Capacity-planning that targets equal capacity per stage.

**How to call it out:** "Goldratt's heresy here is to keep the line *deliberately unbalanced.* A clear, protected constraint produces more than a balanced line. Balancing means everything becomes the bottleneck in turn — and nothing has a buffer."

---

## 4. Busyness-as-progress fallacy

**The belief:** "We worked hard, so we made progress."

**Why it's wrong:** T is the only measure of progress. Activity that doesn't move T is waste — even if it felt productive, even if hours were logged, even if everyone was busy. Busyness at non-constraints actively hurts the system (heresies 1 and 2). Busyness at the constraint is good *if it's the right work*; busyness at the constraint on the wrong work is the worst case.

**Detection patterns:**
- "It was a great week — everyone was slammed."
- "We shipped 30 PRs!" (Were any of them user-facing? Did T move?)
- Status reports that list activity instead of outcomes.
- "I have no idea why we're not making more progress — everyone's working flat out."

**How to call it out:** "Activity isn't throughput. What did the system *deliver* — what increased T, decreased I, decreased OE? If you can't name a system-level change, the busyness was waste."

---

## When two heresies stack

These compound. The most common stack:
- **Utilization + busyness:** "Everyone was at 100% all week and we shipped a ton of internal work" — the worst case. Maximum activity, maximum WIP, no T.
- **Local optima + balance the line:** "Each team improved its metrics and we have equal capacity everywhere" — a beautifully optimized system that produces nothing at the rate of the slowest variable stage.

When a stack is detected, name *both* and trace through what's happening to T.

## How to push back without lecturing

Don't deliver mini-essays. Use the **named-heresy + one-question** pattern:

> "That's the utilization fallacy. Where does work pile up right now?"

> "That's local-optima. Did T move?"

> "That's busyness-as-progress. What did the *system* deliver?"

The naming makes the pattern legible. The question forces the user back to system-level evidence. Lecturing makes the user defensive; naming + asking makes them think.
