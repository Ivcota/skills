# Phase Details & Artifact Templates

## Phase 1: Find

### Full Process

1. **Derive the slug.** Slugify the first 4-6 significant words to kebab-case (e.g., "Add OAuth login for users" → `oauth-login-users`). Create `./faas/{slug}/`.

2. **Parse the input.** Extract:
   - The goal from the user's perspective
   - Any visible UI flows, API calls, or data referenced

3. **Explore the codebase.** Use Glob and Grep to identify entry points:
   - **Level 5 (Incoming/Driving):** UI pages, API routes, CLI commands, webhooks, form actions
   - **Level 4 (Outgoing/Driven):** Repositories, gateways, external API calls, database writes
   - For each: who initiates it, what data flows through it, which layer it belongs to.

4. **List scenarios.** For each user-observable scenario:
   - Write an acceptance criterion: "Given [context], when [action], then [outcome]"
   - Note which entry points are involved
   - Draft a test structure outline (test name, type, what it asserts)

5. **Ask targeted gap questions.** One at a time. Only ask what cannot be derived from code or input.

6. **Confirm before writing.** Present slug, feature goal, entry points, and scenario list. Wait for explicit approval.

### Minimum artifact: `./faas/{slug}/find.md`

```markdown
---
slug: {slug}
feature: {feature name}
---

# Find: {feature name}

## Entry Points
| Level | Location | Who initiates | Data flow |
|-------|----------|---------------|-----------|

## Scenarios
### Scenario 1: {name}
**AC:** Given..., when..., then...
**Entry points involved:**
**Test outline:** {test type} — {what it asserts}
```

---

## Phase 2: ARCH

### Full Process

1. **Responsibility Discovery (RDD).** Enumerate:
   - **Doings** — what must the system do? (behaviors, computations, persistence, coordination)
   - **Knowings** — what must the system know? (state, rules, configuration)

2. **Assign roles.** Map each responsibility to an [RDD stereotype](rdd.md) and [54321 layer](54321.md).

3. **Produce CRC Cards.** For each candidate object:
   - **Front:** name, purpose/role, patterns, stereotype
   - **Back:** responsibilities (knows / does / decides), collaborators

4. **Design collaborations.**
   - For each *doing*: "what role helps with this task?"
   - For each *knowing*: "what roles need to know this?"

5. **List every file** to create or modify. Explicit folder placement.

6. **Define patterns.** Name every pattern in use. No TBDs.

7. **Note scope.** Explicitly call out what is out of scope.

8. **Order implementation steps.** Unambiguous ordered list.

9. **Confirm before writing.** Present doings/knowings, role assignments, file list, and steps. Wait for approval.

### Minimum artifact: `./faas/{slug}/arch.md`

```markdown
# ARCH: {feature name}

## Responsibilities
### Doings
- {responsibility} → {role name} ({stereotype}, Level {N})

### Knowings
- {responsibility} → {role name} ({stereotype}, Level {N})

## CRC Cards
### {CandidateName}
**Front:** {purpose} | {stereotype} | Level {N}
**Knows:** ...
**Does:** ...
**Collaborators:** ...

## File Change List
- CREATE `src/...` — {purpose}
- MODIFY `src/...` — {what changes}

## Pattern Decisions
- {pattern name}: {decision}

## Out of Scope
- ...

## Implementation Steps (ordered)
1. ...
```

---

## Phase 3: Automate

### Full Process

1. **Confirm the test map before scaffolding.** Present one row per scenario: test file, test type, what it asserts. Wait for approval.

2. **Scaffold stub implementations.** For every file in the ARCH file change list:
   - Create with class/function signatures, no real logic
   - Stubs return hardcoded dummies or throw `NotImplemented`

3. **Scaffold test files.** For every scenario in `find.md`, create tests at the appropriate [testing boundary](54321.md):
   - **Unit (L1)** — pure functions, stateless logic
   - **Domain unit (L2)** — entity and aggregate behavior, no stubs
   - **Use case integration (L3)** — application logic wired with fakes at the L4 boundary
   - **Adapter contract (L4)** — adapter wired against real infrastructure (test DB, WireMock)
   - **Slice integration (L5)** — entry point through domain, L4 faked
   - **E2E smoke** — full stack, nothing stubbed
   - All tests must fail (red) — no implementation yet.

4. **Verify the skeleton.** All components import and wire together. Walking skeleton runs E2E.

5. **Document weirdness.** Unexpected behavior, missing deps, or integration surprises.

### Minimum artifact: `./faas/{slug}/automate.md`

```markdown
# Automate: {feature name}

## Test Map
| Scenario (from Find) | Test file | Test type | Status |
|----------------------|-----------|-----------|--------|
| {scenario name}      | {path}    | Unit/Int/E2E | FAILING |

## Weirdness Log
- {issue}: {description and impact}
```

---

## Phase 4: Specify-Test-Refine (STR)

### Full Process

Red → Green → Refactor, per scenario. Do not refactor during red. Do not add scope not in Find.

### Handoff

At the end of Automate, present the test map and ask:

```
Your failing test suite is ready. How do you want to handle STR?

A) I'll implement each scenario myself (Red → Green → Refactor)
B) You implement scenario by scenario — show me each cycle for review before moving on
```

If the user chooses **B**, work through one scenario at a time:
1. Show the failing test
2. Implement the minimum code to make it green
3. Refactor only after green — show the diff
4. Wait for user approval before moving to the next scenario
