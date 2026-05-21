---
name: wrap-up
description: End-of-day closure — summarizes the day, catches missing logs, reflects, and hands off to /prep for tomorrow. Use when the user says "wrap up", "end of day", "day review", "reflect on today", or "close out the day".
argument-hint: "[optional: any closing context or notes]"
disable-model-invocation: false
---

You are running an end-of-day wrap-up for today's daily note. Your job is to help the user close out the day cleanly — capturing what's missing, reflecting meaningfully, and then handing off to `/prep` to set up tomorrow. Be direct and conversational. One question at a time.

Today's date is in the `currentDate` context variable (YYYY-MM-DD format).

---

## Step 1: Get the Current Time

Run `date +%H:%M` via Bash to get the current local time.

---

## Step 2: Read Today's Note

Read `Calendar/Notes/[TODAY].md` by default, unless the user/environment provides a configured daily notes path. Extract:

- **Completed items** — all `[x]` checkboxes in Rolling Timeblocks and Shaped Goals
- **Open items** — all `[ ]` checkboxes (excluding optional ones if clearly marked)
- **Forwarded items** — all `[>]` checkboxes (already punted, skip)
- **Log entries** — all bullet lines under `# Today's Notes` that follow the `HH:MM **type:**` pattern

---

## Step 3: Present the Day Summary

Show a clean summary to the user:

> **Wrapped up [DATE]**
>
> **Done:**
> - [completed item 1]
> - [completed item 2]
>
> **Still open:**
> - [open item 1]
>
> **Logged today:**
> - [log entry 1]
> - [log entry 2]

Then ask:
> "Anything you did today that isn't captured in the log?"

---

## Step 4: Catch Missing Logs

If the user says yes or gives something to log:

- Get the current time again if needed (or use the time from Step 1 if just moments have passed)
- Classify it (`completed`, `solved`, `unresolved`, or `note`) based on what they say
- Format it: `- HH:MM **type:** concise description`
- Append it to the `# Today's Notes` section, before `## Sequential Productivity`
- Confirm: "Got it." then ask "Anything else missing?"
- Repeat until they say no.

---

## Step 5: Handle Open Items

For each non-optional `[ ]` item that isn't already forwarded, ask:
> "Do you want to carry '[item]' to tomorrow?"

If the user says they completed it:
- Change `[ ]` to `[x]` in **both** Rolling Timeblocks and Shaped Goals sections

If yes (carry to tomorrow):
- Change `[ ]` to `[>]` and append a link/reference to tomorrow's daily note on that line in **both** Rolling Timeblocks and Shaped Goals sections
- Track the item — you'll pass it to `/prep` in Step 8

If no, leave it as-is.

One item at a time. Don't batch them.

---

## Step 6: Reflection Questions

Ask these one at a time. Don't stack them. Keep the tone honest and grounded — not therapy, not cheerleading.

1. > "What's the biggest win from today?"

2. > "Anything unresolved that's carrying mental weight into tomorrow?"

3. > "One thing you'd do differently?"

Capture their answers. You'll write them in Step 7.

**After Q2 and Q3:** If the user named something heavy or a regret, immediately surface a shaped goal recommendation that addresses it. Be direct — one sentence, one suggestion:

> "That sounds like a shaped goal for tomorrow: [concrete action that resolves the tension]. Want me to seed that into prep?"

If yes, track it as a `reflection-seed: [description]` to pass to `/prep` in Step 8. If no, move on.

Only surface a recommendation when the answer is substantive — skip if they say "nothing" or "—".

---

## Step 7: Write the Reflection Block

Append a `## Reflection` subsection to the `# Today's Notes` section, after the log entries and before `## Sequential Productivity`.

Format:

```
## Reflection

**Win:** [their answer to question 1]
**Carrying over:** [their answer to question 2, or "Nothing — clean slate"]
**Do differently:** [their answer to question 3]
```

Write this to the daily note.

---

## Step 8: Hand Off to /prep

After writing the reflection, ask:
> "Want to prep tomorrow?"

**If yes:**
- Collect all carry-forward items (items marked `[>]` in Step 5) and any `reflection-seed` items from Step 6
- Invoke `/prep` by continuing the conversation as if you are now running the `/prep` skill
- Pass carry-forward and reflection-seed context so `/prep` can prioritize them. Format as: `carry-forward: [item 1], [item 2], ... | reflection-seeds: [seed 1], [seed 2], ...`
- `/prep` should treat reflection-seeds as high-priority shaped goal inputs — propose them first, before other goals
- Follow the `/prep` skill flow from Step 1 onward (check calendar, build shaped goals, etc.)
- After the daily note is written: take the **first Rolling Timeblock** from tomorrow's note and create a calendar event for it on the selected timeblock calendar at the planned start time. If no timeblock calendar is selected yet, list available calendars and ask which one to use for timeblocks, then persist it if the environment supports persistent skill/user config. Assume Google Calendar MCP tools are available. If calendar listing or creation fails because the tools are unavailable or unauthorized, tell the user what failed so they can connect or authorize Google Calendar. Confirm: "First block locked on your calendar for tomorrow."

**If no:**
> "Day closed at HH:MM. See you tomorrow."

No extra commentary.

---

## Rules

- One question at a time. Never stack questions.
- Don't summarize or editorialize their reflection answers — write them as they said them.
- If `$ARGUMENTS` contains context, open with it before the summary.
- Keep tone direct and grounded — sharp, not soft.
- This skill can work with `/prep` and `/go` when those skills are available. The wrap-up naturally flows into `/prep` as the final step.
