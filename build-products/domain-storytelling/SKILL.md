---
name: domain-storytelling
description: |
  Capture domain stories through collaborative interviews and generate pure domain layer code from them.
  Two phases: capture (interview to YAML) and generate (YAML to domain code).
  Use when user says "domain storytelling", "capture a domain story", "generate domain layer",
  "let's model the domain", or runs /domain-storytelling with capture or generate subcommands.
---

# Domain Storytelling

A two-phase skill for Domain Storytelling (Hofer & Schwentner). Phase one interviews the user to capture a domain story as structured YAML. Phase two reads all stories and generates a pure domain layer into the codebase.

References: [Capture Process](CAPTURE.md) | [Generate Process](GENERATE.md) | [YAML Schema](SCHEMA.md)

## Arguments

- `capture` — Start a domain storytelling interview session
- `generate` — Generate domain layer code from existing stories
- No argument — Show subcommands and descriptions

## Storage

All domain stories are saved as YAML files in `domain-stories/` at the project root. Create this directory if it does not exist. File naming: kebab-case matching the story name (e.g., `customer-places-order.yaml`).

## Phase 1: Capture (`/domain-storytelling capture`)

Interview the user (the domain expert) to capture one concrete domain story per session. See [full process](CAPTURE.md).

1. Read existing stories in `domain-stories/` for context and consistency
2. Set the frame — scenario, AS-IS vs TO-BE, granularity
3. Let the user narrate the scenario in their own words
4. Extract actors, work objects, activities — present back as numbered sequence
5. Probe for gaps: missing actors, vague work objects, skipped steps, constraints
6. Confirm the complete story with the user
7. Save to `domain-stories/<story-name>.yaml` using the [YAML schema](SCHEMA.md)

**Cross-story consistency:** Compare new terms against existing stories. If a term is similar but not identical to an existing one (e.g., "Client" vs "Customer"), ask whether they are the same concept.

## Phase 2: Generate (`/domain-storytelling generate`)

Read all domain stories and generate a pure domain layer. See [full process](GENERATE.md).

1. Load all YAML files from `domain-stories/` (if empty, tell user to capture first)
2. Validate stories — auto-fix minor issues, flag major conflicts for resolution
3. Detect project language and conventions
4. Synthesize: bounded contexts, aggregates, entities, value objects, domain events, commands
5. Generate pure domain code — no infrastructure, no frameworks
6. Place code according to existing project structure
7. Report what was generated and where

## Help (no arguments)

When run with no arguments, display:

```
Domain Storytelling -- capture domain knowledge, generate domain code.

Subcommands:
  capture   -- Interview to capture a new domain story as YAML
  generate  -- Generate domain layer code from all captured stories

Stories are saved to domain-stories/ as YAML files.
```
