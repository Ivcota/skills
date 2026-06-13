---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

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

### 8. Recommended Next Step
- ...
```

Rules:

- Only list decisions explicitly confirmed by the user under "Decisions Made".
- Put unconfirmed recommendations under "Open Questions" or "Recommended Next Step".
- Keep the headings, order, and table columns stable every time.
- Use stable IDs: `D-001`, `Q-001`, `R-001`.
- If a section has no items, write `None`.

Once you have no more questions and have produced the Grill Session Card, DO NOT START IMPLEMENTATION without user permission. Instead, prompt the user for a next step.
