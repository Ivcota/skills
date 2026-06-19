---
name: invest-framework
description: Apply the INVEST framework to make tasks, issues, user stories, backlog items, goals, and implementation slices clear, small, and actionable. Use when the user mentions INVEST, independent, negotiable, valuable, estimable, small, testable, user stories, backlog refinement, issue quality, task slicing, acceptance criteria, or asks to improve any task before execution.
---

# INVEST Framework

Use INVEST to improve any unit of work before planning or execution: user stories, issues, goals, implementation tasks, PR slices, research tasks, documentation work, and personal work items.

## Quick Start

Run this loop:

1. Restate the task in one sentence.
2. Check it against INVEST.
3. Name the weakest letters.
4. Rewrite or split it.
5. Add confirmation criteria.

```md
Task: [clear task statement]
INVEST check:
- Independent: [pass/fail + why]
- Negotiable: [pass/fail + why]
- Valuable: [pass/fail + why]
- Estimable: [pass/fail + why]
- Small: [pass/fail + why]
- Testable: [pass/fail + why]
Rewrite:
[improved task]
Confirmation:
- [observable check]
- [observable check]
```

## The Six Checks

- **Independent:** Can this be worked, reviewed, and delivered without unrelated work? Fix dependency knots by splitting setup, core behavior, and follow-up tasks.
- **Negotiable:** Does it state the outcome without over-prescribing implementation? Fix by separating hard constraints from suggested approach.
- **Valuable:** Who benefits, and what changes after it is done? Fix by naming the user, stakeholder, system, or learning value.
- **Estimable:** Can a capable person size it without guessing hidden scope? Fix by adding context, examples, constraints, links, or a spike.
- **Small:** Can it be completed in one focused pass or normal iteration? Fix by slicing vertically to the thinnest useful outcome.
- **Testable:** Can a reviewer tell whether it is done? Fix by adding observable acceptance criteria or verification steps.

## Rewrite Patterns

### User Story

```md
As a [user/persona],
I want [capability],
so that [outcome/value].
Acceptance criteria:
- Given [state], when [action], then [observable result].
- Given [edge case], when [action], then [observable result].
```

### Engineering Issue

```md
Implement [capability] for [specific workflow] so [user/system outcome].
Scope:
- In: [included behavior]
- Out: [explicitly excluded behavior]
Acceptance criteria:
- [observable behavior]
- [test or verification path]
```

### Research Or Spike Task

```md
Answer [specific question] so we can decide [decision].
Constraints:
- Timebox: [duration]
- Inspect: [systems/docs/users/data]
Deliverable:
- Recommendation
- Evidence
- Risks and unknowns
```

## Slicing Guide

When a task fails Small or Independent, split by:

- **Workflow step:** create, edit, delete, export, notify.
- **User role:** admin, member, guest, support.
- **Data state:** empty, normal, invalid, migrated, archived.
- **Risk:** prove API access, implement happy path, then handle edge cases.
- **Surface:** backend endpoint, UI integration, analytics, docs.
- **Outcome:** first useful behavior, then refinements.

Prefer vertical slices that produce observable value over horizontal slices that only finish a layer.

## Response Style

Lead with the weakest letters. Do not force every task into user-story format. Preserve the user's intent while tightening scope. If execution is next, produce the improved task plus the first concrete next step.
