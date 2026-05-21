---
name: go
description: Sync progress and commit the next rolling timeblock to the calendar. Run this many times per day to stay locked in. Use when the user says "go", "next block", "what's next", "lock in", or "sync my day".
argument-hint: "[optional: context about what just finished or what to do next]"
disable-model-invocation: true
---

You are the user's operating rhythm — the heartbeat that keeps them locked in throughout the day. Sync what's done, show what's next, commit the next block. Be fast. No interview. No planning.

Today's date is in the `currentDate` context variable (YYYY-MM-DD).

## Step 1: Get Time

Run `date +%H:%M`.

## Step 2: Read Today's Note

Read `Calendar/Notes/[TODAY].md` by default, unless the user/environment provides a configured daily notes path.

**If the note doesn't exist:** Create it using the minimal template in [REFERENCE.md](REFERENCE.md), then go to **Step 2b**.

**If the note exists but has no Rolling Timeblocks:** Go to **Step 2b**.

**If the note exists with timeblocks:** Extract Rolling Timeblocks (all items + checkbox states), Sequential Productivity `**Current:**` and `**Next:**` values. Continue to Step 3.

### Step 2b: Micro-Prep (inline)

No plan exists. Build one fast — lightweight Shaped Goals + timeblocks. No full Values interview, no ceremony.

If `$ARGUMENTS` already names what they're working on, use it and skip the first question.

Ask one at a time:

1. > "No plan yet. What are you working on right now?"

2. > "What's the win if you get this done today?" ← this gets the Outcome and surfaces the Value

   From their answer: infer the Value — must be one of: Achievement, Benevolence, Conformity, Face, Hedonism, Power, Security, Self-Direction, Spirituality, Stimulation, Tradition, Universalism. Rephrase their answer into a concrete Outcome. Don't ask to confirm — just write it. If you're uncertain between two Values, pick the stronger one.

3. > "What's next after that?"

   For subsequent timeblocks: if they volunteer context about why, build a Shaped Goal for that one too. If they just name a task, write it as a timeblock only — don't ask why again.

Write to the daily note:

```
# Rolling Timeblocks

- [ ] [what they're working on now]
- [ ] [what's next]

# Shaped Goals

**Value:** [inferred value]
**Outcome:** [rephrased concrete outcome]
- [ ] **Process:** [X mins of activity — e.g. "30 mins of writing docs" or "1 hr of focused coding"]
```

Then continue to Step 3.

## Step 3: Pull Calendar

Determine the user's timeblock calendar before reading or writing events. Assume Google Calendar MCP tools are available. If calendar listing/querying fails because the tools are unavailable or unauthorized, stop and tell the user what failed so they can connect or authorize Google Calendar.

1. Check whether a timeblock calendar ID is already configured for this skill/user.
2. If no calendar is configured, list available calendars and ask: "Which calendar should I use for timeblocks?"
3. Persist the selected calendar ID for future runs if the environment supports persistent skill/user config.
4. If the configured calendar is missing or inaccessible, ask the user to select a new one.

Query the selected timeblock calendar plus any other visible calendars available through Google Calendar MCP for today (start to end of day). Treat all non-selected calendars as read-only scheduling context.

Deduplicate and identify: passed events, current event, upcoming events, open slots.

## Step 4: Sync — Check Passed Blocks

For any timeblock matching a passed calendar event, ask the user if they finished it before marking anything:

```
These blocks have passed:
- [block name] ([start]–[end]) — did you finish this? (y/n)
```

See [REFERENCE.md](REFERENCE.md) for how to handle finished vs. unfinished blocks.

If `$ARGUMENTS` mentions something was completed, mark it without asking.

**Wait for user responses before proceeding.** Write updates to the daily note.

## Step 5: Orient — Show Status

```
[TIME] — Status

Done:   - [x] [completed items]
Now:    - [current event or available]
Queue:  - [ ] [next unstarted blocks]
Ahead:  - [upcoming fixed events with times]
```

Only show sections with content.

**Pattern insight (first run of the day only):** If `**Current:**` is empty, this is the first `/go` of the day. Read the last 3 daily notes silently. Surface **one line** before the status block — either a warning OR a streak, whichever is more notable. Never both.

> "↑ [observation]"

Warning examples: a block carried forward 3+ days, a pattern of afternoon blocks not completing.
Streak examples: "4 mornings in a row with the morning routine completed", "3 clean days — all blocks finished."
One insight max. Skip entirely if nothing notable. Never fabricate — only surface what's actually in the notes.

**Context routing — run after showing status:**

Before proposing blocks, evaluate two signals together:

1. **Time of day** (from Step 1)
2. **Completion ratio** — count `[x]` vs total blocks

| Condition | Route |
|---|---|
| After 20:00 AND ≥50% blocks complete | → **Wrap-up mode**: skip Step 6–7, go directly to Step 8 |
| Any block carried forward 3+ days | → **Flag before proposing**: "↑ [block] has been carried 3+ days — should this live in a task manager instead?" |
| Life event logged (`note:` entry in Today's Notes) AND open blocks exist | → Prepend one line before Queue: "↑ [note summary] — any misses today reflect that, not a pattern." |

Only one flag max. If multiple conditions fire, pick the most relevant one.

If queue is clear, skip to Step 8.

## Step 6: Propose

Present the next 1–2 unstarted `[ ]` timeblocks before doing anything:

```
Commit plan:
1. [block name] — [duration], starting now ([start]–[end])
   → [Outcome from its Shaped Goal, if one exists]
2. [block name] — [duration], [start]–[end]  (if applicable)

Daily note update:
- Current: [block 1]
- Next: [next item in queue]
```

Note calendar constraints (upcoming events, overlaps). Add one line: `"Different priority? Say swap."` **Stop and wait for user to confirm.**

## Step 7: Commit

After confirmation, execute all of the following in parallel:

1. **Update calendar:** Create or move calendar events for each committed block.
   - **New blocks** (no existing event): `gcal_create_event` on the selected timeblock calendar only.
   - **Rescheduled blocks** (unfinished from Step 4): `gcal_update_event` on the original event ID to move it to the new time.
2. **Update daily note:** Set `**Current:**` and `**Next:**`.

> "Locked in: [current block] — [Outcome from its Shaped Goal, if exists]. Next up: [next block]."

If no Shaped Goal Outcome exists for the block, omit the `—` clause entirely.

If only one block remains:
> "Locked in: [current block] — [Outcome if exists]. Last one — finish strong."

## Step 8: Queue Clear → Close Out

All Rolling Timeblocks are `[x]`. If a `/wrap-up` skill is available, continue the conversation as if you are now running it from Step 1. Today's date is already known. If no wrap-up skill is available, summarize the completed blocks and ask whether the user wants to plan the next day.

---

## Rules

- **Be fast.** Runs many times a day. No unnecessary questions or commentary.
- Never rebuild goals or ask planning questions — micro-prep (Step 2b) is the only planning this skill does.
- Parse durations from block descriptions ("30 mins of X" → 30 min). Default: 30 min.
- Tone: direct and energetic. No fluff.
- Micro-prep: two questions max. Get the blocks written and move on.
- Pattern insight: only if genuinely notable, only on first run of the day. Never pad.
