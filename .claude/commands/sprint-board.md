# /sprint-board  (run from Claude Code - needs GitHub)

Status of the current sprint against the June 30 release.

1. Pull GitHub Project items by status (todo / in-progress / blocked / done) and by person.
2. Overlay the alerts module **critical path** (policy engine → enforcement → reasoning graph → AI BOM → govern dashboard). Flag any critical-path item not on track.
3. Flag blocked items + who's blocking; cross-ref `waiting-on.md`.
4. Compare burn vs the week-by-week plan; call out slippage and the June 30 risk.
5. Update `delivery/sprints/current/status.md` and surface the top 3 risks + recommended moves.

## Day plan check
If `delivery/sprints/current/day-by-day-*.md` exists, check TODAY's planned deliverables against GitHub status; flag any slip into open-loops (mine) / waiting-on (others) and recompute whether the deadline is still reachable.
