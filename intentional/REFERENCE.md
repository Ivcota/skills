# Intentional — Reference

## Deep Mode Interview Flow

For carry-forwards, start with:
> "You're carrying '[item]' from [today/yesterday]. What value does finishing this connect to?"

For new goals:
> "What do you want to accomplish [today/tomorrow]?"

For each goal:
1. "Why does that matter to you right now?" — uncovers the **Value**
2. Confirm outcome — rephrase into something concrete, specific enough to know when done
3. "How will you work on this? Give me the action as a time-bound block — like '30 mins of X'."
4. "Anything else for this goal?"

---

## Auto Mode Synthesis

Read silently before responding:
- Last 5 existing daily notes (`Calendar/Notes/[recent dates].md` by default, or the configured daily notes path)
- The configured procrastination list, if one exists
- Carry-forwards from `$ARGUMENTS`

Synthesize patterns: recurring incomplete items, stated priorities, stalled procrastination items. Infer the most likely Value for each goal based on context.

Propose all goals at once as fully-formed Shaped Goals (Value + Outcome + Process already filled). Then ask once:
> "Here's what I'd set up for [today/tomorrow]. Any adjustments?"

Make any requested edits, then proceed immediately to Rolling Timeblocks and writing the note — no further prompts. Rolling Timeblocks are a flexible menu of bounded work blocks, not a fixed schedule; intentional should not assign clock times.

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
