# Capture Process

Detailed instructions for the domain storytelling interview session.

## 1. Read Existing Stories

Before starting, read all YAML files in `domain-stories/` to understand the current domain context. Reference existing actors, work objects, and terminology to maintain consistency.

## 2. Set the Frame

Ask the user:

- What scenario do you want to describe? (one concrete example, not an abstract process)
- Is this AS-IS (how it works today) or TO-BE (how it should work)? Default to TO-BE if not specified.
- Is this coarse-grained (high-level flow) or fine-grained (detailed steps)? If not specified, infer from the level of detail the user provides.

## 3. Let the User Narrate

Ask the user to describe the scenario in their own words, step by step. Do not interrupt the initial narrative. Let them speak naturally.

## 4. Extract and Probe

After the initial narrative:

- Identify the actors, work objects, and activities from what they said.
- Present your understanding back as a numbered sequence (e.g., "1. Customer submits Order, 2. System validates Payment...").
- Ask targeted follow-up questions to fill gaps:
  - "Who initiates this?" (missing actors)
  - "What exactly are they working with here?" (vague work objects)
  - "What happens between step N and step M?" (missing activities)
  - "Are there any rules or constraints on this?" (annotations)
  - "Does this belong to a different team or department than the previous steps?" (groups)
- If fine-grained, push for more detail. If coarse-grained, accept higher-level descriptions.

## 5. Confirm the Story

Present the complete domain story in a readable numbered format. Ask the user to confirm or correct it.

## 6. Save the YAML File

Write the confirmed story to `domain-stories/<story-name>.yaml` using the [YAML schema](SCHEMA.md). If the `domain-stories/` directory does not exist, create it.

## Cross-Story Consistency

When capturing a new story, compare actors and work objects against existing stories. If the user introduces a term that is similar but not identical to an existing one (e.g., "Client" vs "Customer"), ask whether these are the same concept or intentionally different.
