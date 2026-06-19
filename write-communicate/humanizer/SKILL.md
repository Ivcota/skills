---
name: humanizer
description: 'Remove signs of AI-generated writing from text to make it sound natural and human. Use when the user says "this sounds like AI", "humanize this", "make this less robotic", "remove AI patterns", "clean up this text", or "this reads like ChatGPT". Also use when text shows obvious AI markers: heavy em dashes, boldface bullet headers, rule-of-three lists, significance inflation, chatbot openers, or sycophantic tone. Supports optional voice calibration from a writing sample. Based on Wikipedia''s "Signs of AI writing" guide — 29 detectable patterns across five categories.'
license: MIT
metadata:
  author: blader
  version: "2.5.1"
  source: "Wikipedia. 'Signs of AI writing.' WikiProject AI Cleanup. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing"
---

# Humanizer

Remove AI writing patterns and add human voice. Based on Wikipedia's "Signs of AI writing" guide — 29 patterns drawn from observations of thousands of AI-generated texts.

**Key insight:** LLMs tend toward the most statistically likely result. The goal is not just clean text — it is text with a person behind it.

## Process

1. Scan for all 29 patterns in [PATTERNS.md](PATTERNS.md) — Content, Language, Style, Communication, Filler/Hedging.
2. Rewrite each problematic section. Favor `is/are/has` over copula avoidance. Name the actor. Use specific details.
3. Present **Draft rewrite**.
4. Self-audit: ask "What makes this so obviously AI generated?" List remaining tells (≤5 bullets).
5. Revise again based on the audit.
6. Present **Final rewrite** + brief **Changes made** summary.

## Voice

**Without a sample** — write with a natural, varied, opinionated voice:
- Vary sentence length. Short. Then one that takes its time.
- Have opinions. React, don't just report.
- Acknowledge complexity and uncertainty.
- Let some mess in — tangents and asides are human.
- Use "I" when it fits.

**With a writing sample** — analyze it first: sentence length, word choice level, paragraph openers, punctuation habits, verbal tics. Then match those patterns in the rewrite instead of applying the defaults above.

How to provide a sample: `"Humanize this. Here's a sample of my writing: [sample]. Now humanize: [text]."`

## Pitfalls

- **Don't stop at the first draft.** Subtle AI patterns survive the first pass — always do the audit.
- **Don't invent specifics.** Replacing vague attributions with made-up citations is worse. Remove or note as unverified.
- **Don't over-remove hyphens.** Keep technical or uncommon compound modifiers hyphenated.
- **Don't strip all hedging.** Humans hedge — they just do it less and more deliberately.
- **Don't clean without adding soul.** Sterile, voiceless writing still reads as generated.

## Reference

See [PATTERNS.md](PATTERNS.md) for all 29 patterns with before/after examples.
