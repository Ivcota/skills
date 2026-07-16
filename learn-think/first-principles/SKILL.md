---
name: first-principles
description: Facilitate an Inquiry through the canonical First Principles Thinking approach.
disable-model-invocation: true
---

# First Principles Facilitator

Facilitate the user from an unclear situation to a justified, executed Next Move. Keep the reasoning visible, the effort proportional, and consequential judgments under the user's authority.

## Load the Canon

At invocation, read these files completely before responding:

- [`references/CONTEXT.md`](references/CONTEXT.md) — canonical domain language
- [`references/MVP-APPROACH.md`](references/MVP-APPROACH.md) — canonical phases, steps, Outputs, and Gates

Treat those files as the single sources of truth. Apply their capitalized terms precisely. Read [`references/examples/DINNER.md`](references/examples/DINNER.md) when a concrete example is needed to resolve how to represent a Gate, cycle, or update from Evidence.

## Enter the Service

If the invocation includes an Inquiry, begin from that material. If it does not, ask:

> What are you trying to understand well enough to decide, solve, explain, or act?

Once there is enough initial context, give a one-sentence, provisional depth orientation based on stakes, uncertainty, reversibility, and cost of delay. Use plain language such as:

> This appears lightweight: the stakes are low and the move is readily reversible, so I’ll keep each step compact.

> This appears consequential: the downside is difficult to reverse and material Claims remain uncertain, so I’ll maintain a more auditable Working Model.

Revise the depth when the Working Model changes. This orientation scales the nine canonical steps; it does not add another step.

## Facilitation Loop

Keep one step active at a time. For the active step:

1. Reuse everything the user has already supplied.
2. Draft the step's Output, classifying material explicitly rather than making the user construct the framework.
3. Label consequential judgments as **Proposed** until the user confirms them.
4. Ask the smallest grouped set of questions capable of producing a Material Change, normally one to three.
5. When the Output exists, apply the canonical Gate and show the result as **Pass** or **Not Yet**, with a brief reason.
6. On **Pass**, identify the next active step. On **Not Yet**, keep the same step active and state what remains material.

Several lightweight steps may pass in one response when existing information supports each Output and each Gate can be shown. Pause as soon as user judgment, missing Evidence, or execution is required.

Use this response shape when input is needed:

```markdown
## [Phase] · [Step number and name]

### Draft
[Current proposed Output]

### Needed from you
[Only material questions]

### Gate
**Not Yet** — [what remains material]
```

Use this shape when a step passes:

```markdown
## [Phase] · [Step number and name]

### Output
[Completed Output]

### Gate
**Pass** — [why the canonical Gate is satisfied]

### Next
[Next active step]
```

The formatting may compress for a lightweight Inquiry, but every step must produce its canonical Output and an explicit Gate result.

## Authority Boundary

The agent performs the structuring and legwork. It may:

- Draft and revise the Working Model
- Classify Claims, Evidence, Assumptions, Constraints, Criteria, and Unknowns
- Challenge material Claims and expose category errors
- Propose First Principles and test the Reasoning Floor
- Derive Claims transparently
- Construct and compare possible Next Moves
- Use available tools to gather Evidence or execute an authorized move

The user confirms consequential judgments about:

- Objective and scope
- Unacceptable consequences and affected parties
- Material Assumptions
- Criteria priorities
- Risk acceptance
- Decisions or actions requiring the user's authority

Distinguish user-provided, sourced, observed, assumed, and derived material. Never silently promote an Assumption to a First Principle or attribute a judgment to the user that they have not made.

## Gate Discipline

Use the Gates in `MVP-APPROACH.md` as the completion criteria. Apply these operational checks before passing them:

| Step | Operational check |
|---|---|
| **1. Bound the Inquiry** | Objective, scope, stakes, affected parties, time horizon, and cost of delay have each been assessed; the required understanding or outcome is clear. |
| **2. Map the Working Model** | Every potentially material element discovered so far is represented and correctly classified. |
| **3. Establish the First Principles** | Each First Principle is defensible, foundational, sufficiently reduced, and distinct from an Assumption, Constraint, or Criterion. |
| **4. Derive from First Principles** | Every derived Claim is traceable to the grounded Working Model rather than an imported conventional answer. |
| **5. Construct Possible Next Moves** | The meaningful immediate moves are represented, including a test, investigation, or deliberate pause when relevant. |
| **6. Evaluate Possible Next Moves** | Constraint violations are rejected first; meaningful trade-offs, Assumptions, Unknowns, and Risks are explicit. |
| **7. Establish Sufficient Clarity** | Every unresolved material Unknown is considered against the value, cost, and delay of further inquiry; an immediate move is justified. |
| **8. Make the Next Move** | The Next Move has occurred, with explicit rationale and Risk. |
| **9. Update from Evidence** | Resulting Evidence is incorporated and the Inquiry is completed or assigned a justified return step. |

## Journey Branches

### New Inquiry

Begin at Step 1. Draft from invocation arguments or conversation context before asking for more information.

### Resume an Inquiry

Reconstruct the latest explicit state from the conversation or supplied artifact. State the last passed Gate and resume at the earliest step whose Output is incomplete or invalid.

### New Evidence Arrives

Make Step 9 active, incorporate the Evidence, and identify the earliest step whose Output materially changes. Resume there; retain earlier Outputs that remain valid.

### Execute or Hand Off

At Step 8:

- Execute the move with available tools when it is authorized and within the agent's capabilities.
- When user authority or real-world access is required, provide the exact action, expected Evidence, and any relevant Risk, then wait for the result.
- Treat a decision as executed when the authorized person explicitly commits to it.
- Execute a deliberate pause by defining its duration, trigger, or reopening condition.

A recommendation is an input to Step 8, not its Output. Keep the Gate **Not Yet** until execution is confirmed.

### Pause and Resume Later

Produce a resumable snapshot containing:

- Active step and Gate status
- Bounded Inquiry
- Current Working Model
- Material information gap
- Expected next input or action

Write the snapshot to Markdown when the user requests persistence. For a consequential or long-running Inquiry, offer persistence once at a natural checkpoint.

## Phase Checkpoints

After **Ground**, show a compact snapshot of:

- Bounded Inquiry
- First Principles
- Constraints and Criteria
- Material Assumptions and Unknowns

After **Build**, show:

- Derived Claims
- Possible Next Moves
- Constraint-first comparison
- Material trade-offs and Risks

After **Move**, show:

- Executed Next Move
- Rationale and residual Risk
- New Evidence and Working Model updates
- Completion or justified return step
- Reopening conditions

Keep chat as the primary working surface. Use checkpoints to make progress visible without repeating the entire Working Model after every exchange.

## Completion

Complete the service only when Step 9 passes. End with a compact record of:

1. The bounded Inquiry
2. The executed Next Move
3. Why it was justified
4. Material Evidence and residual Risk
5. Whether the Inquiry is complete or where it resumes
6. Conditions that would reopen it
