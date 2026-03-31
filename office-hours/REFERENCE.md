# Office Hours Reference

## Startup Mode: The Six Questions

### Q1 — Demand Reality

"What's the strongest evidence you have that someone actually wants this — not 'is interested,' not 'signed up for a waitlist,' but would be genuinely upset if it disappeared tomorrow?"

Push until you hear specific behavior: someone paying, expanding usage, building their workflow around it, or who would have to scramble if you vanished.

Red flags: "People say it's interesting." "We got 500 waitlist signups." None of these are demand.

### Q2 — Status Quo

"What are your users doing right now to solve this problem — even badly? What does that workaround cost them?"

Push until you hear a specific workflow: hours spent, dollars wasted, tools duct-taped together, people hired to do it manually.

Red flags: "Nothing — there's no solution, that's why the opportunity is so big." If truly nothing exists, the problem probably isn't painful enough.

### Q3 — Desperate Specificity

"Name the actual human who needs this most. What's their title? What gets them promoted? What gets them fired? What keeps them up at night?"

Push until you hear a name, a role, a specific consequence. Ideally something the founder heard directly from that person.

Red flags: Category-level answers. "Healthcare enterprises." "SMBs." You can't email a category.

### Q4 — Narrowest Wedge

"What's the smallest possible version of this that someone would pay real money for — this week, not after you build the platform?"

Push until you hear one feature, one workflow. Something shippable in days.

Red flags: "We need to build the full platform before anyone can really use it." That's attachment to architecture, not value.

Bonus push: "What if the user didn't have to do anything at all to get value? No login, no integration, no setup. What would that look like?"

### Q5 — Observation & Surprise

"Have you actually sat down and watched someone use this without helping them? What did they do that surprised you?"

Push until you hear a specific surprise — something the user did that contradicted your assumptions.

Red flags: "We sent out a survey." "We did some demo calls." Surveys lie. Demos are theater.

The gold: users doing something the product wasn't designed for. That's often the real product trying to emerge.

### Q6 — Future-Fit

"If the world looks meaningfully different in 3 years — and it will — does your product become more essential or less?"

Push until you hear a specific claim about how their users' world changes and why that change makes the product more valuable. Not "AI keeps getting better so we keep getting better."

Red flags: "The market is growing 20% per year." Growth rate is not a vision.

---

## Builder Mode: Questions

Ask one at a time. Goal is to brainstorm and sharpen, not interrogate.

1. What's the coolest version of this? What would make it genuinely delightful?
2. Who would you show this to first? What would make them say "whoa"?
3. What's the fastest path to something you can actually use or share?
4. What existing thing is closest to this — and how is yours different?
5. What would you add with unlimited time? What's the 10x version?

---

## Approach Template

```
APPROACH A: [Name]
  Summary:
  Effort:  [S/M/L/XL]
  Risk:    [Low/Med/High]
  Pros:
  Cons:
  Reuses:  [existing patterns]

APPROACH B: [Name]
  ...
```

---

## Design Doc Template

```markdown
# Design: {title}

Generated: {date} | Branch: {branch} | Status: DRAFT | Mode: {Startup|Builder}

## Problem Statement

## {Startup: Demand Evidence | Builder: What Makes This Cool}

## {Startup: Status Quo | Builder: (omit)}

## {Startup: Target User & Narrowest Wedge | Builder: (omit)}

## Premises

## Approaches Considered

## Recommended Approach

## Open Questions

## Success Criteria

## Next Steps
{Startup: one concrete real-world action — not "go build it" | Builder: concrete build tasks in order}

## What I noticed about how you think
{2-4 bullets. Quote their words back to them. Observational, not evaluative.}
```
