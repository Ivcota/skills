# Story Map Workshop Checklist

Use this worksheet to run a story mapping session or audit an existing map.

---

## Pre-Session Setup

- [ ] **Define the target outcome.** One sentence: "We want [user type] to [do/achieve X] by [when]."
- [ ] **Identify participants.** Small cross-functional group: PM, 1-2 engineers, designer, and someone who knows users (researcher, CSM, or a user directly). 4-6 people is ideal.
- [ ] **Prepare the wall.** Large continuous surface (physical wall or digital board). Horizontal axis = user sequence. Vertical axis = priority.
- [ ] **Materials ready.** Index cards or sticky notes in 2-3 colors (one per row level), markers, tape.

---

## Building the Backbone (Step 1-2)

- [ ] Ask: "If we watched a user accomplish their goal from start to finish, what would we see them doing?"
- [ ] Write activities on cards — one per card, short goal-level phrase.
- [ ] Cluster related actions. Each cluster = one backbone activity.
- [ ] Sequence activities left to right as the user encounters them.
- [ ] Check: Are activities stated from the user's perspective (not the system's)?
- [ ] Check: Does walking the backbone left to right tell the user's story?

---

## Breaking Down the Backbone (Step 3-4)

- [ ] For each activity, write the tasks users perform to accomplish it.
- [ ] Place tasks below their parent activity, top-to-bottom by importance.
- [ ] Add edge cases, failures, and alternatives below the primary tasks.
- [ ] Check breadth before depth: have all backbone activities been broken down before going deep on any one?

---

## Discovery and Validation (Step 5-6)

- [ ] Is there an as-is map? (Current user behavior — not what the product should do)
- [ ] Is the to-be map built from research, not assumptions?
- [ ] Identify the top 3 riskiest cards (assumptions that, if wrong, invalidate the most work).
- [ ] Design an MVPe for each risky assumption before committing to build.

---

## Slicing (Step 5)

- [ ] Define the outcome for release 1 in one sentence.
- [ ] Walk the map and mark tasks that contribute to that outcome.
- [ ] Draw the release line horizontally.
- [ ] Verify: Is there at least one task above the line in each backbone activity?
- [ ] Challenge everything above the line: "Does deferring this prevent the outcome?"
- [ ] Optional: Draw Good/Better/Best lines for three release options.

---

## Delivery Planning (Step 7)

- [ ] Identify Opening game tasks: essential, cross-cutting, and risky.
- [ ] Estimate at the task level (not activity level).
- [ ] Check that Opening game tasks ship in sprint 1 or 2.
- [ ] Confirm Endgame tasks are not being built before Midgame is complete.

---

## Story Map Health Audit

For an existing map or backlog:

| Check | Pass | Fail | Fix |
|-------|------|------|-----|
| Backbone states user activities, not features | Activities = user goals | Activities = system features | Rewrite as user goal phrases |
| Map is horizontal, not a flat list | 2D grid visible | Linear priority list | Add the backbone as top row |
| Each column has a priority order | Most important tasks at top | Random ordering | Sort each column top to bottom by importance |
| At least one release line is drawn | Line exists | No line = no release strategy | Draw the walking skeleton line |
| Release line is horizontal (crosses all columns) | Crosses all backbone activities | Covers only some activities | Extend or redraw the line |
| Stories have been through 3 Cs conversation | Acceptance criteria exist and are testable | Cards have long descriptions but no confirmations | Run conversation sessions; write Given/When/Then criteria |
| Riskiest assumptions are identified | Team can name the top 3 risky cards | No one can name them | Run a risk identification session |

---

## Common Mistakes to Check For

- [ ] Backbone has 20+ items → Cluster into higher-level activities
- [ ] No as-is map exists → Run a current-state mapping session before next planning
- [ ] Stories written without a conversation → Schedule 3 Cs sessions
- [ ] Release slice is vertical (one column fully built) → Redraw as horizontal
- [ ] Team is estimating at the activity level → Break down to tasks before estimating
