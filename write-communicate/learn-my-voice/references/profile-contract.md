# Voice Profile Contract

The profile is portable Markdown. `learn-my-voice` is its only writer; other skills read `STYLE_PROFILE.md` without loading evidence or history.

## Locations

Each layer uses the same three files:

```text
voice/
├── STYLE_PROFILE.md
├── EVIDENCE.md
└── CHANGELOG.md
```

- Global layer: `~/.claude/voice/`
- Project layer: `<project-root>/.claude/voice/`

Create a layer only when it has approved content. The project layer inherits the global layer and contains only differences or explicit overrides.

## Rule identity

IDs are unique across all layers:

- Global observed: `G-V001`
- Global intended: `G-I001`
- Project observed: `P-<project-id>-V001`
- Project intended: `P-<project-id>-I001`

On project-layer creation, derive `project-id` once: normalize the project-root basename to lowercase hyphens, then append the first eight hexadecimal characters of a SHA-256 digest of the canonical Git remote URL; when no remote exists, digest the canonical absolute project-root path. Store the result in profile frontmatter and reuse it thereafter.

Allocate the next unused number in that namespace and never reuse a retired ID. A project rule that changes a global rule keeps its project ID and names the global ID in an `Overrides` field. Without that field, the rules are independent.

## `STYLE_PROFILE.md`

Keep this file compact enough for a writing skill to read before drafting.

```markdown
---
profile-version: 1
scope: global | project
project-id: acme-a1b2c3d4 # project only
updated: YYYY-MM-DD
languages:
  - en
inherits: ~/.claude/voice/STYLE_PROFILE.md # project only
---

# Writing Voice Profile

## Voice Kernel

- G-V001 — Short identifying label

## Observed Voice

### Diction
- [G-V002][supported][default][en] Observable word-choice pattern.

### Rhythm and Sentence Shape

### Structure

### Rhetoric

### Tone

### Mechanics

### Audience and Purpose

### Avoidances

## Intended Voice

- [G-I001][supported][default][en] Explicit preference the user wants to strengthen.

## Contextual Variants

### technical-peers
- [P-acme-a1b2c3d4-V001][supported][technical-peers][en] Project-specific form of the rule.
  - Overrides: G-V003
```

### Rule syntax

Every rule has a stable ID and three independent attributes:

```text
[ID][state][condition][language] Operational rule.
```

- **ID:** globally unique according to the namespace above.
- **State:** `supported` or `confirmed` for active rules. Hypotheses live in `EVIDENCE.md`; retired rules live in evidence and history.
- **Condition:** `default` or a short named audience, purpose, channel, or project context.
- **Language:** a language tag such as `en`, `pt-BR`, or `shared` for cross-language rhetoric only.
- **Operational rule:** behavior a writer can apply or test. Use observable language rather than personality labels such as “authentic” or “smart.”
- **Overrides:** optional on a project rule; names exactly one global rule whose behavior it replaces when the project condition applies.

The **Voice Kernel** is an index of the five to ten highest-signal rule IDs and short labels. The authoritative wording appears only in the rule's home section.

## `EVIDENCE.md`

This file carries the legwork behind the compact profile. Every calibration cycle belongs to exactly one layer: the layer containing the tested rule or hypothesis, or the proposed target layer for a new hypothesis. Increment only that layer's counter after the user approves the save delta. Use blind A/B when the next count in that layer is divisible by three.

```markdown
# Voice Evidence

## Calibration

- Completed cycles: 3
- Last method: blind A/B
- Last tested: YYYY-MM-DD

## Open Hypotheses

### G-V004 — Short hypothesis name
- State: hypothesis
- Proposed rule: ...
- Supporting observations:
  - YYYY-MM-DD — concise observation
- Counterevidence:
  - YYYY-MM-DD — concise conflict
- Next test: one discriminating question or A/B contrast

## Rule Evidence

### G-V002
- State: supported
- Supports:
  - YYYY-MM-DD — "short approved excerpt" — source/context
- Counters:
  - YYYY-MM-DD — concise counterexample — source/context
- Tests:
  - YYYY-MM-DD — visible contrast — result
  - YYYY-MM-DD — blind A/B — result
- Last tested: YYYY-MM-DD
```

Store only evidence needed to justify, challenge, or test a rule. Excerpts must be short and explicitly approved. Summarize the signal when the wording itself is unnecessary. Complete conversations stay outside the profile.

## Evidence states

- **Hypothesis:** one observation or an untested interpretation; stored only under Open Hypotheses.
- **Supported:** repeated evidence or one explicit correction supports the rule, but meaningful uncertainty remains.
- **Confirmed:** the rule survived contrastive testing across representative evidence.
- **Retired:** contradicted, superseded, or intentionally abandoned; retained in evidence and history, removed from active profile sections.

A condition is independent of evidence state: a rule may be both `supported` and limited to `technical-peers`. Age alone does not weaken a rule. New conflict triggers diagnosis: context, evolution, or bad inference.

## `CHANGELOG.md`

Append one compact entry per approved save:

```markdown
## YYYY-MM-DD — global | project

- Added: G-V005 — short label
- Revised: G-V002 — what changed
- Conditioned: P-acme-a1b2c3d4-V001 — condition added
- Retired: G-I001 — reason
- Evidence: approved excerpts or tests retained
- Reason: one-sentence session result
```

For a verified no-change session, update the calibration record and relevant test in `EVIDENCE.md`; leave the changelog unchanged unless the user explicitly requests a history entry.

## Merge rules

1. Load active global rules.
2. Add project rules whose conditions apply.
3. When a project rule's `Overrides` field names a global rule, suppress that global rule only while the project rule's condition applies.
4. A more specific condition wins over `default`.
5. Intended rules remain distinct from observed rules; the consuming writer selects the requested target.
6. Resolve conflicting active rules with explicit conditions or retirement.
7. Promotion retires the project rule and creates or revises one global rule after user approval and evidence beyond one project. Move evidence once; never duplicate it across layers.

## Save checklist

Before writing an approved delta, account for every changed item:

- Active rule text and evidence state
- Observed versus intended section
- Condition and language
- Rule ID and any override relationship
- Supporting or counterevidence
- Test method, result, and cycle count
- Approved excerpt status
- Global or project layer
- Kernel membership, if the rule is high-signal
- Open-hypothesis change
- Changelog entry and reason

The save is complete only when the profile, evidence, and changelog agree.
