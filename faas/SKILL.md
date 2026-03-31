---
name: faas
description: |
  Four-phase engineering framework for shipping features with confidence: Find → ARCH → Automate → Specify-Test-Refine.
  Each phase has a required input, a guided process, and an exit gate you must pass before advancing.
  Integrates Responsibility-Driven Design and the 54321 layered architecture model.
  Supports interview mode for when the user doesn't want to provide codebase access — the agent interviews instead of exploring.
  Use when the user wants to plan and build a feature, says "help me ship this", "let's plan this out",
  "walk me through building this", or provides a ticket, PRD, design, or feature request.
  Also triggers on "interview mode", "no codebase access", or "faas interview".
---

# FAAS — Find, ARCH, Automate, Specify-Test-Refine

A four-phase engineering framework for shipping features with confidence. Each phase has a required input, a guided process, and an exit gate. **You do not advance to the next phase until the exit gate is satisfied.**

References: [54321 Layer Model](54321.md) | [RDD Stereotypes](rdd.md) | [Phase Details & Artifacts](phases.md) | [Interview Mode](interview-mode.md)

## Mode Detection

**Standard mode** (default): Agent explores the codebase to discover entry points, patterns, and context.

**Interview mode**: Activated when the user says "interview mode", "no codebase access", "faas interview", or similar. The agent interviews the user instead of exploring code. Do not use Glob, Grep, or Read for codebase exploration. All context comes from the conversation. See [Interview Mode](interview-mode.md) for full process.

## Input Detection

Accepts: inline text, file path, URL, or design/screenshot. Identify the form and extract feature intent before Phase 1.

## Artifacts

Each run is scoped to a **feature slug** — slugify the first 4-6 significant words to kebab-case. Save artifacts under `./faas/{slug}/` at the project root.

| Phase | Artifact | Phase | Artifact |
|-------|----------|-------|----------|
| Find  | `find.md` | ARCH | `arch.md` |
| Automate | `automate.md` | STR | (tests go green) |

## Phase 1: Find

Build enough context to see the full target before writing a single line. See [full process](phases.md#phase-1-find).

1. Derive the slug and create `./faas/{slug}/`
2. Parse input — extract user goal, UI flows, API calls, data
3. Explore codebase — identify [L4 and L5](54321.md) entry points
4. List scenarios with acceptance criteria (Given/When/Then)
5. Ask targeted gap questions (one at a time, only what code can't answer)
6. **Confirm with user before writing `find.md`**

**Exit gate:** All entry points listed | Every scenario has an AC | You can answer "what does done look like?"

## Phase 2: ARCH

Decide exactly what you're building and how before touching code. See [full process](phases.md#phase-2-arch).

1. [RDD](rdd.md): enumerate doings/knowings → assign stereotypes → produce CRC cards → design collaborations
2. Map everything to [54321 layers](54321.md)
3. List every file to create/modify, define patterns (no TBDs), note out-of-scope
4. Order implementation steps
5. **Confirm with user before writing `arch.md`**

**Exit gate:** Every component named with stereotype + layer | CRC cards complete | File list complete | Steps ordered

## Phase 3: Automate

Prove the architecture works and define the failure target. See [full process](phases.md#phase-3-automate).

1. **Confirm test map with user** before scaffolding
2. Scaffold stubs (signatures only, no real logic)
3. Scaffold failing tests at appropriate [testing boundaries](54321.md)
4. Verify the walking skeleton runs end-to-end
5. Document weirdness in `automate.md`

**Exit gate:** Every Find scenario has a failing test | Skeleton runs E2E | All weirdness documented

## Phase 4: Specify-Test-Refine (STR)

Make every test green, one scenario at a time. See [full process](phases.md#phase-4-specify-test-refine-str).

Red → Green → Refactor, per scenario. Do not refactor during red. Do not add scope not in Find.

At handoff, ask: **(A)** User implements, or **(B)** agent implements scenario-by-scenario with review.

**Done when:** Every Find scenario passes | No tests skipped without documented reason | Working software ships

## The Loop Closes

STR stops when all Find scenarios are green. If a test doesn't map to a Find scenario, walk it back to `find.md`.
