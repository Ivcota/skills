# Story Map Anatomy — Deep Reference

## Sources
- Patton, "The New Backlog": https://jpattonassociates.com/the-new-backlog/
- Marc Abraham, "Jeff Patton's story mapping": https://marcabraham.com/2012/07/27/jeff-pattons-story-mapping/
- howtoes.blog summary: https://howtoes.blog/2024/03/26/user-story-mapping-book-summary/

---

## The Two-Axis Grid

A story map has two organizing axes:

**Horizontal axis — Narrative sequence**
Left to right follows the user's journey through the product. Activities are placed in the order a user would encounter them — not by importance or build order. "A story map, initially, for me, is about thinking things through and understanding user experience." *(Patton, marcabraham.com/2012/07/27/)*

**Vertical axis — Priority within activity**
Top to bottom within each column represents importance. The highest-priority task in each activity sits at the top. The lower you go, the more optional the detail.

---

## The Three Rows

### Row 1: The Backbone (Activities)
- High-level user goals, not system features
- Each activity represents a cluster of related tasks toward a common outcome
- Activities cannot be prioritized against each other — the product needs all of them
- "It would be stupid to ask stakeholders to prioritize...the engine or the transmission?" *(Patton, jpattonassociates.com/the-new-backlog/)*
- Activities are typically noun phrases: "Manage billing," "Find a product," "Complete checkout"

### Row 2: Tasks (User Tasks)
- Specific things a user does to accomplish the parent activity
- Arranged left to right within an activity by sub-sequence (where order matters)
- Arranged top to bottom by importance (where multiple options exist)
- Tasks are the unit that gets sliced into releases
- Term originated with Patton; "ribs" in Dan Rawsthorne's terminology *(marcabraham.com/2012/07/27/)*

### Row 3+: Details (Variations and Alternatives)
- Edge cases, error states, alternative flows, additional user types
- These are the "body" of the map below the primary tasks
- Not required for a working system; deferred to later releases or never built
- Adding details during exploration prevents surprises later in development

---

## Backbone Construction — Step by Step

1. **Start with the user's whole journey.** Ask: "If I were watching a user accomplish their goal, what would I see them doing — from beginning to end?" Write each observable action on a card.

2. **Cluster related actions.** Group cards that belong to the same user goal. Each cluster becomes one activity on the backbone.

3. **Name the activity at the goal level.** The activity name should describe what the user is trying to accomplish, not what the system does. "Pay a bill" not "Billing module."

4. **Sequence the activities.** Arrange activities left to right as the user encounters them. Most products have 5–10 backbone activities.

5. **Resist the urge to decompose immediately.** Build breadth (all activities) before depth (tasks within each). Walk the whole backbone before breaking down any column.

---

## Common Backbone Errors

| Error | Example | Fix |
|-------|---------|-----|
| **Feature-named activities** | "Search feature," "Admin panel" | Rename to user goal: "Find a product," "Manage account" |
| **Too many backbone items** | 20+ activities | Cluster related ones; activities should be major goal areas, not every action |
| **System-perspective backbone** | "Data ingestion," "Report generation" | Reframe from the user's perspective: "Upload data," "View results" |
| **Sequential sub-tasks as activities** | "Enter credit card number" as backbone | This is a task under "Complete checkout," not a backbone activity |

---

## Depth Guidelines

How deep to go in each column depends on how well the team understands that activity:

- **Unknown territory** (new product area): Go 3-4 levels deep in discovery to surface what you don't know
- **Known territory** (established feature): One level of tasks is usually enough to slice releases
- **Edge cases**: Capture them below the primary task row but don't let them crowd the backbone

The map should be *discoverable* — you should be able to stand at the wall and understand the product by reading it. Overcrowded columns with too many levels of detail defeat this purpose.

---

## The Map as a Communication Tool

Patton describes the map as an "information radiator" that stays visible throughout the project, becoming the "constant point of discussion about the product we're building" and the iteration planning board itself. *(Patton, jpattonassociates.com/the-new-backlog/)*

This means the map is not a one-time workshop artifact — it is updated as the team learns. Cards move, release lines shift, new tasks are added based on user feedback. The map reflects current shared understanding, not a signed-off specification.

**Physical vs. digital maps:**
Patton built the technique with physical cards on a wall. The principles transfer to digital tools, but the physical format has advantages: it is easier to move cards, everyone can see it at once, and the act of physically placing cards forces the team to commit to a location in the narrative. Digital maps are more durable and shareable.

---

## Vocabulary Reference

| Term | Definition | Source |
|------|-----------|--------|
| **Backbone** | Top row of activities — high-level user goals that cannot be prioritized against each other | Patton, jpattonassociates.com/the-new-backlog/ |
| **Activities** | Clusters of related tasks toward a common user goal — the backbone items | howtoes.blog/2024/03/26/ |
| **Tasks** | Individual things users do within an activity — the "ribs" in Dan Rawsthorne's terminology | marcabraham.com/2012/07/27/ |
| **Details** | Edge cases, alternatives, and variations below the primary task rows | marcabraham.com/2015/05/07/ |
| **Happy path** | The basic narrative flow: one task per activity, end-to-end | marcabraham.com/2015/05/07/ |
| **Body** | All the alternative stories and edge cases below the happy path row | marcabraham.com/2015/05/07/ |
| **Walking skeleton** | The minimum end-to-end system — one task from each backbone activity | Patton, jpattonassociates.com/the-new-backlog/ |
| **Release line** | A horizontal line drawn across the map separating what ships from what defers | Patton, jpattonassociates.com/the-new-backlog/ |
| **Ribs** | Alternative term for tasks, from Dan Rawsthorne's framing | marcabraham.com/2012/07/27/ |

---

## Facilitation Notes

**Who should be in the room:**
Patton recommends small cross-functional teams for initial map building — too many people produces maps by committee. Ideal: PM, 1-2 engineers, designer, and someone with direct user knowledge. Observers (who ask questions but don't build) add value without slowing down the primary mapping. *(Patton, mindtheproduct.com)*

**Breadth before depth rule:**
Walk the entire backbone — all activities — before breaking down any single column. Teams that start decomposing the first activity in detail lose the narrative flow and end up with a lopsided map.

**The "so what?" test for backbone items:**
For each candidate backbone activity, ask: "So what? What does the user accomplish?" If the answer describes a system capability rather than a user goal, the item belongs below the backbone, not on it.
