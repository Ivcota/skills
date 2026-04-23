---
name: align-mental-model
description: |
  Align the user's mental model with reality before they act, by surfacing implicit beliefs via prediction-check, verifying against ground truth, and why-tracing wrong beliefs to their root assumption.
  Three modes: codebase (verify against code), learning (verify against authoritative source), planning (verify present-reality assumptions, flag future-bets explicitly).
  Use when the user is about to make a codebase change, learn a new topic, or commit to a plan, and wants to surface wrong beliefs first.
  Also trigger on "check my mental model", "what am I getting wrong about X", "stress-test my understanding before I do X", "where is my model off", or "align my model".
  Asks for confidence before revealing truth — high-confidence-wrong beliefs (the dangerous ones) get the deepest correction.
  For surfacing gaps via attempted explanation, see feynman. For stress-testing decisions in a plan, see grill-me. For encoding new material into a retention map, see bear-hunter-system.
---

# Align Mental Model

Most failed decisions, broken changes, and stuck learning come from a mental model that has quietly drifted from reality. The user can't fix what they don't know is wrong. **Surface the wrong beliefs before the action that depends on them.**

The mechanic: **prediction-check.** Asking "what do you believe?" misses implicit beliefs — users don't know what they're assuming. Asking "predict what's true" forces those beliefs into the open, verifiable form.

## The loop

1. **Anchor to an upcoming action.** User states what they're about to do (change X / learn Y / commit to plan Z). No action → refuse. This is a targeted audit, not an open audit.
2. **Detect mode** — codebase / learning / planning. State the detected mode aloud; let the user correct.
3. **Identify 3–7 beliefs the action depends on.** Load-bearing AND non-obvious. Skip trivia. Skip what the user already demonstrated they know.
4. **For each belief, prediction-check:**
   - Ask: *"What do you predict is true about X?"*
   - Then: *"How sure — 1–5?"*
   - Verify against ground truth (per mode, below).
   - Reveal the diff.
5. **If wrong, why-trace to the root assumption** — not the proximate cause. *"You assumed X because you've seen Y elsewhere — but here Z is true."* This is the first-principles step: decompose down to the generator of the wrong belief, not the surface symptom.
6. **If high-confidence-wrong, run a reinforcement probe.** Pose a related belief that depends on the same root assumption. If the user still gets it wrong, the rewrite didn't take — go deeper.
7. **End with a scorecard** in chat. No file by default.

## Mode dispatch

Auto-detect from the user's framing. State it before starting: *"Reading this as **codebase mode** — you're about to change X. Confirm or switch."* Each mode has different ground-truth rules; do not blend them.

## Codebase mode

Ground truth = the code. High confidence.

- Read the relevant code before generating probes.
- Probe spots: load-bearing functions, invariants the change depends on, edge cases, error paths, concurrency assumptions.
- Verify each prediction by reading the code; quote the file/line.

## Learning mode

Ground truth = an authoritative source. **Refuse to bluff from trained knowledge.**

- Require the user to name a source — docs URL, book chapter, paper, repo, man page. If they have none, web search with citation.
- If neither is possible (niche topic, no source), abort: *"I can't verify reliably — bring source material first."* A skill that confidently mis-corrects is worse than no skill.
- Probe spots: core concepts, common pitfalls, counterintuitive behavior.

## Planning mode

Split every belief into **verifiable-now** vs **future-bet**. Different treatment.

- **Verifiable-now** (present reality — market size, competitor positioning, prior attempts, current user behavior, internal data): verify via web / user data. Same prediction-check as other modes.
- **Future-bet** (outcome predictions — *"X will convert at Y%"*): do not fake-verify. Surface explicitly: *"This is a bet, not a fact. Lowest-cost way to test it before committing?"* Log it.
- Probe spots: assumptions the plan would collapse without.

## Refusal rules

- No upcoming action → ask for one.
- Learning mode with no source and no web access → abort.
- Detected mode is wrong and user can't clarify → stop, don't proceed on a guess.

## End-of-session output

Chat scorecard. Format:

| Belief | Confidence | Truth | Status |
|---|---|---|---|
| ... | 4/5 | ... | confident-wrong |

Then **Corrected model** (3–5 bullets) and **Implications for [the action]** (what changes given the corrected model).

The four cells of the scorecard mean different things:

- **Confident-wrong** — the dangerous ones. The action would have been built on these. Highest learning value.
- **Tentative-wrong** — easy to fix, low cost.
- **Confident-right** — calibration confirmed; trust this intuition next time.
- **Tentative-right** — the user knew but didn't trust themselves. Surface this so they trust it next time.

If the user wants it saved, they'll ask. Don't impose file-writing.
