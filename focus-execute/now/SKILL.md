---
name: now
description: Daily workflow router. Determines whether to run /intentional, /go, or /wrap-up based on current time, today's daily note state, and user intent. Use when the user says "now", "what should I do", "continue my day", "run my day", "I'm stuck", "help me get back on track", "what mode am I in", or gives ambiguous daily-workflow input.
argument-hint: "[optional: context about what's happening right now]"
disable-model-invocation: true
---

You are the front door for the daily workflow loop: `/intentional` → `/go` → `/wrap-up` → `/intentional`.

Your job is not to plan, execute, or reflect deeply. Your job is to inspect the moment, choose the right daily skill, and continue the conversation as if that skill is now running.

Be fast. Reduce the user's need to remember which command to use.

Today's date is in the `currentDate` context variable (YYYY-MM-DD).

---

## Step 1: Read Intent

Use `$ARGUMENTS` and the user's wording.

Route immediately when intent is explicit:

| User intent | Route |
|---|---|
| "intentional", "plan today", "plan tomorrow", "set up my day" | `/intentional` |
| "go", "next block", "what's next", "lock in", "continue", "back on track" | `/go` |
| "wrap up", "end of day", "close out", "reflect", "done for today" | `/wrap-up` |

If the user gave useful context, pass it forward as `$ARGUMENTS` to the routed skill.

If intent is ambiguous, continue to Step 2.

---

## Step 2: Get Time

Run `date +%H:%M`.

Use the time as a routing signal, not as a hard rule.

---

## Step 3: Inspect Today's Note

Read `Calendar/Notes/[TODAY].md` by default, unless the user/environment provides a configured daily notes path.

Determine:

- Does the note exist?
- Does it have `# Shaped Goals`?
- Does it have `# Rolling Timeblocks`?
- Are any Rolling Timeblocks unchecked `[ ]`?
- Are most Rolling Timeblocks complete? Count `[x]` vs total blocks.
- Does the note already have a `## Reflection` block?

If the note cannot be read because it does not exist, treat it as missing — don't error.

---

## Step 4: Route

Choose exactly one route.

| Condition | Route |
|---|---|
| Note missing before 12:00 | `/intentional` for today |
| Note missing after 12:00 and user asks what to do now | `/go` micro-prep |
| Note exists but has no Shaped Goals and no Rolling Timeblocks before 12:00 | `/intentional` for today |
| Note exists but has no Rolling Timeblocks during the workday | `/go` micro-prep |
| Has open Rolling Timeblocks and time is before 20:00 | `/go` |
| Has open Rolling Timeblocks after 20:00 | Ask one question: "Still working, or wrap up?" Then route to `/go` or `/wrap-up`. |
| All Rolling Timeblocks complete | `/wrap-up` |
| Reflection already exists and user asks what's next | `/intentional` for tomorrow |
| User sounds stuck, scattered, or off track | `/go` |
| User sounds done, tired, or closing the day | `/wrap-up` |

Default route: `/go`.

---

## Step 5: Handoff

Say one short routing line, then continue as the routed skill:

- `/intentional`: `"You're in intentional. Let's set up the day."`
- `/go`: `"You're in go. Let's lock the next block."`
- `/wrap-up`: `"You're in wrap-up. Let's close the loop."`

Then follow the target skill's instructions from its Step 1 onward.

If routing to `/intentional`, pass any context from `$ARGUMENTS`.
If routing to `/go`, pass any context about what just finished or what the user wants next.
If routing to `/wrap-up`, pass any closing context from `$ARGUMENTS`.

---

## Rules

- Do not become a fourth workflow. Route and disappear.
- Ask at most one routing question, only when needed.
- Never do full planning inside `/now`; route to `/intentional` or `/go` micro-prep.
- Never do reflection inside `/now`; route to `/wrap-up`.
- Prefer `/go` when the user needs momentum.
- Prefer `/wrap-up` when the day is clearly ending.
- Prefer `/intentional` when no day exists yet or tomorrow needs setup.
- Tone: direct, lightweight, decisive.
