---
name: intentional
description: Planning session that builds a complete daily note with Shaped Goals, Rolling Timeblocks, and calendar awareness. Targets today (if before noon, incomplete note) or tomorrow (after noon). Uses auto proposal mode by default; use `/intentional deep` for a full Values interview. Use when the user says "intentional", "plan today", "plan tomorrow", or "set up my day".
argument-hint: "[deep] [auto] [optional priorities or carry-forward items]"
disable-model-invocation: true
---

Build a daily note so the user can execute without thinking. One question at a time.

See [REFERENCE.md](REFERENCE.md) for the Values table, Shaped Goal format, and Daily Note template.

---

## Step 0: Determine Mode

**Depth mode** (from `$ARGUMENTS`):
- `deep` present → deep mode: full Values interview, one question at a time
- `auto` present or absent → auto mode: read context, propose all goals at once, single adjustment prompt
- optional priorities or carry-forward items present → treat them as high-priority shaped goal inputs; propose them first in Step 2 before other inferred goals

**Timing mode** (auto-detect current time):
- After noon → target = **tomorrow**
- Before noon → read today's note (`Calendar/Notes/[TODAY].md` by default, or the configured daily notes path):
  - No Shaped Goals → target = **today**
  - Has Shaped Goals → ask: "Today already has goals — prepping for today or tomorrow?"

Compute ISO week number for target date. Check whether the weekly note exists in the default or configured notes path.

---

## Step 1: Calendar Check (always first, both modes)

Determine the user's timeblock calendar before reading or writing events. Assume Google Calendar MCP tools are available. If calendar listing/querying fails because the tools are unavailable or unauthorized, stop and tell the user what failed so they can connect or authorize Google Calendar.

1. Check whether a timeblock calendar ID is already configured for this skill/user.
2. If no calendar is configured, list available calendars and ask: "Which calendar should I use for timeblocks?"
3. Persist the selected calendar ID for future runs if the environment supports persistent skill/user config.
4. If the configured calendar is missing or inaccessible, ask the user to select a new one.

Query the selected timeblock calendar plus any other visible calendars available through Google Calendar MCP for the target day (start to end of day). Treat all non-selected calendars as read-only scheduling context.

Deduplicate and summarize fixed commitments, or confirm open calendar.

---

## Step 2: Shaped Goals

**Deep mode:** Conversational Values interview. For each goal: ask why it matters → map to a Value → confirm concrete Outcome → get time-bound Process actions. See [REFERENCE.md](REFERENCE.md) for the Values table and question flow.

**Auto mode:** Read the last 5 existing daily notes. Also read the configured procrastination list if it exists. Before proposing goals, surface what you found in one short block:

> "Based on your last 5 days: [1–2 notable observations — e.g., 'You've carried X forward 3 days', 'Achievement goals have been your most-completed', 'Afternoon blocks rarely finish']. Here's what I'd set up:"

Then propose all Shaped Goals at once — fully formed with inferred Value, Outcome, and Process. Values MUST come from the Values Table in REFERENCE.md — never invent one (valid: Achievement, Benevolence, Conformity, Face, Hedonism, Power, Security, Self-Direction, Spirituality, Stimulation, Tradition, Universalism). Ask once: "Any adjustments?" Make edits, then proceed immediately. See [REFERENCE.md](REFERENCE.md) for synthesis approach.

Repeat until 2–4 goals or user is done (deep mode only).

---

## Step 3: Procrastination List (deep mode only)

Read the configured procrastination list if it exists. Surface unchecked items not already addressed. Build a Shaped Goal if yes. If no procrastination list exists, skip this step silently.

(Auto mode folds these into Step 2 synthesis — don't surface again.)

---

## Step 4: Rolling Timeblocks

Pull every Process item from all Shaped Goals into `# Rolling Timeblocks` as a flexible menu of bounded work blocks the user can choose from when ready to work. Do **not** assign clock times or prescribe exact calendar slots in the daily note. Use calendar events only to avoid unrealistic load and group/order blocks sensibly. Add standing daily items at top. In auto mode, write immediately — no reorder prompt.

---

## Step 5: Write the Daily Note

Write to `Calendar/Notes/[TARGET].md` by default, or the configured daily notes path if one is provided. See [REFERENCE.md](REFERENCE.md) for the full template and date path logic.

After writing:
- Today-mode: "You're set. First up: [first timeblock]. Go."
- Tomorrow-mode: "Tomorrow's set. First up: [first timeblock]. Good night."

---

## Rules

- Default is auto mode. Deep mode requires explicit `/intentional deep`.
- Auto mode: always show synthesis observations before proposing — never silently propose.
- Auto mode: never ask follow-up questions after the adjustment prompt — write and go.
- Deep mode: never skip the Values conversation. A goal without a Value is just a wish.
- One question at a time (deep mode). Don't stack questions.
- Calendar check always runs first, both modes.
- Tone: direct and energetic — sharp accountability partner, not a life coach.
- Keep this skill standalone. Do not reference or depend on any other skills.
- If `$ARGUMENTS` includes user-provided priorities or carry-forward items, acknowledge them briefly and fold them into planning.
