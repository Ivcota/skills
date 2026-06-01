---
name: my-habits
description: Finds active habit cards in this Obsidian vault and surfaces the right cue/action at the right time. Use when the user runs /my-habits, asks to review habits, find active habits, archive habits, or surface habit cards by day, schedule, cue, priority, or tag.
---

# My Habits

## Purpose

Surface habit cards from the vault as a short, actionable list focused on **cue -> action**.

## Habit card metadata

Prefer note-level frontmatter for machine-readable habits:

```yaml
tags:
  - habits
habit_status: active # active | archived
habit_cards:
  - id: door-to-door-confidence
    title: Door-to-Door Confidence
    status: active # active | archived
    priority: 90 # 0-100, higher first
    schedule: daily # daily, weekly, Tuesday, weekdays, etc.
    cue: Leaving any electronic device
    action: Say the AI opener once out loud
```

Rules:
- `status: active` habits are shown by default.
- `status: archived` habits are hidden unless the user asks for archived/all habits.
- A card with today's weekday or date in `schedule`, `cue`, `action`, or body gets boosted.
- Higher `priority` appears first after time/date relevance.

## When user runs `/my-habits`

Run from the vault root:

```bash
python3 .agents/skills/my-habits/scripts/find_habits.py
```

Then summarize the output. Keep it brief. Show:

1. Habit title
2. Cue
3. Action
4. Why surfaced now, if relevant
5. Source note

## Arguments

If the prompt includes extra words, map them like this:

- `all` or `include archived` -> pass `--include-archived`
- `archived` or `archive` -> pass `--status archived`
- `active` -> pass `--status active`
- `json` -> pass `--json`
- any other terms -> pass as `--query "terms"`

Examples:

```bash
python3 .agents/skills/my-habits/scripts/find_habits.py --include-archived
python3 .agents/skills/my-habits/scripts/find_habits.py --query Tuesday
```

## Archiving habits

To archive a habit, edit the note frontmatter:

```yaml
status: archived
```

inside the relevant `habit_cards` entry. If the whole note is archived, set:

```yaml
habit_status: archived
```
