# /go Reference

## Micro-Prep: Minimal Daily Note Template (Step 2b)

If today's note doesn't exist, create it before running micro-prep:

```
---
up: []
related: []
created: [TODAY]
---
<< [[Calendar/Notes/[YESTERDAY]]] | [[Calendar/Notes/[TOMORROW]]] >>

# Rolling Timeblocks


# Shaped Goals


****


# Today's Notes

## Sequential Productivity

**Current:**
**Next:**

****

[Embed or link the configured procrastination list here if one exists; otherwise omit this line.]
```

Substitute [TODAY], [YESTERDAY], [TOMORROW] from `currentDate`. Set `up` to the weekly note link if `Calendar/Notes/[YEAR]-W[NN].md` exists, otherwise leave `up: []`. If the user/environment provides a configured daily notes path, use that instead of `Calendar/Notes/`.

After creating the note, run micro-prep (two questions) to populate Rolling Timeblocks, then continue to Step 3.

---

## Values Table (for Shaped Goals)

Use these when inferring a Value during micro-prep (Step 2b) or filling in missing Shaped Goals. You suggest — user confirms or adjusts.

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

---

## Shaped Goal Format

```
**Value:** [one or more values from the table above]
**Outcome:** [specific result they'd recognize as done]
- [ ] **Process:** [time-bound action]
- [ ] **Process:** [additional time-bound action if any]
```

---

## Sync Rules (Step 4)

**If finished:** Mark `[x]` in Rolling Timeblocks. If a matching Process item exists in Shaped Goals, mark it `[x]` too.

**If not finished:** Keep `[ ]` and move back into the queue. Re-propose it in Step 6 alongside the next unstarted blocks. Adjust queue order if downstream blocks shift. **Note the calendar event ID** so the block can be rescheduled (not duplicated) in Step 7.

---

## Commit Rules (Step 7)

**Rescheduled blocks** (unfinished from Step 4): Use `gcal_update_event` on the original event ID to move it to the new time.

**New blocks** (no existing calendar event): Use `gcal_create_event` on the selected timeblock calendar only. Never write events to any other calendar unless the user explicitly selects it as the timeblock calendar.

---

## Wrap-Up Transition (Step 8)

When all timeblocks are complete, continue directly into the `/wrap-up` skill flow if that skill is available. No announcement. If no wrap-up skill is available, summarize the completed blocks and ask whether the user wants to plan the next day.

---

## Belt Context

`/go` is the primary daily habit. It handles three states:
- **No plan** → micro-prep inline (Step 2b)
- **Plan in progress** → sync, orient, commit (Steps 3–7)
- **Queue clear** → close out via `/wrap-up` inline if available, otherwise summarize and offer next-day planning (Step 8)

`/intentional` is the intentional deep version — run it explicitly on quiet mornings when you want the full Values interview.
