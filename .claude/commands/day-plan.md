# /day-plan  (repeatable - works for any release/month)

Turn a goal + deadline into a comprehensive day-by-day schedule that keeps every workstream accountable.

## STEP 0 - Build the COMPLETE deliverable map first (do not skip)
A goal usually has MULTIPLE parallel tracks. Aggregate deliverables from ALL signals, not one doc:
- the release/plan doc(s) in `delivery/sprints/current/`
- recent **DSU digests** + **design-sync** notes (`team/dsu/`) - UI/design/QA work lives here
- **product roadmap** (`product/roadmap/*`, e.g. analytics V1 dates) and product-context
- **waiting-on.md** / **open-loops.md** (in-flight + ad-hoc commitments)
- **quality/** (QA, staging) and **engineering/arch-reviews/**
Write/refresh `workstreams.md` (tracks → deliverables → owners → cross-track dependencies). If a track is implied but not in the OS, ASK before finalizing.

## STEP 1-5 - Schedule
1. Identify the critical path + **cross-track dependencies** (e.g. design system → UI revamp; platform features → the UI that surfaces them).
2. Pull GitHub estimates (from Claude Code) + `delivery/capacity.md` + calendar; if no estimates, sequence by dependency and say so.
3. Work backward from the deadline: reserve feature-freeze + QA buffer; close the critical path with slack; respect weekends/PTO/timezones.
4. Lay out every day as a **track-by-track grid** (one column per track) with owners + a daily done-check.
5. Flag standing risks (bottlenecks, fragile envs, slipping prerequisites, missing estimates). Write `delivery/sprints/current/day-by-day-<deadline>.md` and (re)render the calendar artifact.

Pair with `/sprint-board` daily; re-run to replan when reality shifts.
