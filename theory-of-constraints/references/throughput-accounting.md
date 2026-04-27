# Throughput Accounting

Goldratt's three-number measurement system. Replaces traditional cost accounting for TOC decisions.

## The three numbers

- **Throughput (T)** — money the system generates *through sales*. Sellable output, not gross production. Unsold inventory is **not** throughput, even if it's finished.
- **Inventory / Investment (I)** — money tied up in the system. WIP, raw materials, started-not-finished work. In knowledge work: open PRs, half-built features, candidates mid-pipeline, started-not-shipped commitments.
- **Operating Expense (OE)** — money spent turning I into T per unit time. Team cost, tooling, overhead.

**Decision rule:** a "good" change increases T, decreases I, or decreases OE — for the system as a whole.

## Why cost accounting misleads

Traditional cost accounting allocates fixed costs per unit produced. This creates two pathologies:

1. **Producing for inventory looks profitable.** If you allocate $X of fixed cost per unit, building 1000 units (even unsold) makes the unit cost look low and "absorbs overhead." Throughput accounting says: only sales count. Inventory ties up cash and adds operating expense (storage, handling, obsolescence) — it's a liability, not an asset.
2. **Local cost cuts look like profit.** Cutting a non-constraint resource's cost (faster machine, cheaper labor at a non-bottleneck) doesn't change T. The system still produces at the constraint's pace. The "savings" are paper savings; real T is unchanged.

Goldratt's heresy: **cost accounting is the enemy of throughput thinking.** It makes managers optimize the wrong thing because it can't see system-level flow.

## The three questions for any proposed change

1. Does this change *increase Throughput*? (Are we selling more, or faster?)
2. Does this change *decrease Inventory*? (Less cash tied up, less WIP?)
3. Does this change *decrease Operating Expense*? (Lower run cost?)

If a proposed change can't show a yes to at least one — kill it. If it shows a yes on one but a no on another, weigh the magnitudes. Throughput dominates: a small T increase usually beats a small OE decrease, because T has no ceiling and OE has a floor.

## Domain translations (recap from SKILL.md)

| Domain | Throughput | Inventory | Operating Expense |
|---|---|---|---|
| Software | Features shipped to users | Open PRs, half-built features, started-not-shipped work | Team cost + tooling per unit time |
| Sales | Closed revenue | Pipeline (leads × time-in-stage) | Sales team cost + tooling |
| Hiring | Hires made | Candidates in pipeline | Recruiter time + interviewer time |
| Manufacturing | Sold units × contribution margin | Raw + WIP + finished-unsold | Plant operating cost |
| Personal | Outcomes that matter | Open loops, started-not-finished commitments | Your time |

## Common mistakes

- **Defining T as "output" instead of "sold output."** Features built but not shipped, leads generated but not closed — these are I, not T.
- **Ignoring I in knowledge work.** Started work that doesn't ship is the dominant form of waste in software, and most teams don't measure it. WIP age is the proxy.
- **Measuring per-team or per-stage instead of per-system.** Stage-level metrics encourage local optimization (the local-optima fallacy). Roll metrics up to system T/I/OE.

## Source

*The Goal* (1984), *The Haystack Syndrome: Sifting Information Out of the Data Ocean* (1990) — Goldratt's most direct treatment of throughput accounting vs. cost accounting.
