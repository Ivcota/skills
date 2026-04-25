---
name: style-profile
description: Extract a user's writing style from text samples into a reusable style profile, then apply that style to rewrite, generate, or critique content. Also supports refining an existing profile sentence-by-sentence against a draft. Use when user mentions "my style", "writing style", "extract style", "write like me", "rewrite in my voice", "style profile", "refine my style", "go through this sentence by sentence", or wants to analyze or apply their personal writing voice.
---

# Style Profile

## Quick start

**Extract:** "Extract my writing style from this text" or "Build a style profile from ./blog-posts/*.md"
**Apply:** "Rewrite this in my style" or "Write a blog post about X in my voice"
**Refine:** "Go through this sentence by sentence — I'll approve or rewrite, then update the profile"

## Important

**ALWAYS check for an existing `./STYLE_PROFILE.md` in the current working directory BEFORE telling the user you don't have a style profile.** Read the file first. If it exists and contains profile data, use it. Only ask for samples if the file doesn't exist or is empty/template-only.

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
6. Save to `./STYLE_PROFILE.md` in the **current working directory** using this structure:

```markdown
# Style Profile

> Generated from [N] writing samples. Last updated: [date].

## Tone
**Confidence:** [high/medium/low — more samples needed for X]
[Description of formality, warmth, humor, energy]
**Examples:**
- "[verbatim excerpt]"
- "[verbatim excerpt]"

## Sentence Structure
**Confidence:** [high/medium/low]
[Length patterns, fragment use, complexity, rhythm]
**Examples:**
- "[verbatim excerpt]"
- "[verbatim excerpt]"

## Vocabulary
**Confidence:** [high/medium/low]
[Technical level, preferred words/phrases, jargon, distinctive word choices]
**Examples:**
- "[verbatim excerpt]"
- "[verbatim excerpt]"

## Formatting
**Confidence:** [high/medium/low]
[Header usage, list preferences, paragraph length, punctuation quirks]
**Examples:**
- "[verbatim excerpt]"
- "[verbatim excerpt]"

## Rhetorical Patterns
**Confidence:** [high/medium/low]
[How they open pieces, build arguments, use questions, deploy examples, close pieces]
**Examples:**
- "[verbatim excerpt]"
- "[verbatim excerpt]"

## Notes
[Anything that doesn't fit above — distinctive quirks, things to avoid, areas needing more samples]
```

**If `./STYLE_PROFILE.md` exists:** Merge new observations. Update dimensions with stronger signal. Preserve what isn't contradicted.

### Apply style

1. Read `./STYLE_PROFILE.md` from the **current working directory**
2. Detect intent:
   - **Rewrite** ("rewrite this", "edit this") — preserve all points, change only voice. Conservative.
   - **Generate** ("write a...", "draft a...") — create new content in the style
   - **Critique** ("review this", "does this sound like me") — compare against profile, suggest edits
3. Default conservative. Allow freer rephrasing when user signals latitude ("make this sound like me", "put in my voice").

### Refine style (sentence-by-sentence)

Use when the user has an existing `./STYLE_PROFILE.md` and wants to sharpen it against a fresh draft. Triggers: "go through this sentence by sentence", "I'll approve or rewrite", "refine my style profile", "tighten the profile against this".

The core mechanic: **the user's rewrites are data, your verdicts are hypotheses.** Approvals reinforce existing profile entries. Rewrites correct or add to them.

**Steps:**

1. Read the existing `./STYLE_PROFILE.md`. If it doesn't exist, run the Extract workflow first instead — refine assumes you already have a hypothesis to test.

2. Take the user's draft text. Do not paraphrase or summarize it back.

3. **One sentence at a time.** For each sentence:
   - Quote the original sentence verbatim
   - Give a verdict: **sounds like you** (with which profile dimensions back it up) or **suggested tweak** (with the specific reason — which profile rule pushes the change)
   - If suggesting a tweak, propose a concrete rewrite
   - End with a short prompt: "Approve, or rewrite?"
   - **Stop and wait.** Do not advance to the next sentence until the user responds.

4. Read the user's response as one of:
   - **Approval** ("yep", "approve", "sure", "its fine") — move to next sentence. No profile update needed; the existing rule held.
   - **Rewrite** (any version of the sentence) — this is the signal. Note what changed and why in one line back to the user ("logged — connector instead of fragment, `for sure` as a tag"), then move on.
   - **Question or pushback** — answer it before advancing.

5. **Handle truncated input.** If a sentence is cut off mid-word, reconstruct a best-guess version using the existing profile's vocabulary and the surrounding logic. Mark it as a guess and let the user approve, rewrite, or replace.

6. **At the end, fold findings into the profile.** Use Edit (not Write) to update the existing `./STYLE_PROFILE.md`:
   - Update dimension descriptions where rewrites revealed a stronger or contradicting pattern
   - Add new entries to Vocabulary (softeners, tags, recurring words) and Notes (quirks, things to avoid)
   - Sharpen Latitude levels if the rewrites exposed a context split (e.g., reply-mode vs long-form behave differently for the same rule)
   - Bump confidence levels where the pass added evidence
   - Update the "Last updated" line with the date and a brief note on what was refined

**What to log vs. what to skip:**
- Log: rewrites, surprising approvals (where the user accepted something the profile didn't predict), patterns that repeat across multiple rewrites
- Skip: routine approvals of already-documented patterns, one-off typos in rewrites (don't infer rules from a single instance unless it matches an existing trend)

**Tone during the pass:**
- Brief. One verdict per sentence, one-sentence reason. Don't lecture.
- Cite the profile rule by name when proposing a tweak ("profile says em dashes are rare for you")
- After a rewrite, log the signal in one line. Don't re-explain the whole rule.
