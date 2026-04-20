# Plan to Finish on Time — Deep Reference

## Sources
- howtoes.blog summary: https://howtoes.blog/2024/03/26/user-story-mapping-book-summary/
- O'Reilly TOC Ch 4: https://www.oreilly.com/library/view/user-story-mapping/9781491904893/
- Patton, "The New Backlog": https://jpattonassociates.com/the-new-backlog/

---

## Development Strategy Slicing: The Three Phases

Patton describes three phases for sequencing development within a release: *(howtoes.blog/2024/03/26/)*

### Opening Game
Build what is essential, cross-cutting, and risky first.
- Essential: The core function without which the product makes no sense
- Cross-cutting: Infrastructure that multiple features depend on (auth, data model, APIs)
- Risky: Unknowns that could derail the release if discovered late

**Why first?** Risks found in the Opening game have the most response time. A technical blocker discovered in the final sprint cannot be resolved without a schedule slip. The same blocker found in sprint 1 can be redesigned around.

### Midgame
Fill functionality gaps. Build the tasks that add breadth and depth to the walking skeleton established in the Opening game.
- Additional task rows within each backbone activity
- Secondary user flows
- Error handling and edge cases that complete the main path

### Endgame
Polish and refinement. Build the details that improve experience but are not load-bearing for the release.
- UI polish
- Performance optimization
- Non-critical edge cases
- Nice-to-haves that survived the release line

**Rule:** Do not Endgame before you have completed the Midgame. Polishing before filling gaps produces a product that looks good in demos but fails in real use.

---

## Estimation at the Task Level

> "Estimation should be done piece-by-piece against individual tasks on the map, not against epic-level activities." *(O'Reilly TOC, Ch 4)*

Activities are too large to estimate reliably. Tasks — the individual cards — are small enough for confident estimates. The map makes this natural: you can see exactly which tasks are above the release line and estimate each one.

Aggregate the task estimates per release slice to get a delivery forecast. If the slice is too large for the time available, move tasks below the line until the estimate fits.

---

## Done Enough

> "Software is never really done, only abandoned." *(Patton, howtoes.blog/2024/03/26/)*

"Finishing on time" in Patton's framing means defining *done enough for this release* — not "everything the product could ever need." Before drawing a release line, the team must agree on what the release is supposed to achieve and what state of completion is sufficient to test that hypothesis.

Done-enough criteria:
1. The walking skeleton is end-to-end functional
2. The target outcome can be measured
3. The riskiest assumptions have been tested or can be tested post-release
4. The team can respond to what they learn

---

## The Map as Iteration Planning Board

Patton recommends using the story map itself as the team's iteration planning board, replacing the flat sprint backlog. *(Patton, jpattonassociates.com/the-new-backlog/)*

Benefits:
- Every task selected for a sprint is visible in context of the whole story
- The team can see which backbone activities are complete vs. in-progress
- New stakeholder requests can be placed on the map and evaluated against the release line in real time
- The map serves as the "constant point of discussion" rather than a static artifact reviewed once at planning
