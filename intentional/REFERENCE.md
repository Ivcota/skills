# Intentional — Reference

## Deep Mode Interview Flow

For carry-forwards, start with:
> "You're carrying '[item]' from [today/yesterday]. What value does finishing this connect to?"

For new goals:
> "What do you want to accomplish [today/tomorrow]?"

For each goal:
1. "Why does that matter to you right now?" — uncovers the **Value**
2. Confirm outcome — rephrase into something concrete, specific enough to know when done
3. If the goal is stalled/avoided/carry-forward: "Which trigger does this task set off — boring, frustrating, unpleasant, far away, unstructured, or meaningless?"
4. Choose matching Procrastination Roadmap interventions and convert them into time-bound Process actions
5. "How will you work on this? Give me the action as a time-bound block — like '30 mins of X'."
6. "Anything else for this goal?"

---

## Auto Mode Synthesis

Read silently before responding:
- Last 5 existing daily notes (`Calendar/Notes/[recent dates].md` by default, or the configured daily notes path)
- The configured procrastination list, if one exists
- Carry-forwards from `$ARGUMENTS`

Synthesize patterns: recurring incomplete items, stated priorities, stalled procrastination items. For stalled/carry-forward work, infer likely procrastination triggers from the roadmap and pick matching interventions. Infer the most likely Value for each goal based on context.

Propose all goals at once as fully-formed Shaped Goals (Value + Outcome + Process already filled). Then ask once:
> "Here's what I'd set up for [today/tomorrow]. Any adjustments?"

Make any requested edits, then proceed immediately to Rolling Timeblocks and writing the note — no further prompts. Rolling Timeblocks are a flexible menu of bounded work blocks, not a fixed schedule; intentional should not assign clock times.

---

## Procrastination Roadmap

Use this when a task is stalled, repeatedly carried forward, vague, emotionally heavy, or listed on the user's procrastination list.

Legend:
- **Prep** = setup intervention before execution
- **Do** = action intervention during execution

Ask: **"Which trigger does this task set off?"**

| Trigger | Prep interventions | Do interventions |
|---|---|---|
| **Boring** | Up the challenge; practice daily disconnection; dopamine fast | — |
| **Frustrating** | Make it a learning goal | — |
| **Unpleasant** | Add joy | Practice aversion journaling; treat yourself |
| **Far Away** | Connect with future you; find accountability | Track your goal page; set mini goals; find accountability |
| **Unstructured** | Connect to your life systems; designate habit points | Define the very next step; shrink your resistance; time block; connect to your life systems |
| **Meaningless** | Do a values edit | Is the goal worth dropping? |

Convert interventions into concrete Process actions. Examples:
- **Up the challenge** → `30 mins: make the boring task harder in a useful way — race the clock, raise the quality bar, or add a constraint`
- **Practice daily disconnection** → `10 mins tonight: put phone in Do Not Disturb, grayscale, or Sleep mode so stimulation winds down before bed`
- **Dopamine fast** → `15 mins: identify one infinity pool/high-stimulation input to weed out and choose an analog replacement`
- **Make it a learning goal** → `30 mins: try one approach and write what failed, changed, or became clearer`
- **Practice aversion journaling** → `10 mins: write what feels unpleasant, what you're avoiding, and the smallest tolerable next action`
- **Treat yourself** → `After the block: redeem a specific small reward if the work block is completed`
- **Add joy** → `45 mins: work with music, coffee, location, tools, or company that makes the task lighter`
- **Track your goal page** → `10 mins: update the cumulative goal page and compare current progress against target pace`
- **Set mini goals** → `20 mins: complete the next tiny milestone toward the farther goal`
- **Find accountability** → `5 mins: send the target and deadline to someone who will check whether it happened`
- **Connect with future you** → `10 mins: write what future-you gains if this gets done and what they inherit if it doesn't`
- **Define the very next step** → `15 mins: identify the first physical action and do it`
- **Shrink your resistance** → `10 mins: open the file, make one tiny edit, stop if needed`
- **Time block** → `30 mins: focused work on [specific task]`
- **Connect to your life systems** → `10 mins: attach this task to an existing routine, calendar block, checklist, or habit stack`
- **Designate habit points** → `5 mins: assign points for completing the habit and define what indulgence those points can redeem`
- **Do a values edit** → `10 mins: rewrite why this matters and which Value it serves`
- **Is the goal worth dropping?** → `10 mins: decide whether to drop, defer, shrink, or recommit to the goal`

Do not over-prescribe. Pick the smallest useful intervention, especially in auto mode.

---

## Values Table

| Value | When to use it |
|---|---|
| **Achievement** | Excelling, finishing something meaningful, demonstrating competence |
| **Benevolence** | Caring for people close to them, helping or serving others |
| **Conformity** | Acting within norms, respecting rules or expectations |
| **Face** | Maintaining reputation, self-image, how others perceive them |
| **Hedonism** | Pleasure, enjoyment, personal gratification |
| **Power** | Influence, control over outcomes, status, resources |
| **Security** | Safety, stability, harmony in relationships or environment |
| **Self-Direction** | Autonomy, independent thinking, freedom to choose their own path |
| **Spirituality** | Inner life, devotion, sacred meaning |
| **Stimulation** | Novelty, challenge, excitement, variety |
| **Tradition** | Respect for culture, heritage, long-held customs and beliefs |
| **Universalism** | Understanding, tolerance, care for all people and nature |

You suggest — user confirms or adjusts.

---

## Shaped Goal Format

```
**Value:** [one or more values]
**Outcome:** [specific result they'd recognize as done]
- [ ] **Process:** [time-bound action]
- [ ] **Process:** [additional time-bound action if any]
```

---

## Daily Note Template

Default file path: `Calendar/Notes/[TARGET].md` unless the user/environment provides a configured daily notes path.
- Today-mode: target = `[TODAY]`, prev = yesterday, next = tomorrow
- Tomorrow-mode: target = `[TOMORROW]`, prev = today, next = day after tomorrow

`up` field: set to weekly note link if `Calendar/Notes/[YEAR]-W[NN].md` exists, else `up: []`.

```
---
up: ["[[Calendar/Notes/[YEAR]-W[NN]]]"]
related: []
created: [TARGET]
---
<< [[Calendar/Notes/[PREV]]] | [[Calendar/Notes/[NEXT]]] >>

# Rolling Timeblocks

[populated flexible menu of bounded work blocks from Step 4 — no clock times]

# Shaped Goals

[populated shaped goals from Step 2]

****


# Today's Notes

****

[Embed or link the configured procrastination list here if one exists; otherwise omit this line.]
```
