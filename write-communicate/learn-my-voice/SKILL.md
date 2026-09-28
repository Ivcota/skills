---
name: learn-my-voice
description: Learn and refine my writing voice through conversation.
disable-model-invocation: true
---

# Learn My Voice

Build an evidence-backed **ear** for the user's intended written voice. Keep this service on learning and calibration; profile-consuming writing skills produce finished content.

Before creating or changing profile files, read [`references/profile-contract.md`](references/profile-contract.md) completely.

## Orient

Profiles are layered:

- **Global:** `~/.claude/voice/`
- **Project overlay:** `<project-root>/.claude/voice/`

Read the global layer first, then the project overlay when one exists. The overlay contains only project-specific additions or explicit overrides.

Infer the session's mode from the invocation and existing files:

- **Bootstrap** an empty profile
- **Continue** from the largest open uncertainty
- **Calibrate** existing rules

Briefly state the proposed mode. Classify each proposed rule as global or project-specific; one session may produce separate deltas for both layers, but the same rule or evidence belongs to only one. Let the user correct the classification before saving. If a legacy `<project-root>/STYLE_PROFILE.md` exists and the layered profile does not, offer to import it rather than starting over.

## Evidence

Weight evidence in this order:

1. Explicit corrections, contrastive choices, and approved rewrites
2. Approved finished writing
3. Patterns repeated across conversations or contexts
4. A single conversational observation

Corrections are strongest, not permanent: re-check them when later behavior repeatedly conflicts.

Treat voice-to-text as noisy evidence. Preserve meaningful diction, cadence, emphasis, and rhetorical habits. Classify fillers, false starts, accidental repetition, and transcription punctuation as noise rather than written-style rules.

Capture style: linguistic behavior, rhetorical habits, audience choices, and intentional preferences. Keep biography, beliefs, private facts, and subject knowledge outside the profile. Separate observed defaults from intended preferences. Retain only short excerpts the user approves; summarize other evidence instead of storing transcripts.

## Build the Ear

Work in calibration cycles. Each cycle:

1. Select one highest-value uncertainty in diction, rhythm, structure, rhetoric, tone, mechanics, audience adaptation, avoidances, or an evidence-backed emergent category, and identify the single profile layer that owns it.
2. Ask up to three varied, low-stakes questions that expose that uncertainty. Ask one at a time; the user may redirect or skip any topic.
3. Listen without narrating every observation. A single observation remains a hypothesis.
4. End the cycle with a contrastive check: show two concise alternatives and ask which is closer, or ask the user to correct both.
5. Read the owning layer's completed-cycle count. When the next count is divisible by three, use a blind A/B: preserve one meaning, vary only the style under test, conceal which version follows the current profile until after the choice, and record the method and result. Otherwise use the visible contrast from step 4.
6. Classify the result as a new hypothesis, stronger support, confirmation, a condition, retirement, or verified no-change.
7. Ask whether to continue with the next uncertainty or review the session delta.

When evidence conflicts, ask whether the difference is context, intentional evolution, or a bad inference. Update the condition, evidence state, language, or profile layer that explains the conflict.

For an empty profile, use a representative finished sample when one is already available. Otherwise begin the interview immediately; a sample is helpful, never required.

## Maintain the Profile

Use the stable frame in the profile contract, adding custom categories only when evidence requires them.

- Track evidence as **hypothesis**, **supported**, **confirmed**, or **retired**; track context in the separate condition field.
- Separate **Observed voice** from **Intended voice**.
- Represent audience-, purpose-, project-, and language-specific behavior as conditions.
- Keep a shared rhetorical identity across languages, while learning diction, syntax, rhythm, and mechanics separately for each language used.
- Promote a project rule to global only after evidence extends beyond one project. Propose the promotion explicitly.
- Keep the operational profile compact. Evidence and history live in their disclosed files.

## Save Gate

Draft changes during the session. When the user chooses review—or stops early—show one concise delta:

- Target layer for each item
- Rules added, revised, conditioned, promoted, or retired
- Evidence and counterevidence retained
- Approved excerpts retained
- Open hypotheses changed
- Calibration cycle count, test method, and result

Wait for approval. Apply only the approved delta, then append its reason to the compact changelog.

## Completion

A session completes in either state:

- **Useful delta:** every approved rule, state, condition, language, layer, evidence item, counterevidence item, excerpt, open-hypothesis change, kernel membership, calibration count, test method, test result, and changelog entry has been saved, and all three profile files agree; or
- **Verified no-change:** one complete calibration cycle tested the highest-value uncertainty; the owning layer's approved cycle count, test method, and result were saved in `EVIDENCE.md`, while active rules and the changelog remained unchanged.

Close with the result, the remaining highest-value uncertainty, and the best next question for a future session.
