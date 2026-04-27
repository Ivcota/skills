# Drum-Buffer-Rope

The operational scheduling pattern of TOC. Once the constraint is identified, DBR is *how you run the system day-to-day* against it.

## The three pieces

- **Drum** — the constraint sets the pace. Everything else syncs to its rhythm. The constraint is the system's drumbeat; non-constraints don't get to march to their own.
- **Buffer** — a *time* buffer (not inventory) sits in front of the constraint. Protects it from upstream variability so it never starves. The buffer is sized in *time* (e.g., "two hours of work always staged in front of the constraint") not units.
- **Rope** — a signal pulling new work into the system at the constraint's rate. Holds back upstream stages so they can't release work into the system faster than the constraint can absorb it. Prevents WIP buildup upstream.

## Why all three

Each piece fails alone:
- **Drum without rope** → upstream still pushes work in faster than the constraint absorbs. WIP piles up. The constraint is set; the inflow isn't.
- **Drum without buffer** → upstream variability starves the constraint occasionally. Every minute the constraint is starved is a minute of lost system T (and you can never get it back).
- **Buffer without drum** → the buffer floats; nobody knows how big it should be or what it's protecting. Eventually it grows or shrinks unpredictably.
- **Rope without drum** → you're throttling inflow, but to what rate? Rope rate must be the drum rate.

## Domain translations

### Software (development flow)

- **Drum** — the slowest stage. In most teams it's *code review* or *QA / staging*. Sometimes deploy bandwidth. Identify it by where PRs / tickets pile up oldest.
- **Buffer** — a small queue of "ready for review" or "ready for QA" work just before the bottleneck. Aim for ~1-2 days of constraint work staged. Less and the constraint starves; more and you're hiding WIP that should be pulled back.
- **Rope** — WIP limits per stage upstream. New tickets are pulled into "in progress" only when the bottleneck pulls something out of its queue. Most teams call this Kanban; what makes it work is the rope, not the board.

The Rope is the half of Kanban most teams don't implement. Without WIP limits at *every upstream stage*, the team keeps starting work to feel productive (busyness fallacy) and the bottleneck queue grows.

### Sales (pipeline flow)

- **Drum** — the closer's capacity. AEs only have so many calls per week. T is set by close rate × closer hours.
- **Buffer** — a small pool of qualified, scheduled-but-not-yet-pitched leads. Closers should never have an empty calendar; nor should they have a 4-week backlog (lead heat decays).
- **Rope** — SDRs throttle prospecting when the closer queue is full. Counterintuitive but correct: an SDR generating leads that go stale before the closer can reach them is destroying T (lead decay) and OE (SDR time).

### Hiring (candidate flow)

- **Drum** — the interview-loop scheduler or the hiring manager's final-decision capacity.
- **Buffer** — a small pool of fully-vetted candidates ready for the next stage.
- **Rope** — recruiters throttle sourcing when the loop is backed up. A 30-day delay between phone screen and on-site loses good candidates to other offers (T loss) and burns recruiter cycles re-engaging cold ones (OE waste).

### Personal productivity

- **Drum** — your deep-work hours per day. Probably 2-4. T is whatever ships in those hours.
- **Buffer** — a short list of "ready-to-execute" work staged for the next deep-work block. Not a 50-item backlog; ~3 next things.
- **Rope** — stop saying yes to new commitments when the buffer is full. The "yes by default" rule is the rope cut; the buffer overflows; deep-work hours get consumed by shallow work; T collapses.

## Sizing the buffer

Goldratt's rule of thumb: buffer sized to absorb most upstream variability without starving the constraint. Start small and grow it only if the constraint actually starves.

- Too small: the constraint runs out of work; T drops.
- Too big: WIP hides; lead times grow; defects accumulate without being noticed; you're back to push instead of pull.

In practice: start with ~1.5x the typical upstream cycle time, then watch. If the buffer is consistently green (always full, never below a third), it's too big — shrink it. If it dips into red (near-empty) more than rarely, it's too small or upstream variability is too high.

## Why the rope matters most

The rope is the part that distinguishes TOC from "just identify the bottleneck and add capacity." Without it:

- Upstream stages keep pushing.
- WIP piles up.
- Cycle time grows. (Little's Law: cycle time = WIP / throughput. Throughput is fixed by the drum, so more WIP → longer cycle time, period.)
- Defects accumulate (work sits, rots, gets reworked).
- Local optima fallacy gets worse — upstream stages produce more, "looks" productive, doesn't help T.

The rope says: **don't release work into the system faster than the constraint can absorb.** This single rule, applied seriously, fixes most "we're slow despite working hard" problems even before any other TOC move.

## Common DBR failures

- **Implicit drum.** Team agrees there's a bottleneck but never names it. Everyone subordinates to a different mental model of where the drum is.
- **Inventory buffer instead of time buffer.** Counting units in front of the constraint instead of time. Time is what matters — the constraint must not be idle.
- **No rope.** Drum and buffer set up; upstream still pushes. Buffer overflows; WIP piles upstream of the buffer; cycle time blows up.
- **Rope but no drum.** WIP limits set per stage with no recognition of which stage is the constraint. Limits are arbitrary; some stages choke, others sit idle.

## Source

*The Goal* (1984), *The Race* (1986) — Goldratt's most direct DBR treatments. *The Phoenix Project* (2013, Kim et al.) applies DBR to IT/software with named characters and worked examples.
