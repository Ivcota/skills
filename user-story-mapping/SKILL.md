---
name: user-story-mapping
description: |
  Apply, diagnose, and teach Jeff Patton's User Story Mapping — a visual technique for building shared understanding and slicing work into outcome-focused releases.
  Organizes the product backlog as a two-dimensional grid (backbone + prioritized tasks) rather than a flat list, keeping the whole story visible while planning incremental delivery.
  Use when the user mentions user story mapping, story map, story map backlog, backbone and tasks, walking skeleton, or slice the map. Also trigger when the user wants to plan to build less, plan to learn faster, or plan to finish on time.
  Also trigger when the user is building a story map, slicing a release, defining MVP scope, running a product discovery workshop, or restructuring a flat backlog.
---

# User Story Mapping

User Story Mapping is a product planning technique developed by Jeff Patton and described in his 2014 O'Reilly book *User Story Mapping: Discover the Whole Story, Build the Right Product*. The technique arranges user activities and tasks in a two-dimensional grid — left to right as a narrative of user behavior, top to bottom by priority — so teams can identify the smallest release that delivers real value without losing sight of the whole story.

## Core Principle

The problem with agile development is not stories — it is what teams do with them. Flattening work into a prioritized backlog strips stories of context. Patton describes the result as "A bag of context-free mulch": dozens of cards that cannot be navigated, communicated through, or used to find what is missing. *(Patton, jpattonassociates.com/the-new-backlog/)*

The solution is to organize stories spatially. A story map preserves the narrative of how users move through a system. Working left to right follows user sequence; working top to bottom reveals prioritization within each activity. The result is a planning artifact that teams can walk, slice, and update together.

**The foundation:** "Shared documents aren't shared understanding." The value of story mapping is not the map itself — it is the conversation the map enables and the common mental model the team builds while making it. *(Patton, jpattonassociates.com/the-new-backlog/)*

## The User Story Mapping Framework

### 1. Story Map Anatomy

**Core concept:** A story map is a two-dimensional grid. The top row — the *backbone* — holds high-level user activities arranged in chronological or logical sequence. Below each activity hang *tasks*: the specific things users do to accomplish that activity. Below the tasks hang *details*: variations, edge cases, and alternatives. The backbone cannot be prioritized against itself (you cannot ship email without compose *and* inbox), but tasks and details can be sliced into releases. *(Patton, jpattonassociates.com/the-new-backlog/; marcabraham.com/2012/07/27/)*

**Why it works:** The grid format preserves narrative flow that a flat list destroys. Walking the top row tells you what the product does; walking down any column shows you how deep that capability needs to go. Teams can see both the whole story and where individual stories fit within it simultaneously.

**Key insights:**
- The backbone represents activities — "large goals like 'managing email'" — not individual features. *(Patton, jpattonassociates.com/the-new-backlog/)*
- "Those big things on the top are often the essential capabilities the system needs to have." Asking stakeholders to prioritize them against each other is like asking whether a car needs an engine or a transmission. *(Patton, jpattonassociates.com/the-new-backlog/)*
- Below the backbone, tasks are arranged vertically by importance — not sequence. The most important task in each column sits at the top. *(howtoes.blog/2024/03/26/)*
- Activities cluster related tasks toward a common goal; tasks are the individual things users do within each activity. *(marcabraham.com/2012/07/27/)*
- The map becomes the team's "constant point of discussion about the product we're building" and functions as an information radiator throughout the project. *(Patton, jpattonassociates.com/the-new-backlog/)*
- The horizontal flow follows user sequence; activities are placed left to right as the user would experience them. *(marcabraham.com/2012/07/27/)*

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **Mobile app** | Use backbone activities as navigation areas; tasks map to screens within each area | Banking app: backbone = check balance, pay bills, transfer; tasks under "pay bills" = find payee, enter amount, confirm |
| **B2B SaaS** | Map admin and end-user journeys as parallel backbones | CRM: admin setup activities + sales rep daily-use activities run as separate rows on the same map |
| **Discovery workshop** | Build the map collaboratively to surface conflicting mental models | Different team members placing the same card in different columns reveal gaps in shared understanding |
| **Sprint planning** | Use the map as the iteration planning board instead of a flat backlog | Map shows which activity areas have undone tasks, preventing over-investment in any single column |
| **New team member onboarding** | Walk the map horizontally (what the product does) then vertically (priority decisions made so far) | Horizontal walk = product scope; vertical walk = why things are ordered as they are |

**Copy patterns:**
- "Let's walk the backbone first — [activity 1], [activity 2], [activity 3] — before we break down any column."
- "This goes in the backbone only if removing it would make the product make no sense."
- "We are not prioritizing activities against each other. We are organizing tasks within each activity by importance."
- "What is the smallest set of tasks across each column that gives us end-to-end functionality?"

See: [references/story-map-anatomy.md](references/story-map-anatomy.md) for backbone construction examples and task decomposition depth guidelines.

---

### 2. Plan to Build Less

**Core concept:** Most teams build too much because they conflate *output* (features delivered) with *outcome* (behavior change in users). Patton defines the MVP not as "the crappiest version" but as "the smallest product release that successfully achieves its desired outcomes." *(marcabraham.com/2015/05/07/)* The story map makes the cut visible: draw a horizontal line below the tasks that constitute the walking skeleton and above the rest. Everything above the line ships in release 1; everything below is deferred.

**Why it works:** The map externalizes the trade-off. Teams can see the full story, slide cards up and down within a column, and draw the release line with everyone watching. The line makes scope decisions a discussion rather than a unilateral call by a single person.

**Key insights:**
- "There's always more to build than we have time and money for." Story mapping makes that constraint visible rather than hiding it in a prioritized list. *(Patton, howtoes.blog/2024/03/26/)*
- MVP categories: Differentiator (competitive advantage), Spoiler (neutralizing competitor strength), Cost Reducer (operational savings), Table Stakes (expected baseline features). *(Medium/@ivanlandabaso citing the book)*
- The walking skeleton — a concept Patton draws from Alistair Cockburn — is "the smallest possible system you could build that would give you end to end functionality." It is built by taking the highest-priority task from each backbone activity. *(Patton, jpattonassociates.com/the-new-backlog/)*
- Development proceeds "left to right, and top to bottom...slowly moving across the backbone, and down through the priorities of each rib" — ensuring "we never release a car without brakes." *(Patton, jpattonassociates.com/the-new-backlog/)*
- "Plan to build less, plan to learn faster, and plan to finish on time." *(Medium/@ivanlandabaso citing Patton)*

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **SaaS MVP launch** | Draw the release line to identify minimum functional release | Keep account creation + core job-to-be-done above line; defer settings, reporting, bulk ops |
| **Feature development** | Use outcome focus to cut scope mid-discovery | PM removes 8 of 12 planned tasks after identifying that only 4 drive the target behavior change |
| **Roadmap negotiation** | Walk stakeholders through the map to negotiate cuts visually | Stakeholder removes a card from above the line; team walks through what that changes |
| **Sprint scope** | Slice thin across the backbone rather than fully completing one column | Each sprint delivers an end-to-end slice; no sprint produces a subsystem that isn't usable |
| **Engineering scoping** | Distinguish output (features) from outcome (user behavior change) | Reframes "we shipped the notification feature" to "did notifications change return behavior?" |

**Copy patterns:**
- "What outcome do we need from this release? Now let's cut everything that doesn't drive that outcome."
- "The MVP is the smallest release that achieves [specific outcome] for [specific user]."
- "Walk the skeleton: one task from each backbone activity, end-to-end, nothing more."
- "We are not shipping the minimum crappy product — we are shipping the minimum product that does its job."

See: [references/plan-to-build-less.md](references/plan-to-build-less.md) for MVP slicing criteria and walking skeleton construction.

---

### 3. Plan to Learn Faster

**Core concept:** Before writing stories, validate the problem. Patton describes a discovery process: Frame the Idea (clarify why, for whom, and within what business bounds), Understand Customers (develop personas, current-state journey maps, and pain points), Envision Solutions (future-state story map with UI sketches), and Minimize and Plan (cut to the minimum viable experiment). *(howtoes.blog/2024/03/26/)* The as-is state must be mapped before the to-be state — "the future is a fiction" until a release validates it. *(Patton, mindtheproduct.com)*

**Why it works:** Story maps built before discovery are speculative. Maps built after user research capture real behavior, real sequences, and real pain points. Discovery converts the map from a feature list into a testable hypothesis about user behavior.

**Key insights:**
- "If you cannot tell me a story about how people use your product...you bloody well better not be building a feature at all." *(Patton, mindtheproduct.com)*
- Map the current state ("as-is") separately from the future state ("to-be"). The as-is map grounds the conversation in evidence; the to-be map is the design fiction under test. *(Patton, mindtheproduct.com)*
- Minimum Viable Product Experiment (MVPe): a targeted experiment to validate a specific risk before committing to build the full feature. *(howtoes.blog/2024/03/26/)*
- "Failing to learn is frequently the biggest failure." *(Patton, howtoes.blog/2024/03/26/)*
- The discovery sequence: Frame → Understand Customers → Envision Solutions → Minimize. *(howtoes.blog/2024/03/26/)*
- Defining who the product will *not* help is as important as defining who it will: "The hardest decisions you will make are not what features go into your product. It's what people you're going to help." *(Patton, mindtheproduct.com)*

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **New product** | Build current-state map from user interviews before writing a single story | Map how users manage invoices today — with all pain and workarounds — before designing the invoicing feature |
| **Feature discovery** | Run a discovery sprint: Frame, research, Envision, Minimize | 4-day sprint produces a future-state map and 3 MVPe hypotheses to test before committing |
| **Persona development** | Use map-building sessions with real users to validate who the system serves | Mid-session discovery that two assumed user roles are the same person eliminates a major assumption |
| **Product pivot** | Rebuild the as-is map after market feedback contradicts assumptions | Current-state map reveals users skip the step the original product was built to improve |
| **Roadmap justification** | Present the as-is map before the to-be map to stakeholders | Makes the problem concrete before the solution; prevents "why are we building this?" questions |

**Copy patterns:**
- "Before we map the solution, let's map what users actually do today — pain points included."
- "What is the riskiest assumption in this map? Build the MVPe to test that assumption first."
- "We have a to-be map but no as-is map. We are building from fiction."
- "Frame it: who is this for, what do they do today, and what behavior do we need to change?"

See: [references/plan-to-learn-faster.md](references/plan-to-learn-faster.md) for discovery sprint structure and MVPe design.

---

### 4. Plan to Finish on Time

**Core concept:** Story maps support delivery planning by making risk and dependency visible. Patton recommends three development strategy phases: Opening game (essential, cross-cutting, and risky features first), Midgame (fill functionality gaps), Endgame (refinement and polish). Slicing the map by phase — rather than by feature category — keeps each slice functional end-to-end and risk addressed early. *(howtoes.blog/2024/03/26/)*

**Why it works:** Phase-based slicing ensures the team builds a working product at every point rather than assembling half-built components that only compose into something usable at the very end. Risk is front-loaded when there is still time to respond.

**Key insights:**
- Development strategy slicing has three phases: Opening game (risky, essential, cross-cutting), Midgame (gap fill), Endgame (polish and refinement). *(howtoes.blog/2024/03/26/)*
- Release strategy slicing identifies "the minimum viable solution focused on specific business outcomes." *(howtoes.blog/2024/03/26/)*
- Estimation should be done at the task level on the map, not at the activity level — tasks are small enough to estimate with confidence. *(O'Reilly TOC, Ch 4)*
- "Software is never really done, only abandoned." Planning to finish on time means defining *done enough* for a given release. *(Patton, howtoes.blog/2024/03/26/)*
- The map used as an iteration planning board replaces the flat backlog and keeps every priority decision in the context of the whole story. *(Patton, jpattonassociates.com/the-new-backlog/)*

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **Sprint planning** | Use Opening/Midgame/Endgame framing to sequence sprints | Sprint 1 = auth + one end-to-end core slice (Opening); Sprint 5 = edge cases and polish (Endgame) |
| **Launch planning** | Identify risky technical areas as Opening game to surface blockers early | Authentication, payment, and data migration are Opening game; profile editing is Midgame |
| **Engineering estimation** | Estimate at the task level on the map rather than the epic/activity level | Tasks are estimable; activities are not — decomposing first prevents estimate inflation |
| **Stakeholder communication** | Show release line position to communicate scope decisions visually | "Here is what ships in v1 (above this line) and what is in v2 (below)" |
| **Scope creep defense** | New requests placed on the map above the release line must displace something else | Makes trade-offs visible and concrete; stops scope additions from being invisible |

**Copy patterns:**
- "Opening game: what is risky, cross-cutting, or essential? That ships first."
- "Midgame fills the gaps. Endgame polishes. Do not polish before you have filled the gaps."
- "Estimate at the task level, not the activity level."
- "What does *done enough for release* mean for this map? Draw that line."

See: [references/plan-to-finish-on-time.md](references/plan-to-finish-on-time.md) for phase planning templates and estimation approaches.

---

### 5. The Three Cs: How Stories Work

**Core concept:** Ron Jeffries's 3 Cs framework describes what a user story is: a *Card* (a short title on a physical token), a *Conversation* (the rich discussion the card triggers), and *Confirmation* (the shared agreement on how the team knows the story is done). Patton adopts and extends this throughout the book: "Stories get their name from how they're supposed to be used, not what you're trying to write down." *(Patton, howtoes.blog/2024/03/26/; O'Reilly TOC Ch 6)*

**Why it works:** The 3 Cs reframe stories from documentation artifacts into conversation triggers. The Card is a placeholder for a conversation, not a specification. The Conversation is where shared understanding is built. Confirmation captures the output of that conversation — not as locked requirements but as testable acceptance criteria that reflect current understanding.

**Key insights:**
- The 3 Cs originate with Ron Jeffries (original XP contributor) and are used and extended by Patton in Ch 6. *(O'Reilly TOC; howtoes.blog/2024/03/26/)*
- "Stories get their name from how they're supposed to be used, not what you're trying to write down." *(Patton, howtoes.blog/2024/03/26/)*
- The conversation checklist should address: who (specific user types), what (user tasks), why (goals across users and stakeholders), context (outside the software), failures (what goes wrong), assumptions (to test), better solutions, implementation approach, and timeline/cost. *(marcabraham.com/2015/05/07/)*
- "As a…, I want to…, so that…" — the standard story template — is a starting point for the conversation, not a complete requirement. *(briefshelf.com/book/user-story-mapping)*
- The As/Want/So-That format makes visible: who benefits, what they do, and why — opening each of those as discussion topics. *(howtoes.blog/2024/03/26/)*

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **Story writing** | Use the template to surface the "so that" — the outcome — not just the feature | "As a returning customer, I want to see my order history, so that I can reorder without searching" |
| **Refinement sessions** | Treat each card as a conversation trigger, not a ready-to-implement spec | Card titled "export report" triggers conversation about formats, frequency, who exports, what happens when it fails |
| **Acceptance criteria** | Write confirmations as testable behaviors discovered in conversation | Instead of "the user can export," write "given X state, when Y action, then Z observable result" |
| **Story splitting** | Use the conversation to find natural seams in a large story | "Manage account" splits mid-conversation into billing, security, and preferences — three separate stories |
| **Sprint review** | Use confirmations as the definition of done, not feature presence | A story is done when all confirmed behaviors can be demonstrated, not when the feature is visible |

**Copy patterns:**
- "The card is the invitation to the conversation. What do we actually need to talk through?"
- "Tell me the story: who does this, in what context, for what outcome?"
- "What is the confirmation? If we cannot describe how we would test it, we do not understand it yet."
- "As [specific user type], I want [concrete action], so that [measurable outcome]."

**Ethical boundary:** Patton is explicit that the goal of stories is "building shared understanding," not producing documentation. Teams that write detailed story specs without conversation are using the form without the substance. *(Patton, jpattonassociates.com/the-new-backlog/)*

See: [references/three-cs.md](references/three-cs.md) for conversation checklist and confirmation templates.

---

### 6. Slicing Strategies

**Core concept:** Slicing is cutting the story map horizontally to define releases. Patton describes three slicing strategies: Release slicing (what outcome this release achieves for which users), Learning slicing (what risks must be resolved before committing to build), and Development slicing (the technical order of construction within a release). Each slice is end-to-end: it includes at least one task from each backbone activity so the result is always coherent and deliverable. *(howtoes.blog/2024/03/26/)*

**Why it works:** Horizontal slices force end-to-end thinking. Vertical slices (building one activity fully before moving to the next) produce shippable subsystems but not shippable products. A horizontal slice ensures the product does *something* complete at every milestone.

**Key insights:**
- Release slicing identifies "minimum viable solution focused on specific business outcomes." *(howtoes.blog/2024/03/26/)*
- Learning slicing creates MVPe hypotheses around the riskiest assumptions in the map before committing to build. *(howtoes.blog/2024/03/26/)*
- Development slicing (Opening/Midgame/Endgame) addresses technical risk in the Opening game before adding breadth in Midgame. *(howtoes.blog/2024/03/26/)*
- Slices are always horizontal — crossing all backbone activities — not vertical. *(Patton, jpattonassociates.com/the-new-backlog/)*
- "We never release a car without brakes." Horizontal slicing prevents releasing a polished capability area against an unfinished core. *(Patton, jpattonassociates.com/the-new-backlog/)*
- Good/Better/Best slicing gives teams three release lines on one map: minimum viable (good), improved (better), complete (best). *(Patton, mindtheproduct.com)*

**Product applications:**

| Context | Application | Example |
|---------|-------------|---------|
| **Release planning** | Draw multiple horizontal lines to define v1, v2, v3 on one map | Three lines = three releases, each with one task from every backbone activity |
| **Risk-based ordering** | Use learning slices to sequence experiments before full builds | Validate willingness to pay before building billing infrastructure |
| **Quarterly roadmap** | Translate each release slice into a roadmap milestone | Each horizontal slice becomes one milestone with a defined target outcome and success metric |
| **Technical architecture** | Use development slicing to scaffold incrementally | Opening game slice drives core data model + auth; Midgame adds domain logic; Endgame adds polish |
| **Scope negotiation** | Move cards between slices in front of stakeholders | "If we move this card below the v1 line, we ship two weeks earlier — what do we lose?" |

**Copy patterns:**
- "Draw three lines: good, better, best. What goes in good? That is your v1."
- "This is a horizontal slice — one task from every column, not a full column."
- "What is the learning slice? What do we need to know before we commit to building the full release?"
- "What outcome does this slice achieve, for which user, and how will we know it worked?"

See: [references/slicing-strategies.md](references/slicing-strategies.md) for release, learning, and development slicing templates.

---

## User Story Mapping Process

Follow these steps in order to build and use a story map from scratch:

1. **Frame the opportunity.** Clarify who the product or feature is for, what problem it solves, and what outcome the team is trying to achieve. Map the as-is state before envisioning any solution. *(O'Reilly TOC Ch 1; howtoes.blog/2024/03/26/)*

2. **Map the big picture.** Write user activities across the top row (the backbone) in left-to-right narrative order. Focus on breadth before depth — cover the whole user journey before expanding any column. *(marcabraham.com/2015/05/07/; howtoes.blog/2024/03/26/)*

3. **Break down the backbone into tasks.** For each activity, write the tasks users perform to accomplish it. Place them below the activity in rough priority order — most important at the top. *(Patton, jpattonassociates.com/the-new-backlog/)*

4. **Explore alternatives.** Add edge cases, failure paths, and alternative user types below the primary tasks. These form the body of the map — the variations that a minimal release can defer. *(marcabraham.com/2015/05/07/)*

5. **Slice for the first release.** Draw a horizontal line across the map. Everything above the line is the walking skeleton — the smallest end-to-end slice that achieves the target outcome. *(Patton, jpattonassociates.com/the-new-backlog/)*

6. **Run discovery to validate assumptions.** Before committing to build, identify the riskiest assumptions in the map and design MVPe experiments to test them. *(howtoes.blog/2024/03/26/; mindtheproduct.com)*

7. **Sequence delivery by phase.** Use Opening game (risky + essential), Midgame (gaps), Endgame (polish) to order development within the release slice. *(howtoes.blog/2024/03/26/)*

8. **Keep the map alive.** Update the map as the team learns. Move cards, redraw release lines, and add tasks as the product evolves. The map is not a signed-off document — it is a living model. *(Patton, jpattonassociates.com/the-new-backlog/)*

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| **Treating the map as a documentation artifact** | A map no one discusses is a prettier flat backlog — it still lacks shared understanding | Build the map in a room with the right people; the conversation is the deliverable, not the map |
| **Building the backbone from features, not activities** | Features belong below the backbone; activities are user goals, not system capabilities | Ask "what is the user trying to accomplish?" not "what does the feature do?" |
| **Slicing vertically instead of horizontally** | Vertical slices produce fully-built subsystems that don't compose into a shippable product | Every slice must cross all backbone activities end-to-end |
| **Confusing output with outcome** | Shipping features without validating behavior change produces a product no one uses | Define the target outcome and success metric before drawing the release line |
| **Mapping the solution before the problem** | A to-be map without an as-is map is speculative fiction | Map current user behavior first; build the future-state map second |
| **Too many people in the room from the start** | Large groups produce maps by committee; no one owns the narrative | Start with a small cross-functional group; invite observers who ask questions without building |
| **Writing story templates without conversation** | "As a…, I want to…" written without discussion produces incomplete specs that breed misunderstanding | The template opens the conversation — use the checklist (who, what, why, context, failures, assumptions) |

*Sources: mindtheproduct.com; marcabraham.com/2015/05/07/; howtoes.blog/2024/03/26/*

## Quick Diagnostic

Use this table to audit an existing story map or story-based backlog:

| Question | If No | Action |
|----------|-------|--------|
| Does the backbone represent user activities (not features)? | No narrative flow; prioritization fights are endless | Rewrite top row as user goals; move feature cards below the backbone |
| Is there a horizontal release line drawn? | The backlog is a flat list with no release strategy | Draw the walking skeleton: one task from each backbone activity |
| Does each release slice cross all backbone activities? | Some releases are vertical (subsystems, not shippable products) | Redraw release lines horizontally across the full map |
| Is there an as-is map alongside the to-be map? | Team is building solutions without evidence of the problem | Run a current-state mapping session grounded in user research |
| Can every card above the release line be linked to the target outcome? | Scope creep above the line | Walk each card: if it does not drive the release outcome, move it below the line |
| Has the team run the 3 Cs conversation checklist on each story? | Cards are specs, not conversation triggers | Schedule refinement sessions using the checklist: who, what, why, context, failures, assumptions |
| Are the riskiest assumptions in the map identified? | Team is building without validating core hypotheses | Identify the top 3 riskiest cards; design MVPe experiments before committing to build |

## Reference Files

- [story-map-anatomy.md](references/story-map-anatomy.md): Backbone construction, task decomposition, and depth guidelines
- [plan-to-build-less.md](references/plan-to-build-less.md): MVP slicing, walking skeleton construction, outcome vs. output
- [plan-to-learn-faster.md](references/plan-to-learn-faster.md): Discovery sprint structure, MVPe design, as-is vs. to-be mapping
- [plan-to-finish-on-time.md](references/plan-to-finish-on-time.md): Phase planning (Opening/Midgame/Endgame), estimation, delivery sequencing
- [three-cs.md](references/three-cs.md): Conversation checklist, confirmation templates, story template usage
- [slicing-strategies.md](references/slicing-strategies.md): Release, learning, and development slicing templates
- [case-studies.md](references/case-studies.md): Worked examples across product discovery, sprint planning, and roadmap negotiation
- [checklist.md](references/checklist.md): Step-by-step workshop worksheet and story map health checklist

## Further Reading

This skill is based on *User Story Mapping: Discover the Whole Story, Build the Right Product* by Jeff Patton with Peter Economy (O'Reilly, 2014).

- [*User Story Mapping*](https://www.oreilly.com/library/view/user-story-mapping/9781491904893/) — O'Reilly (ISBN: 978-1-491-90490-9)
- [jpattonassociates.com/the-new-backlog/](https://jpattonassociates.com/the-new-backlog/) — Jeff Patton's original blog post on story mapping
- [Amazon](https://www.amazon.com/User-Story-Mapping-Discover-Product/dp/1491904909) — ISBN: 1491904909

## About the Author

**Jeff Patton** is a product discovery coach, consultant, and speaker. He is a recognized practitioner in agile and lean product development and has taught user story mapping at conferences globally since the mid-2000s. His blog at [jpattonassociates.com](https://jpattonassociates.com) and his original 2008 "The New Backlog" article predate the book and are widely cited in the agile and product management communities. The book carries forewords from Martin Fowler, Alan Cooper, and Marty Cagan. *(Patton, jpattonassociates.com; Amazon.com/User-Story-Mapping-Discover-Product/dp/1491904909)*
