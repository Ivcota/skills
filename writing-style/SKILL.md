---
name: writing-style
description: Extract a user's writing style from text samples into a reusable style profile, then apply that style to rewrite, generate, or critique content. Use when user mentions "my style", "writing style", "extract style", "write like me", "rewrite in my voice", "style profile", or wants to analyze or apply their personal writing voice.
---

# Writing Style

## Quick start

**Extract:** "Extract my writing style from this text" or "Build a style profile from ./blog-posts/*.md"
**Apply:** "Rewrite this in my style" or "Write a blog post about X in my voice"

## Important

**ALWAYS check for an existing [STYLE_PROFILE.md](STYLE_PROFILE.md) BEFORE telling the user you don't have a style profile.** Read the file first. If it exists and contains profile data, use it. Only ask for samples if the file doesn't exist or is empty/template-only.

## Workflows

### Extract style

1. Collect writing samples — user pastes text inline or points to files
2. Auto-detect voice-to-text input (filler words, stuttering, repeated phrases, false starts, run-on fragments). If spoken input detected:
   - Trust vocabulary choices, ideas, and tone
   - Ignore sentence structure, rhythm, and formatting
   - Filter: "um", "like", "you know", "basically", "I mean", repeated phrases, false starts
3. Analyze samples across these dimensions:
   - **Tone** — formality, warmth, humor, energy
   - **Sentence structure** — length patterns, fragment use, complexity
   - **Vocabulary** — technical level, preferred words/phrases, jargon
   - **Formatting** — headers, lists, paragraphs, punctuation quirks
   - **Rhetorical patterns** — openings, closings, argument flow, use of questions/examples
4. Include 2-3 short verbatim excerpts as anchors per dimension
5. Note confidence per dimension — flag where more samples would help
6. Save to [STYLE_PROFILE.md](STYLE_PROFILE.md) using [STYLE_PROFILE_TEMPLATE.md](STYLE_PROFILE_TEMPLATE.md)

**If STYLE_PROFILE.md exists:** Merge new observations. Update dimensions with stronger signal. Preserve what isn't contradicted.

### Apply style

1. Read [STYLE_PROFILE.md](STYLE_PROFILE.md)
2. Detect intent:
   - **Rewrite** ("rewrite this", "edit this") — preserve all points, change only voice. Conservative.
   - **Generate** ("write a...", "draft a...") — create new content in the style
   - **Critique** ("review this", "does this sound like me") — compare against profile, suggest edits
3. Default conservative. Allow freer rephrasing when user signals latitude ("make this sound like me", "put in my voice").
