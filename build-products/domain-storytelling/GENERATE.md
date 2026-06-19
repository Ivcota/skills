# Generate Process

Detailed instructions for generating a pure domain layer from captured stories.

## 1. Read All Stories

Load every YAML file from `domain-stories/`. If the directory does not exist or is empty, tell the user to run `/domain-storytelling capture` first.

## 2. Validate Stories

Check for issues across all stories:

- **Auto-fix minor issues** silently: casing inconsistencies, whitespace, missing optional fields.
- **Flag major conflicts** to the user and ask for resolution before proceeding: same-named actors with different types, work objects that appear to be the same concept under different names, contradictory activities.

## 3. Detect Project Language

Explore the codebase to determine the primary language and conventions in use (file structure, naming conventions, module patterns). Generate code that feels native to the existing project.

## 4. Synthesize the Domain Model

Across all stories, identify:

- **Bounded contexts** -- from groups and natural language boundaries where the same term takes on different meanings.
- **Aggregates** -- work objects that are always created or modified together.
- **Entities** -- actors and work objects with identity and lifecycle.
- **Value objects** -- work objects or attributes without independent identity.
- **Domain events** -- activities that trigger downstream activities, especially across group boundaries.
- **Commands** -- activities initiated by actors that change state.

## 5. Generate the Domain Layer

Produce code for:

- Entities with their properties and identity
- Value objects with equality semantics
- Aggregates with their boundaries and invariants
- Domain events with their payloads
- Repository interfaces (not implementations)

Keep it pure domain -- no infrastructure, no frameworks, no database concerns.

## 6. Place the Code

Determine the correct location in the existing codebase based on project structure and conventions. If the project has no existing domain layer structure, create a sensible one consistent with the project's patterns.

## 7. Report What Was Generated

After generating, give the user a summary of what was created and where it was placed.
