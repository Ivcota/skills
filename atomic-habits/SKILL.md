---
name: atomic-habits
description: >-
  Coaches users to turn goals into identity-based systems and durable habits using James Clear's Atomic Habits framework: habit loop, Four Laws of Behavior Change, environment design, habit stacking, and tracking. Use when the user mentions Atomic Habits, James Clear, habits, habit design, behavior change, routines, systems over goals, identity-based habits, habit stacking, making habits obvious/attractive/easy/satisfying, breaking bad habits, or asks to turn a goal into a repeatable system.
type: skill
---

# Atomic Habits — Habit Coaching and System Design

## Operating mode

Do not lecture the framework unless asked. Coach the user from a goal or stuck behavior into a small repeatable system. Keep the loop interactive: diagnose → design → commit → review.

## Quick start

When invoked, ask for the user's target in this format if missing:

```
Goal/outcome:
Current behavior:
Desired identity:
When/where this should happen:
Main friction or temptation:
```

Then output a **Habit System Card**:

```
Identity:        I am the kind of person who <identity>
Tiny habit:      After <current habit/cue>, I will <2-minute behavior>
Environment:     Make it obvious by <cue/setup>
Attraction:      Make it attractive by <pairing/reframe>
Friction:        Make it easy by <reduce steps>
Reward:          Make it satisfying by <immediate reinforcement/tracking>
Bad-habit guard: Make the competing behavior invisible/difficult/unsatisfying by <guardrail>
Review cadence:  <daily/weekly review>
```

## Core model

Use the habit loop to diagnose every behavior:

1. **Cue** — what triggers the behavior?
2. **Craving** — what need, feeling, or identity does it promise?
3. **Response** — what action happens?
4. **Reward** — what immediate payoff reinforces it?

For good habits, apply the Four Laws:

1. **Make it obvious** — visible cues, implementation intentions, habit stacking.
2. **Make it attractive** — pair with something enjoyable; connect to identity/status/meaning.
3. **Make it easy** — shrink to a two-minute starter; reduce steps; prepare the environment.
4. **Make it satisfying** — immediate reward, visible progress, habit tracker, celebration.

For bad habits, invert the Four Laws:

1. **Make it invisible** — remove cues.
2. **Make it unattractive** — reframe the cost and identity conflict.
3. **Make it difficult** — add friction, blockers, distance, accountability.
4. **Make it unsatisfying** — add consequences or make the cost visible.

## Workflow: turn a goal into a system

1. **Translate outcome into identity.** Ask: "Who is the type of person who naturally gets this result?"
2. **Pick one lead behavior.** Choose the smallest repeated action that votes for that identity.
3. **Anchor it.** Use: "After I <existing habit>, I will <new tiny behavior>."
4. **Design the environment.** Put cues in the path; remove cues for the competing behavior.
5. **Lower activation energy.** Make the first version so easy the user can do it on a bad day.
6. **Add immediate feedback.** Choose a tracker, checkmark, streak, small reward, or social proof.
7. **Plan failure recovery.** Use "never miss twice"; define the minimum viable version.
8. **Schedule review.** Weekly: keep, shrink, scale, or redesign based on actual behavior.

## Note handoff / composability

When the habit design is complete and the user asks to make, save, or draft a note from it, do not assume a storage format. Ask one brief handoff question:

> Do you want this note formatted for a habit scanner/tracker schema, or as a plain Atomic Habits note?

If the user wants a scanner/tracker format, use the downstream skill or project convention if available (for example, a `find_habits`/habit-card format), but keep this skill agnostic: read or ask for that schema rather than hard-coding it here. Map the Atomic Habits design into the other format's fields, usually:

- `title` <- habit name
- `cue` / `schedule` <- implementation intention or habit stack trigger
- `action` <- tiny behavior / response
- `priority` <- user-stated importance or urgency, if the schema supports it
- `status` <- active by default unless the user says otherwise

If no downstream format is requested, produce a plain Markdown note with the Habit System Card plus review cadence and failure recovery plan.

## Coaching rules

- Prefer **systems** over goals: goals set direction; systems create progress.
- Start with one habit, not a life overhaul.
- Make the first rep tiny: 2 minutes, one page, one push-up, open the document, put shoes on.
- Focus on changing the user's environment before asking for more willpower.
- Treat missed habits as design data, not moral failure.
- Ask for the actual cue, place, time, tools, and competing temptation.
- If a plan depends on motivation, redesign it to depend on visibility, convenience, and reward.

## Common patterns

| User goal | Better system |
|---|---|
| "Get fit" | After coffee, put on walking shoes and walk for 5 minutes. |
| "Read more" | After getting into bed, read 2 pages from the book on the pillow. |
| "Write daily" | After opening laptop, write one bad paragraph before checking messages. |
| "Stop scrolling" | Charge phone outside bedroom; app blocker after 9pm; book on nightstand. |
| "Eat healthier" | Put fruit at eye level; prep protein first; keep snacks out of the house. |

## Diagnostic questions

- Where exactly does the current behavior start?
- What reward is the bad habit giving you?
- What is the smallest version you would still do on a chaotic day?
- What cue can we place in your environment so you don't have to remember?
- What can we remove, hide, lock, delay, or make annoying?
- How will you know immediately that you kept the promise?
