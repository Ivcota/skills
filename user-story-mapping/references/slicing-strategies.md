# Slicing Strategies — Deep Reference

## Sources
- howtoes.blog summary: https://howtoes.blog/2024/03/26/user-story-mapping-book-summary/
- Patton, "The New Backlog": https://jpattonassociates.com/the-new-backlog/
- MindTheProduct interview: https://www.mindtheproduct.com/getting-started-with-user-story-mapping-jeff-patton/

---

## The Three Slicing Types

Patton describes three distinct purposes for slicing a story map horizontally: *(howtoes.blog/2024/03/26/)*

### 1. Release Slicing
**Purpose:** Identify the minimum viable solution focused on a specific business outcome.
**Question:** What is the smallest set of tasks that achieves [outcome] for [user]?
**Output:** A horizontal line drawn across the map with a named outcome tied to the tasks above it.

### 2. Learning Slicing
**Purpose:** Identify the experiments needed to validate the riskiest assumptions before committing to build.
**Question:** What do we need to know before we can commit to this release? What is the most efficient way to learn it?
**Output:** An MVPe — a targeted experiment or prototype targeting the single riskiest card.

### 3. Development Slicing
**Purpose:** Order the construction of the release to front-load risk.
**Question:** Within the tasks above the release line, what do we build first to expose blockers early?
**Output:** An Opening/Midgame/Endgame ordering of the tasks already committed to the release.

---

## Good / Better / Best Slicing

Patton uses a "Good, Better, Best" model to draw three release lines on one map: *(Patton, mindtheproduct.com)*

- **Good (v1):** The walking skeleton — minimum end-to-end functionality achieving the core outcome
- **Better (v2):** Adds breadth — additional tasks per backbone activity, secondary user flows
- **Best (v3):** Full depth — edge cases, polish, non-critical alternatives

This gives stakeholders three concrete options to discuss, rather than a single scope negotiation that defaults to "everything."

---

## The Horizontal Slice Rule

> "We never release a car without brakes." *(Patton, jpattonassociates.com/the-new-backlog/)*

Every slice must cross all backbone activities. A slice that only covers two of five backbone activities is not a release — it is a subsystem. Users cannot accomplish their goal with a subsystem.

**Test:** Can a user with only the tasks above the release line complete their end-to-end goal? If no, the slice is vertical (a mistake) rather than horizontal (correct).

---

## Slicing vs. Prioritizing

Slicing and prioritization are not the same thing:

| Concept | Meaning | Applies to |
|---------|---------|-----------|
| **Prioritizing** | Ranking individual items | Tasks within a column (top = higher priority) |
| **Slicing** | Drawing a horizontal line across the whole map | All columns simultaneously |

Trying to prioritize across backbone activities is the error that produces "some of the most miserable hours of my life," in Patton's words. *(Patton, jpattonassociates.com/the-new-backlog/)* Activities cannot be prioritized against each other. Tasks within an activity can be prioritized. Slices define which priority level ships in which release.

---

## Slicing Workshop Format

A practical format for a slicing session:

1. **State the release outcome.** "What behavior change in which user does this release produce?"
2. **Walk the map and mark tasks that contribute.** Use dots or move cards up.
3. **Draw the release line.** Everything that contributes to the stated outcome, and nothing else.
4. **Check for horizontal coverage.** Is there at least one task above the line in each backbone activity?
5. **Challenge everything above the line.** "What happens if we defer this?" If the release still achieves its outcome, move it down.
6. **Name the release.** Not "v1" but the outcome: "Invoice creation for freelancers" or "Core checkout for mobile."
