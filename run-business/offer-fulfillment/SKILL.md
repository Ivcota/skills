---
name: offer-fulfillment
description: Turn a Grand Slam Offer or equivalent offer description into a fulfillment blueprint, tailored production playbooks, and an implementation plan. Use when designing how to deliver a new offer or systematizing delivery of an existing offer. Designs and plans the work; does not produce the customer deliverables or run operations.
---

# Offer Fulfillment

Translate an offer's promises into a practical system for fulfilling them. Design the whole customer journey first, then the production playbooks for its components, then the work needed to establish and test the system.

Support both new offers and existing businesses. Output is a planning package the business can implement and refine. Completing a document or session is not evidence that the customer achieved the promised result.

## Conversation style and scope

- Propose concrete designs and alternatives; let the user keep, edit, reject, or add. Ask a few targeted questions per stage, using answers already available.
- Map the whole offer before detailing components. Develop one component at a time, starting with the component most critical to the result, unless the user requests a complete first draft.
- At each stage, summarize settled decisions and unresolved assumptions. Revisit affected downstream plans when something changes; do not restart unnecessarily.
- Design and planning only: specifications, procedures, and build briefs are in scope. Creating the actual course, software, client report, automation, or other fulfillment asset requires a separate execution request.
- Preserve the offer's scope and commitments. When they appear infeasible, explain the conflict and propose options for the user's decision; do not silently weaken the offer or add guarantee conditions.
- Present plans in conversation by default. Save planning artifacts when requested, using the user's preferred location and format.

## 1. Intake and operating context

Accept a Grand Slam Offer Card, its fuller conversation output, or an equivalent offer description. Do not require another skill to be installed or rerun offer creation.

Extract the customer, outcome, stack, bonuses, delivery vehicles, timing, guarantee, capacity claims, price, and payment structure. The final Offer Card may omit vehicle details and prior problem-to-solution reasoning: ask only for details that affect fulfillment. Keep absent information visibly unresolved.

Establish:

- New offer, existing delivery system, or a mixture.
- People, available time, expertise, tools, budget, intended customer volume, and launch constraints.
- Reusable assets and processes already available.
- Customer prerequisites and the work expected of them.

For an existing offer, ask for a recent delivery walkthrough: what actually happened, who did it, elapsed time, rework, customer friction, and evidence of results. Separate actual practice from documented procedure. Propose **keep / adapt / replace / investigate** decisions with reasons; preserve demonstrated strengths.

For a new offer, plan a workable first delivery before adding mechanisms for repeated delivery. Mark resource and effort estimates as assumptions.

**Exit:** offer brief, operating constraints, known assets, current-state evidence where available, and consequential unknowns.

## 2. Unpack the commitments

Create a commitment register:

| ID | Offer promise or component | Customer benefit | Concrete output or service | Type(s) | Timing / recurrence | Dependencies | Open questions |
|---|---|---|---|---|---|---|---|

Include core components, bonuses, onboarding, support, result measurement, and obligations created by the guarantee. Distinguish explicit promises from proposed supporting work.

Unpack branded names into concrete work. A "Growth Accelerator" might contain an assessment, roadmap, software setup, and coaching. Split parts with different production processes while retaining their parent commitment. Several promises may share one asset or process: reference it rather than duplicating work.

Treat scarcity as a capacity or scheduling claim to test. Treat guarantee terms as requirements for measurement and a defined response when results fall short. Do not treat perceived stack dollar values as delivery costs.

**Exit:** every commitment has a proposed fulfillment mechanism; ambiguities are visible and material interpretations have been discussed.

## 3. Blueprint the entire journey

Read [references/system-design.md](references/system-design.md). Draft a service blueprint spanning purchase through completion, including continued support where promised.

Show customer actions, visible interactions, internal work, supporting resources, and the artifacts the customer receives. Connect component IDs, handoffs, prerequisites, timing, and feedback. Include the customer's implementation work rather than ending at artifact delivery.

For existing businesses, distinguish the current and proposed arrangements. Highlight changes and why they are needed.

**Exit:** an agreed provisional fulfillment map, shared processes, and a sensible order for detailed playbook design.

## 4. Design component playbooks

Read [references/production-methods.md](references/production-methods.md), selecting only relevant types. Combine methods for mixed components. Use [references/playbook-template.md](references/playbook-template.md) for consistent outputs.

For each component:

1. Define the customer result it supports and a concrete output specification.
2. Identify inputs and readiness conditions.
3. Propose the production method, including consequential decision rules. Explain relevant tradeoffs when multiple methods fit.
4. Specify quality checks, customer handoff, follow-up, and likely exception handling.
5. Estimate resource needs and separate reusable setup from recurring production.
6. Define a pilot that could reveal whether the design works.

Avoid empty steps such as "analyze data" or "create strategy." State what evidence is examined, how it informs a decision, and what the output must contain. Where specialist knowledge is missing, specify the expertise or research needed; do not manufacture an authoritative method.

Use roles when personnel are unknown. A solo operator can hold several roles. Add documentation and checks in proportion to complexity; a checklist does not need the machinery of a software launch.

**Exit per component:** an implementable design with explicit uncertainties and a validation plan. Its process status remains **proposed** until actual delivery evidence supports a stronger status.

## 5. Check the system together

Use the capacity and coherence checks in the system-design reference:

- Does every promise have an owner, process, output, and check?
- Do handoffs supply what downstream work needs, when it needs it?
- Can the team fulfill the promised timing and customer volume, including support and rework?
- Is customer effort feasible, and are delays or missing inputs handled explicitly?
- What measures distinguish output quality, customer adoption, and the promised result?
- Can the proposed system administer the guarantee as written?

Show the most consequential conflicts with practical options and tradeoffs. Keep unresolved dependencies in the final package rather than declaring readiness prematurely.

## 6. Assemble the implementation plan

Produce three connected artifacts:

1. **Fulfillment blueprint:** offer brief, commitment register, journey, dependencies, roles, and operating assumptions.
2. **Component production playbooks:** tailored designs linked to commitment IDs, with shared procedures referenced once.
3. **Prioritized implementation plan:** what to create, adapt, source, or establish; dependency order; proposed owner; effort range and basis; completion criteria; and pilot evidence to collect.

Separate one-time setup, per-customer work, and periodic maintenance. Prioritize prerequisites and uncertain steps critical to the promise. State what is needed before the first delivery and what can be standardized after learning from it.

End with the next concrete planning or implementation step, unresolved decisions, and pilot success criteria. Do not start execution merely because planning is complete.

## Method provenance

This skill is a synthesis: service blueprinting provides the overall map; ISO's process approach informs process definition and feedback; ADDIE and CDC training standards inform learning components. APQC is an optional completeness reference, not a mandatory workflow.

The interview, commitment register, output schema, and unsourced type-specific guidance are practical adaptations, not requirements or certified methods from those sources. Source links and their limits appear in the references. This skill makes no claim of ISO conformity or independently validated business results.
