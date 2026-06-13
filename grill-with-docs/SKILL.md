---
name: grill-with-docs
description: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions.
---

<what-to-do>

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

Ask the questions one at a time. Wait for the user's answer before continuing.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Question format

Every question must use this deterministic structure:

```md
Recognition: <briefly restate the last decision or clarification the user confirmed. Omit only for the first question if nothing has been confirmed yet.>

Question N: <single decision or clarification needed>

a) <option>
b) <option>
c) <option>
d) <option>

Recommendation: Choose <a|b|c|d>)

Why: <short rationale for the recommendation>
```

Rules:

- Always provide exactly four answer options: `a)`, `b)`, `c)`, and `d)`.
- Make options mutually exclusive when possible.
- Keep each question focused on one decision.
- Include the recommended answer every time.
- Recognition is a short restatement of what the user just confirmed, not a full decision log.

## Final artifact

When the interview is complete, produce a final **Grill Session Card** in chat using this exact structure:

```md
## Grill Session Card

### 1. Objective
- ...

### 2. Final Shape
- ...

### 3. Decisions Made
| ID | Decision | Rationale | Alternatives Rejected |
|---|---|---|---|
| D-001 | ... | ... | ... |

### 4. Constraints
- ...

### 5. Non-Goals
- ...

### 6. Open Questions
| ID | Question | Why It Matters | Suggested Next Step |
|---|---|---|---|
| Q-001 | ... | ... | ... |

### 7. Risks / Watchpoints
| ID | Risk | Mitigation / Watchpoint |
|---|---|---|
| R-001 | ... | ... |

### 8. Documentation Updates
| File | Change Made | Reason |
|---|---|---|
| ... | ... | ... |

### 9. Recommended Next Step
- ...
```

Rules:

- Only list decisions explicitly confirmed by the user under "Decisions Made".
- Put unconfirmed recommendations under "Open Questions" or "Recommended Next Step".
- Keep the headings, order, and table columns stable every time.
- Use stable IDs: `D-001`, `Q-001`, `R-001`.
- If a section has no items, write `None`.
- In "Documentation Updates", list only files actually changed during the session.

Once you have no more questions and have produced the Grill Session Card, DO NOT START IMPLEMENTATION without user permission. Instead, prompt the user for a next step.

</what-to-do>

<supporting-info>

## Domain awareness

During codebase exploration, also look for existing documentation:

### File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Create files lazily — only when you have something to write. If no `CONTEXT.md` exists, create one when the first term is resolved. If no `docs/adr/` exists, create it when the first ADR is needed.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` right there. Don't batch these up — capture them as they happen. Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

`CONTEXT.md` should be totally devoid of implementation details. Do not treat `CONTEXT.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).

</supporting-info>
