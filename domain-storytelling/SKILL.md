---
name: domain-storytelling
description: Capture domain stories through collaborative interviews and generate pure domain layer code from them.
---

# domain-storytelling

A two-phase skill for Domain Storytelling (Hofer & Schwentner). Phase one interviews the user to capture a domain story as a structured YAML file. Phase two reads all captured stories and generates a pure domain layer directly into the codebase.

## When to use

- When the user runs `/domain-storytelling capture` to record a new domain story
- When the user runs `/domain-storytelling generate` to produce domain layer code from existing stories
- When the user runs `/domain-storytelling` with no arguments to see help

## Arguments

This skill accepts a subcommand as its argument:

- `capture` — Start a domain storytelling interview session
- `generate` — Generate domain layer code from existing stories
- No argument — Show available subcommands and a brief description of each

## Storage

All domain stories are saved as YAML files in `domain-stories/` at the project root. Create this directory if it does not exist.

### YAML Schema

Each story file follows this structure:

```yaml
name: customer-places-order
description: A customer browses the catalog and places an order
type: to-be # or as-is
granularity: fine # or coarse

actors:
  - name: Customer
    type: person # person | group | system
  - name: Inventory System
    type: system

work_objects:
  - name: Order
    contains:
      - Order Item
  - name: Catalog
  - name: Payment

activities:
  - number: 1
    actor: Customer
    verb: browses
    work_object: Catalog
  - number: 2
    actor: Customer
    verb: adds
    work_object: Order Item
    target_actor: null
  - number: 3
    actor: Customer
    verb: submits
    work_object: Order

annotations:
  - target: Order
    note: "Must contain at least one Order Item"

groups:
  - name: Shopping
    activities: [1, 2]
  - name: Checkout
    activities: [3]
```

File naming convention: kebab-case matching the story name (e.g., `customer-places-order.yaml`).

---

## Phase A: Capture (`/domain-storytelling capture`)

### Goal

Interview the user (the domain expert) to capture one concrete domain story per session.

### Instructions

1. **Read existing stories.** Before starting, read all YAML files in `domain-stories/` to understand the current domain context. Reference existing actors, work objects, and terminology to maintain consistency.

2. **Set the frame.** Ask the user:

   - What scenario do you want to describe? (one concrete example, not an abstract process)
   - Is this AS-IS (how it works today) or TO-BE (how it should work)? Default to TO-BE if not specified.
   - Is this coarse-grained (high-level flow) or fine-grained (detailed steps)? If not specified, infer from the level of detail the user provides.

3. **Let the user narrate.** Ask the user to describe the scenario in their own words, step by step. Do not interrupt the initial narrative. Let them speak naturally.

4. **Extract and probe.** After the initial narrative:

   - Identify the actors, work objects, and activities from what they said.
   - Present your understanding back to them as a numbered sequence (e.g., "1. Customer submits Order, 2. System validates Payment...").
   - Ask targeted follow-up questions to fill gaps:
     - "Who initiates this?" (missing actors)
     - "What exactly are they working with here?" (vague work objects)
     - "What happens between step N and step M?" (missing activities)
     - "Are there any rules or constraints on this?" (annotations)
     - "Does this belong to a different team or department than the previous steps?" (groups)
   - If this is a fine-grained story, push for more detail. If coarse-grained, accept higher-level descriptions.

5. **Confirm the story.** Present the complete domain story to the user in a readable numbered format. Ask them to confirm or correct it.

6. **Save the YAML file.** Write the confirmed story to `domain-stories/<story-name>.yaml`. If the `domain-stories/` directory does not exist, create it.

### Cross-story consistency

When capturing a new story, compare actors and work objects against existing stories. If the user introduces a term that is similar but not identical to an existing one (e.g., "Client" vs "Customer"), ask whether these are the same concept or intentionally different.

---

## Phase B: Help (no arguments)

When the user runs `/domain-storytelling` with no arguments, display:

```
Domain Storytelling — capture domain knowledge, generate domain code.

Subcommands:
  capture   — Interview to capture a new domain story as YAML
  generate  — Generate domain layer code from all captured stories

Stories are saved to domain-stories/ as YAML files.
```

---

## Phase C: Generate (`/domain-storytelling generate`)

### Goal

Read all domain stories from `domain-stories/` and generate a pure domain layer directly into the codebase.

### Instructions

1. **Read all stories.** Load every YAML file from `domain-stories/`. If the directory does not exist or is empty, tell the user to run `/domain-storytelling capture` first.

2. **Validate stories.** Check for issues across all stories:

   - **Auto-fix minor issues** silently: casing inconsistencies, whitespace, missing optional fields.
   - **Flag major conflicts** to the user and ask for resolution before proceeding: same-named actors with different types, work objects that appear to be the same concept under different names, contradictory activities.

3. **Detect the project language.** Explore the codebase to determine the primary language and conventions in use (file structure, naming conventions, module patterns). Generate code that feels native to the existing project.

4. **Synthesize the domain model.** Across all stories, identify:

   - **Bounded contexts** — from groups and natural language boundaries where the same term takes on different meanings.
   - **Aggregates** — work objects that are always created or modified together.
   - **Entities** — actors and work objects with identity and lifecycle.
   - **Value objects** — work objects or attributes without independent identity.
   - **Domain events** — activities that trigger downstream activities, especially across group boundaries.
   - **Commands** — activities initiated by actors that change state.

5. **Generate the domain layer.** Produce code for:

   - Entities with their properties and identity
   - Value objects with equality semantics
   - Aggregates with their boundaries and invariants
   - Domain events with their payloads
   - Repository interfaces (not implementations)
   - Keep it pure domain — no infrastructure, no frameworks, no database concerns.

6. **Place the code.** Determine the correct location in the existing codebase based on project structure and conventions. If the project has no existing domain layer structure, create a sensible one consistent with the project's patterns.

7. **Report what was generated.** After generating, give the user a summary of what was created and where it was placed.
