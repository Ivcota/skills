# The Evaporating Cloud

A 5-box logic diagram for resolving conflicts where two reasonable actions appear mutually exclusive. The "evaporation" happens when you find an assumption underneath the conflict that's wrong.

## When to use it

Surface this only when conflict is detected — don't force every TOC user through it. Tells:

- The user is stuck in "we must do A *and* B but they conflict."
- A policy or paradigm constraint has been identified and the user can't see how to relax it without breaking something else.
- The same argument keeps recurring without resolution ("but if we do that, then...").
- A trade-off feels permanent ("you can have speed *or* quality").

## The 5 boxes

```
                  ┌─────────────┐
                  │  Common     │
                  │  Objective  │  (D)
                  └──────┬──────┘
                ┌────────┴────────┐
        ┌───────▼──────┐   ┌──────▼───────┐
        │   Need A     │   │   Need B     │  (B, C)
        └───────┬──────┘   └──────┬───────┘
        ┌───────▼──────┐   ┌──────▼───────┐
        │   Action A   │◄─►│   Action B   │  (A, A')
        │              │   │              │
        │  (conflict)  │   │              │
        └──────────────┘   └──────────────┘
```

- **D — Common Objective.** What both sides ultimately want. Often the system's T or a system-level goal.
- **B — Need behind A.** The underlying requirement Action A is meeting.
- **C — Need behind B.** The underlying requirement Action B is meeting.
- **A — Action A.** The proposed action one side wants.
- **A' — Action B.** The conflicting action the other side wants.

The conflict is between A and A'. The resolution is *not* to compromise between them — it's to find a hidden assumption underneath that, once exposed, dissolves the conflict.

## How to read it

The diagram is read as a chain of *necessary conditions*:

- "In order to achieve **D** (common objective), I must have **B** (need A)."
- "In order to have **B**, I must do **A** (action A)."
- "In order to achieve **D**, I must also have **C** (need B)."
- "In order to have **C**, I must do **A'** (action B)."
- "But **A** and **A'** conflict."

Each arrow has a *because*. Behind every "must" there's an *assumption*. The cloud evaporates when one of those assumptions is shown to be false or contingent — meaning the "must" wasn't really a must.

## How to find the wrong assumption

Walk every arrow and ask: "What assumption makes this 'must' true?" Most clouds have 5 candidate assumptions (one per arrow). The wrong one is usually:

- **Behind D→B or D→C** — assuming the only way to meet the objective is via this need.
- **Behind B→A or C→A'** — assuming the only way to meet the need is via this specific action.
- **Behind the conflict A↔A'** — assuming A and A' are actually mutually exclusive (sometimes they aren't; sometimes the conflict is imagined).

The most productive question: **"What would have to be true for both A and A' to coexist?"** That answer is usually the assumption to break.

## Worked example: software team

**Conflict:** "We need to ship faster" vs. "We need to maintain code quality."

```
                  ┌──────────────────────┐
                  │  D: Maximize T       │
                  │  (sustained user-    │
                  │  facing throughput)  │
                  └──────────┬───────────┘
              ┌──────────────┴──────────────┐
              ▼                             ▼
    ┌──────────────────┐            ┌──────────────────┐
    │  B: Ship features│            │  C: Avoid rework │
    │  quickly         │            │  / regressions   │
    └────────┬─────────┘            └────────┬─────────┘
             ▼                               ▼
    ┌──────────────────┐            ┌──────────────────┐
    │  A: Skip review/ │  conflict  │  A': Thorough    │
    │  ship fast       │◄──────────►│  review + tests  │
    └──────────────────┘            └──────────────────┘
```

**Walk the assumptions:**

- D→B "fast shipping = more T" — assumes shipped-fast features stay shipped. False if defects cause rework.
- D→C "no rework = more T" — assumes a stable codebase enables faster future shipping. True.
- B→A "fast shipping requires skipping review" — *this is the wrong assumption.* It assumes review is slow. If review is the bottleneck, the right move is to make review fast (exploit), not skip it.
- C→A' "avoid rework requires thorough review" — assumes thoroughness has to mean slowness. Often false: targeted automated tests + focused human review can be both fast and thorough.

**The cloud evaporates** at B→A. The conflict was framed as "speed vs. quality." The real problem is that the team treats review as expensive. Once you treat review as the constraint and *exploit* it (smaller PRs, automated checks before human review, reviewer rotation, fast-path for clear changes), the conflict dissolves: you ship fast *and* maintain quality.

## Worked example: hiring

**Conflict:** "We need to fill roles fast" vs. "We need to maintain a high hiring bar."

The naive resolution is "compromise — slightly faster, slightly lower bar." Usually wrong.

Walking the cloud:

- The hidden assumption is often at C→A': "high bar requires long process." False if the long process is mostly *waiting* (scheduling delays, candidates dropping out from slow feedback). The bar isn't doing the slowing — the *process inefficiency* is. Compress the loop without lowering the bar.

## How to use the cloud in conversation

Don't draw the boxes formally with the user unless they ask. Walk them through it as five questions:

1. "What do both sides ultimately want?" → D
2. "What does [doing A] give you that you need?" → B
3. "What does [doing A'] give you that you need?" → C
4. "Why must we do A *specifically* to get B?" → assumption B→A
5. "Why must we do A' *specifically* to get C?" → assumption C→A'

Then: "What if [the assumption] weren't true? What would change?"

Most conflicts dissolve at step 4 or 5.

## Common failures

- **Treating the cloud as a compromise tool.** It's not. A compromise weakens both A and A'. The cloud finds an assumption to break so both sides get what they need.
- **Stating actions as needs.** "I need to ship fast" — fast is the action, not the need. The need is "I need to deliver T quickly to capture market opportunity" or similar. Force the need to be more abstract than the action.
- **Solving D too quickly.** If D is "make money," every cloud trivially evaporates because everything serves "make money" eventually. D should be specific to *this conflict* — the system-level outcome both sides agree on.

## Source

The Evaporating Cloud is part of Goldratt's Thinking Processes, introduced in *It's Not Luck* (1994) and detailed in *The Goldratt Institute Theory of Constraints Self-Learning Program*. Sometimes called the "Conflict Resolution Diagram" or "Evaporating Conflict Cloud."
