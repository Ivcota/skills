# Business-Aligned Blueprint

Source anchors: Chapter 1, pages 2-4; Chapter 16, pages 477-486.

## Use This When

- The architecture has technology choices but no clear business rationale.
- Stakeholders disagree about scope, timeline, risk, or what success means.
- A design review keeps jumping straight into implementation details.
- The team needs a SAD, ADR, proposal, or architecture review.

## Intake Prompts

Ask these before proposing architecture:

1. What business concern does this solution address?
2. What capability will the business gain or improve?
3. Who are the direct and indirect stakeholders?
4. What is in scope, and what is explicitly out of scope?
5. What assumptions are required for this design to hold?
6. What constraints are fixed: budget, timeline, compliance, technology, skills, vendors, data residency?
7. What upstream and downstream dependencies does the system have?
8. What risks would threaten delivery, operation, adoption, cost, or security?
9. What measurable NFRs define success?

## Decision Capture

Use this structure for major decisions:

```markdown
Decision: [choice]
Problem: [business/technical problem]
Options considered: [option A], [option B], [option C]
Chosen because: [rationale]
Trade-offs: [cost, complexity, risk, operations, performance]
Constraints: [constraints that shaped the decision]
Validation: [POC, test, metric, stakeholder review]
```

## Review Heuristics

- If a technology choice cannot be traced to a business goal or NFR, treat it as weak.
- If assumptions are not documented, ask what would break the design if the assumption is false.
- If a dependency is not documented, ask who owns it and what happens when it fails.
- If no stakeholder view exists, ask which audience cannot use the current document.
