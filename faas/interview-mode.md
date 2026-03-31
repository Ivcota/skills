# Interview Mode

When the user activates **interview mode** (e.g., "faas interview mode", "no codebase access", "interview mode"), the agent replaces codebase exploration with structured interviews. All four phases still apply with the same exit gates — only the input method changes.

**Key principle:** The agent never uses Glob, Grep, or Read to explore the codebase. All context comes from interviewing the user.

---

## Phase 1: Find (Interview)

### Process

1. **Derive the slug.** Same as standard mode.

2. **Parse the input.** Extract feature intent from whatever the user provides.

3. **Interview for context.** Replace codebase exploration with a structured interview. Start broad, then drill into gaps.

   **Opening question:** Ask the user to walk you through what happens when a user triggers this feature — end to end, in their own words.

   **Track coverage internally.** As the user talks, map their answers to these five areas. Drill into whichever areas are missing or thin:

   | Area | What you need to know | Example drill questions |
   |------|----------------------|------------------------|
   | **Entry points (L5)** | Every way this feature gets triggered | "Is this a button click? API call? Cron job? Are there multiple entry points?" |
   | **Exit points (L4)** | Every external system touched | "Does this hit a database? Third-party API? File system? Message queue?" |
   | **Data flows** | What comes in, what goes out, what transforms happen | "What data does the user submit? What shape? What gets persisted vs. returned?" |
   | **Existing patterns** | How the codebase currently handles similar work | "What framework are you using? ORM? How do similar features in your codebase work?" |
   | **Constraints** | Tech stack, auth, conventions, non-functional requirements | "Any auth requirements? Rate limits? Conventions I should follow?" |

   **Interview style:** One question at a time. Follow the most interesting thread. Resolve each branch before moving on. Don't dump a checklist — have a conversation.

4. **List scenarios.** Same as standard — Given/When/Then acceptance criteria for each scenario.

5. **Gap questions.** Same as standard — only ask what can't be derived from prior answers.

6. **Confirm before writing.** Present slug, feature goal, entry points, exit points, data flows, and scenario list. Wait for explicit approval before writing `find.md`.

**Exit gate:** Same as standard — all entry points listed, every scenario has an AC, you can answer "what does done look like?"

---

## Phase 2: ARCH (Interview)

### Process

1. **Draft first.** Using everything learned in Phase 1, the agent proposes:
   - Doings and knowings
   - Role assignments (stereotype + layer)
   - CRC cards
   - Collaboration design
   - File list (based on user-described project structure and patterns)
   - Implementation steps

2. **Grill to validate.** Present each section and challenge the user:
   - "I'm assuming X coordinates between Y and Z — is that right, or does something else own that?"
   - "I have this as a Service Provider at L1 — does your codebase have an existing pattern for this?"
   - "I'm proposing this file at `src/services/` — does that match your project structure?"
   - Resolve disagreements before moving on.

3. **Confirm before writing.** Same as standard — present the full arch, wait for approval before writing `arch.md`.

**Exit gate:** Same as standard — every component named with stereotype + layer, CRC cards complete, file list complete, steps ordered.

---

## Phase 3: Automate (Interview)

### Process

1. **Interview for testing setup.** Before producing any test code, grill the user:
   - "What test runner do you use?" (Jest, Vitest, pytest, Go testing, etc.)
   - "Where do tests live? Next to source? Separate `tests/` directory?"
   - "Any test utilities, factories, or helpers I should know about?"
   - "How do you handle test databases or external service mocks?"
   - "Any testing conventions or patterns your team follows?"

2. **Confirm the test map.** Same as standard — one row per scenario with test file, test type, what it asserts. Wait for approval.

3. **Produce copy-paste-ready code.** Write `automate.md` containing:
   - The test map
   - Stub implementations (signatures only, hardcoded dummies) tailored to user's stack and patterns
   - Failing test code tailored to user's test framework and conventions
   - File paths matching user's described project structure

4. **Document assumptions.** Note anything the agent assumed about the codebase that the user should verify.

**Exit gate:** Every Find scenario has a test in the document. All code is tailored to the user's described stack. User confirms the output is usable.

### Artifact changes

The `automate.md` artifact in interview mode includes additional sections:

```markdown
# Automate: {feature name}

## Test Map
| Scenario (from Find) | Test file | Test type | Asserts |
|----------------------|-----------|-----------|---------|

## Stub Implementations
### {file path}
\`\`\`{language}
{stub code}
\`\`\`

## Failing Tests
### {test file path}
\`\`\`{language}
{test code}
\`\`\`

## Assumptions to Verify
- {assumption}: {what to check}
```

---

## Phase 4: STR (Interview — Coaching Mode)

### Process

The agent acts as a **pair programming coach**. The user runs tests and writes code in their own environment. The agent guides them through the red-green-refactor loop.

1. **Pick a scenario.** Agent suggests which scenario to tackle first (usually the simplest or most foundational).

2. **Red.** User runs the failing test from Phase 3. If they hit setup issues, the agent helps debug based on error messages the user shares.

3. **Green.** Agent coaches the user toward the minimum implementation:
   - "What's the simplest thing that could make this pass?"
   - If the user pastes errors, the agent diagnoses and suggests fixes.
   - If the user pastes their implementation, the agent reviews it.

4. **Refactor.** Only after green. Agent asks:
   - "Anything you'd clean up now that it's green?"
   - "Any duplication worth extracting?"
   - Reviews refactoring the user proposes or performs.

5. **Next scenario.** Confirm the test passes, then move to the next scenario.

**Exit gate:** Same as standard — every Find scenario passes. User confirms working software.

### Coaching style

- One scenario at a time. Don't jump ahead.
- Ask what the user is seeing, don't assume.
- When the user pastes code or errors, respond to what's in front of you.
- Keep suggestions concrete and specific to their stack.
- If the user gets stuck, offer a specific next step, not a general strategy.
