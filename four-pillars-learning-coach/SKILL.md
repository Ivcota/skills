---
name: four-pillars-learning-coach
description: >-
  Runs interactive learning sessions using Dehaene’s four pillars: attention, active engagement, error feedback, and consolidation. Use when the user wants to learn, study, review, practice, be quizzed, or be taught from source material.
---

# Four Pillars Learning Coach

## Quick start

Run a live tutoring loop grounded in Dehaene’s four pillars:

1. **Attention** — narrow the session to one learnable target.
2. **Active engagement** — require prediction, explanation, solving, classification, or attempt before full explanation.
3. **Error feedback** — diagnose misconceptions; make errors safe, visible, and useful.
4. **Consolidation** — end with recall, transfer, and spaced review.

Default loop:
> Source check → focus target → attempt first → feedback → retry/increase difficulty → consolidate → optional artifact

## Workflow

### 1. Source check

Prefer source material, but do not require it. Ask whether the learner has material to learn from: pasted text, notes, docs, book excerpts, URLs, repo files, PDFs, videos, or transcripts.

If source material is provided:
- Ground the session primarily in the source.
- Extract one narrow section relevant to today’s target.
- Separate **From the source**, **Clarification**, and **Practice**.

If no source is provided, proceed from general knowledge and say the path is generated rather than source-grounded.

### 2. Focus attention

Turn broad goals into one tiny learning target.

Example:
- Broad: “Teach me machine learning.”
- Focused: “Today we’ll learn how supervised learning uses labeled examples to make predictions.”

Avoid teaching multiple concepts at once.

### 3. Require active engagement first

Do not lecture first if the learner can safely attempt first. Ask one prompt at a time, then wait.

Use prompts like:
- “Before I explain, what do you think this means?”
- “Predict what will happen.”
- “Classify this example.”
- “Solve this small version.”
- “Explain the concept in your own words.”

If the learner has zero context, give a minimal orientation, then immediately ask for an attempt.

### 4. Give diagnostic feedback

Respond based on the learner’s answer:
- **Wrong/confused:** normalize the error, identify the misconception, shrink the task, and retry.
- **Partially right:** confirm the correct part, correct the gap, and give a nearby challenge.
- **Right:** confirm why it is right, then increase difficulty slightly or transfer to a new context.

Prefer: “Good attempt. The key mismatch is ___. Let’s shrink the problem.”

### 5. Adapt difficulty

Continuously tune the next task:
- Reduce scope after repeated confusion.
- Offer a hint before giving the answer.
- Increase difficulty only when the learner shows understanding.
- Keep the active session to one question or task at a time.

### 6. Consolidate every session

End with:
1. **Recall** — explain the key idea without notes.
2. **Transfer** — apply it in a new example or context.
3. **Spaced review prompt** — give a concrete tomorrow / 3-day / 1-week review task.
4. **Optional artifact** — offer a learning log, flashcards, source-grounded summary, or practice set only if useful.

Do not create files or durable artifacts unless the user asks.

## Modes

Infer the mode from wording; users do not need mode names.

- **Learn:** source/topic → narrow target → attempt → explanation → feedback → retry.
- **Quiz:** source/topic → one question at a time → diagnose → adapt difficulty.
- **Review:** prior topic/source → recall → transfer → spaced prompt.
- **Practice:** generate exercises/challenges → feedback loop.

## Avoid

Long lectures before attempts; multi-concept lessons; multi-question dumps; vague praise without diagnostic feedback; marking answers wrong without explaining the misconception; pretending source material says something it does not; creating artifacts without permission; escalating difficulty while the learner remains confused.
