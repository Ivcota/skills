# Plan to Build Less — Deep Reference

## Sources
- Patton, "The New Backlog": https://jpattonassociates.com/the-new-backlog/
- marcabraham.com book review: https://marcabraham.com/2015/05/07/book-review-user-story-mapping/
- howtoes.blog summary: https://howtoes.blog/2024/03/26/user-story-mapping-book-summary/
- Medium bullet summary: https://medium.com/@ivanlandabaso/user-story-mapping-by-jeff-patton-bullet-summary-1bf7b673e181

---

## The MVP Redefined

Patton's central reframe: MVP does not mean "minimum crappy product." It means "the smallest product release that successfully achieves its desired outcomes." *(marcabraham.com/2015/05/07/)*

The difference matters. "Minimum crappy" optimizes for shipping fast by cutting quality. "Minimum viable outcome" optimizes for learning fast by cutting scope while maintaining integrity.

---

## MVP Feature Categories

From the book, four categories for classifying features during MVP slicing: *(Medium/@ivanlandabaso)*

| Category | Definition | Implication for MVP |
|----------|-----------|---------------------|
| **Differentiator** | Provides competitive advantage | High priority — likely in MVP |
| **Spoiler** | Neutralizes a competitor's strength | Situational — depends on competitive context |
| **Cost Reducer** | Reduces operational costs | Often deferred unless cost savings are critical at launch |
| **Table Stakes** | Expected baseline features users assume exist | Must be present, but should be scoped narrowly |

---

## The Walking Skeleton

The walking skeleton is the MVP of the map: the smallest end-to-end system that can actually run. The term comes from Alistair Cockburn; Patton applies it to story maps specifically.

Construction rule: take the highest-priority task from **each backbone activity**. The result is a system that does one thing in each activity area — barely — but does it coherently end to end.

> "All the stories placed high on the story map describe the smallest possible system you could build that would give you end to end functionality." *(Patton, jpattonassociates.com/the-new-backlog/)*

**Why end-to-end matters:** Shipping a fully-built subsystem (vertical slice) does not give you something users can use or that you can learn from. A walking skeleton does — even if it does very little.

---

## Drawing the Release Line

Step-by-step:

1. **Define the target outcome** for the release. What behavior change in which user?
2. **Walk each task above the tentative line.** Does this task contribute to the target outcome?
3. **Move non-contributing tasks below the line.** They are not excluded — they are deferred.
4. **Check that the line crosses all backbone activities.** If any activity has nothing above the line, the skeleton has a gap.
5. **Challenge everything above the line.** "What happens if we defer this?" If the release still achieves its outcome, move it down.

---

## Output vs. Outcome

A persistent failure mode Patton identifies: teams measure what they shipped (output) rather than what changed in user behavior (outcome).

> "There's always more to build than we have time and money for." *(Patton, howtoes.blog/2024/03/26/)*

The output/outcome distinction changes how the release line is drawn:
- **Output-focused:** "Which features can we fit in the sprint?"
- **Outcome-focused:** "Which tasks are necessary and sufficient to produce [specific behavior change] in [specific user]?"

Outcome-focused slicing consistently produces smaller, more coherent releases.

---

## The "Plan to Build Less" Conversation

Patton frames the discipline of building less as an active planning practice, not a passive consequence of constraint. The phrase "plan to build less" is deliberate: it suggests that reducing scope is a first-class decision made intentionally, not something that happens when a deadline is hit. *(Medium/@ivanlandabaso citing Patton)*

The story map makes this decision visible. Teams that negotiate scope on a flat backlog are fighting over priority positions. Teams that negotiate scope on a story map are drawing lines — a concrete, visual act that shows exactly what changes when scope moves.

---

## Common Questions

**Q: Isn't the walking skeleton just a prototype?**
No. A prototype is disposable and often does not implement the real system. The walking skeleton is a slice of the actual production system — thin but real. It is deployable and usable, even if it does very little. *(Patton, jpattonassociates.com/the-new-backlog/)*

**Q: How do we handle Table Stakes features that users expect but don't differentiate us?**
Patton's advice: include them, but scope them narrowly. Table Stakes features need to be present to avoid rejection, but they do not need to be fully-featured in the MVP. The minimum version of a Table Stakes feature is enough for release 1. *(Medium/@ivanlandabaso)*

**Q: What if the walking skeleton doesn't give users enough to form an opinion?**
If the skeleton is too minimal to get signal, it means the walking skeleton has been sliced too thin. Every task in the skeleton should represent real user capability, not just technical scaffolding. The test: can a user accomplish their core goal using only the tasks above the release line?

---

## Vocabulary Reference

| Term | Definition | Source |
|------|-----------|--------|
| **MVP** | "The smallest product release that successfully achieves its desired outcomes" | marcabraham.com/2015/05/07/ |
| **Walking skeleton** | Minimum end-to-end system built from one task per backbone activity | Patton, jpattonassociates.com/the-new-backlog/ |
| **Release line** | Horizontal line across the map separating what ships from what defers | Patton, jpattonassociates.com/the-new-backlog/ |
| **Output** | Features and software delivered | howtoes.blog/2024/03/26/ |
| **Outcome** | Real-world behavioral change from users | howtoes.blog/2024/03/26/ |
| **Differentiator** | Feature providing competitive advantage | Medium/@ivanlandabaso |
| **Spoiler** | Feature neutralizing a competitor's strength | Medium/@ivanlandabaso |
| **Cost Reducer** | Feature reducing operational costs | Medium/@ivanlandabaso |
| **Table Stakes** | Expected baseline features users assume exist | Medium/@ivanlandabaso |
