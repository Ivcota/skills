---
name: faas
description: |
  Four-phase engineering framework for shipping features with confidence: Find → ARCH → Automate → Specify-Test-Refine.
  Each phase has a required input, a guided process, and an exit gate you must pass before advancing.
  Integrates Responsibility-Driven Design and the 54321 layered architecture model.
  Use when the user wants to plan and build a feature, says "help me ship this", "let's plan this out",
  "walk me through building this", or provides a ticket, PRD, design, or feature request.
---

# FAAS — Find, ARCH, Automate, Specify-Test-Refine

A four-phase engineering framework for shipping features with confidence. Each phase has a required input, a guided process, and an exit gate. **You do not advance to the next phase until the exit gate is satisfied.**

---

## 54321 Layer Model

| Level | Layer                  | Description                                      |
| ----- | ---------------------- | ------------------------------------------------ |
| 5     | **Incoming / Driving** | Entry points: UI, API routes, CLI adapters       |
| 4     | **Outgoing / Driven**  | Adapters: Gateways, external APIs, databases     |
| 3     | **Application**        | Coordination: Use cases, Presenters              |
| 2     | **Stateful**           | Domain logic: models, entities, aggregates       |
| 1     | **Stateless**          | Pure functions: calculations, transformations    |

Dependencies point inward only — outer layers know about inner layers, never the reverse.

---

## Testing Boundaries

**The rule:** test at a layer by wiring everything *inward* (toward 1) for real, and stubbing everything *outward* (toward infrastructure) at the boundary.

| Level | Test type              | Wire real          | Stub at boundary                              |
| ----- | ---------------------- | ------------------ | --------------------------------------------- |
| 1     | Unit                   | — (no deps)        | Nothing — pure functions are fully isolated   |
| 2     | Domain unit            | Level 1            | Nothing — if L2 reaches outward, design smell |
| 3     | Use case integration   | Levels 1 & 2       | Level 4 ports (fakes / in-memory repos)       |
| 4     | Adapter contract       | The adapter itself | The external system (test DB, WireMock, etc.) |
| 5     | Slice integration      | Levels 1, 2, 3     | Level 4 adapters (same fakes as L3 tests)     |
| —     | E2E smoke              | Everything         | Nothing                                       |

**Key constraints:**

- **L3 and L5 share the same fakes.** The in-memory repo that tests use cases also powers slice tests. One fake, two layers.
- **L4 is the only layer that touches real infrastructure.** Not E2E. Not L5. DB migrations and adapter wiring get exercised here.
- **L2 requires no stubs by design.** If you need to stub to test a domain object, the domain object has the wrong dependencies.

---

## Input detection

The skill accepts any of the following as the feature input:

- **Inline text** — a description, ticket, or problem statement pasted directly
- **File path** — read the file (PRD, design doc, user stories)
- **URL** — fetch the page (GitHub issue, Linear ticket, Notion doc)
- **Design or screenshot** — analyze the image to infer UI entry points and user flows

When the skill starts, identify which form was provided and extract the feature intent before beginning Phase 1.

---

## Artifacts

Each faas run is scoped to a **feature slug** derived automatically from the feature description at the start of Phase 1. Slugify the first 4–6 significant words of the description to kebab-case (lowercase, strip punctuation, drop filler words like "a", "the", "with").

Save all phase artifacts under `./faas/{slug}/` at the project root. Create the directory if it does not exist.

| Phase     | Artifact file                    |
|-----------|----------------------------------|
| Find      | `./faas/{slug}/find.md`          |
| ARCH      | `./faas/{slug}/arch.md`          |
| Automate  | `./faas/{slug}/automate.md`      |

Phases 2–4 read the slug from the `slug:` frontmatter field in `./faas/{slug}/find.md`.

---

## Phase 1: Find

**Purpose:** Build enough context that you can see the full target before writing a single line.

### Process

1. **Derive the slug.** From the feature description, slugify the first 4–6 significant words to kebab-case (e.g., "Add OAuth login for users" → `oauth-login-users`). This slug names the run directory: `./faas/{slug}/`. Create the directory now.

2. **Parse the input.** Read the feature request, design, ticket, or screenshot. Extract:
   - The goal from the user's perspective
   - Any visible UI flows, API calls, or data referenced

3. **Explore the codebase.** Use Glob and Grep to identify entry points at levels 4 and 5 of the 54321 model:
   - **Level 5 (Incoming/Driving):** UI pages, API routes, CLI commands, webhooks, form actions
   - **Level 4 (Outgoing/Driven):** Repositories, gateways, external API calls, database writes

   For each entry point, note: who initiates it, what data flows through it, and which layer it belongs to.

4. **List scenarios.** Enumerate every distinct user-observable scenario this feature touches. For each scenario:
   - Write an acceptance criterion: "Given [context], when [action], then [outcome]"
   - Note which entry points are involved
   - Draft a test structure outline (test name, type, what it asserts)

5. **Ask targeted gap questions.** Only ask what cannot be derived from the codebase or input. One question at a time.

### Exit gate — do not enter ARCH until:
- [ ] All entry points are listed (Level 4 & 5)
- [ ] Every scenario has a written acceptance criterion
- [ ] You can answer "what does done look like?" without hesitation

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

### Scenario N: ...
```

---

## Phase 2: ARCH

**Purpose:** Decide exactly what you're building and how before touching code.

**Required input:** `./faas/{slug}/find.md` — read the `slug:` frontmatter field to locate the run directory.

### Process

1. **Responsibility Discovery (RDD).** For the feature as a whole, enumerate:
   - **Doings** — what must the system do? (behaviors, computations, persistence, coordination)
   - **Knowings** — what must the system know? (state, rules, configuration)

2. **Assign roles.** Map each responsibility to a stereotype:
   - **Information Holder (1-2)** — entities, value objects, DTOs, domain events
   - **Structurer (2)** — aggregates, collections, cache
   - **Service Provider (1)** — stateless domain services, utility classes
   - **Coordinator (3)** — event listeners, routers, input handlers
   - **Controller (3)** — use cases, interactors, application services, presenters
   - **Interfacer (4-5)** — repositories, HTTP servers, external API facades

3. **Map to 54321 layers.**
   ```
   Level 5 (Driving UI)
       ↓ uses
   Level 3 (Application/Coordination)
       ↓ uses                    ↓ uses
   Level 4 (Driven Infra)    Level 2 (Domain)
                                 ↓ uses
                             Level 1 (Pure functions)
   ```
   Place each role in a layer. Dependencies must point inward — inner layers never know about outer layers.

4. **Produce CRC Cards.** For each candidate object:
   - **Front:** name, purpose/role, patterns, stereotype
   - **Back:** responsibilities (knows / does / decides), collaborators

5. **Design collaborations.**
   - For each *doing* responsibility: "what role helps with this task?"
   - For each *knowing* responsibility: "what roles need to know this?"

6. **List every file to create or modify.** Be explicit about folder placement.

7. **Define patterns.** Name every pattern in use — from the codebase or newly introduced. No TBDs.

8. **Note scope.** Explicitly call out what is out of scope for this implementation.

9. **Order the implementation steps.** Produce an unambiguous ordered list.

### Exit gate — do not enter Automate until:
- [ ] Every component is named with a stereotype and layer
- [ ] CRC cards exist for every candidate object
- [ ] Every file to create/modify is listed
- [ ] Patterns are decided, not TBD
- [ ] Implementation steps are ordered and unambiguous

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

**Purpose:** Prove the architecture works and define the failure target before writing real logic.

**Required input:** `./faas/{slug}/arch.md` — read the slug from `./faas/{slug}/find.md` frontmatter to locate the run directory.

### Process

1. **Scaffold stub implementations.** For every file in the ARCH file change list:
   - Create the file with the class/function signatures but no real logic
   - Stubs return hardcoded dummies or throw `NotImplemented`

2. **Scaffold test files.** For every scenario in `./faas/{slug}/find.md`:
   - Create a corresponding test file
   - Write test descriptions and assertions against the acceptance criteria
   - Tests must fail (red) — no implementation yet
   - Test types to scaffold (see Testing Boundaries):
     - **Unit (L1)** — pure functions, stateless logic
     - **Domain unit (L2)** — entity and aggregate behavior, no stubs
     - **Use case integration (L3)** — application logic wired with fakes at the L4 boundary
     - **Adapter contract (L4)** — adapter wired against real infrastructure (test DB, WireMock)
     - **Slice integration (L5)** — entry point through domain, L4 faked
     - **E2E smoke** — full stack, nothing stubbed

3. **Verify the skeleton.** Confirm all components can be imported and wired together, even with dumb implementations. The walking skeleton runs end-to-end.

4. **Document any weirdness.** If you discover unexpected existing behavior, missing dependencies, or integration surprises — document them in `./faas/{slug}/automate.md` before proceeding.

### Exit gate — do not enter STR until:
- [ ] Every Find scenario has a corresponding failing test
- [ ] Walking skeleton runs end-to-end (even with stubs)
- [ ] No unknown unknowns — all weirdness is documented

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

**Purpose:** Make every test green, one scenario at a time.

**Required input:** Failing test suite from Automate.

### Process

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

### Done when:
- [ ] Every Find scenario has a passing test
- [ ] No tests are skipped or mocked out without documented reason
- [ ] Working software ships

---

## The Loop Closes

STR stops when all Find scenarios are green. If a test does not map to a Find scenario, you either drifted from scope or wrote the wrong test. Walk it back to `./faas/{slug}/find.md`.
