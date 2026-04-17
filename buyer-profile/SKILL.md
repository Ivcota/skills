---
name: buyer-profile
description: |
  Create deep buyer psychology profiles that uncover real emotional drivers, fears, desires, and motivations behind purchasing decisions.
  Produces comprehensive buyer personas with raw, unfiltered internal monologue, relationship dynamics, failed past solutions, and transformation fantasies.
  Two modes: Interview mode (asks the user questions to gather product/market/avatar info) and Direct mode (user provides all context upfront).
  Use when the user wants to create a buyer profile, buyer persona, avatar profile, customer psychology analysis,
  understand their market's emotional drivers, or says "who is my buyer", "buyer profile", "avatar research", or "customer persona".
---

# Buyer Profile — Deep Buyer Psychology Analysis

Build accurate buyer profiles that reveal the raw emotional drivers behind purchasing decisions. Not surface-level demographics — the private fears, desires, and internal monologue prospects would never say out loud.

References: [Profile Template](profile-template.md) | [Interview Questions](interview-questions.md)

## Mode Detection

**Direct mode** (default): User provides product, market, and avatar info upfront. Proceed directly to profile generation.

**Interview mode**: Activated when the user says "interview me", doesn't provide market/product info, or context is insufficient. Walk through the interview questions in [Interview Questions](interview-questions.md) to gather what's needed before generating the profile.

## Input Requirements

Before generating a profile, you need three things:

1. **Target Market** — Who are these people? (e.g., eBay resellers, SaaS founders, fitness coaches)
2. **Product/Service** — What are you selling? (Can be "TBD" — profile the market first)
3. **Avatar Details** — Any known demographics, psychographics, or context about the ideal buyer

If any of these are missing or thin, switch to Interview mode.

## Process

### Phase 1: Context Gathering

- [ ] Identify target market
- [ ] Identify product/service (or mark TBD)
- [ ] Identify any known avatar details
- [ ] If insufficient context → run Interview mode via [Interview Questions](interview-questions.md)

### Phase 2: Profile Generation

Generate the full buyer profile following the structure in [Profile Template](profile-template.md). Every section is required.

**Critical rules for generation:**

1. **Write as the prospect** — use their language, their internal monologue, their slang
2. **Go dark** — fears should be 3AM-awake-staring-at-the-ceiling fears, not polished survey answers
3. **Be ultra-specific** — name relationships (spouse, mother-in-law, coworker Dave), use vivid scenarios, not abstractions
4. **Soundbites are dialogue** — they should read like overheard conversations, not marketing copy
5. **Include both supporters and antagonists** — well-meaning but hurtful comments AND hostile ones
6. **Fantasy is allowed** — the transformation section is the prospect's wildest dream, let it be vain and aspirational
7. **No sugarcoating** — the entire point is honesty. Sanitized profiles are useless profiles

### Phase 3: Review & Refine

- [ ] Present the full profile to the user
- [ ] Ask: "Does this match your understanding of your market? Anything feel off or missing?"
- [ ] Refine based on feedback
- [ ] Optionally generate advertising angle recommendations based on the strongest emotional drivers

## Output Format

Deliver the profile as a single, structured document using the section headers from [Profile Template](profile-template.md). Use markdown formatting. All soundbites should be in blockquotes with speaker labels.

## Principles

- **Emotion first, logic second** — buyers purchase on emotion, justify with logic. Lead with the feeling.
- **Nothing leaves the room** — this profile is internal strategy. Remind the user that raw insights inform copy but are never shown to prospects.
- **Common over niche** — pain points, desires, and past solutions should be widely shared across the target audience, not edge cases.
- **Conversational tone** — everything written in the voice of the prospect, not a researcher.
