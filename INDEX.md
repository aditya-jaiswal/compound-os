# Compound OS - Top-Level Index
> `CLAUDE.md` is the lean always-loaded router. This is the full map.

## Operating files
- `CLAUDE.md` - root context (identity, roster, rules, memory engine, sharding).
- `feature-index.yaml` - every feature mapped to its artifacts. Check first for feature questions.
- `me.local.example.*` - copy to `me.local.*` (private) to set the current user.

## `.claude/`
- `commands/` - the daily-loop commands (morning-briefing, triage-inbox, draft-reply, email-followups, log-call, ingest-source, eod-capture, day-plan, sprint-board, capacity, whatif, gap-check, team-accountability, accountability-check, roadmap-update, design-review, qa-check, draft-post, suggest-plan, slack-catchup, dsu-insight).
- `skills/` - call-summary, dsu-digest, email-voice, linkedin-voice, person-note, os-builder (first-run setup).
- `agents/` - researcher, reviewer.
- `sources.md` - how connectors are used (per-user).

## Domains (each: CLAUDE.md + rules.md + knowledge.md + hypotheses.md + working subfolders)
| Domain | Path | Memory engine? |
|--------|------|----------------|
| Customers | `customers/` | yes |
| Product | `product/` | yes |
| Competitive | `competitive/` | yes |
| Design | `design/` | yes |
| Engineering | `engineering/` | yes |
| Delivery | `delivery/` | yes |
| Quality | `quality/` | yes |
| Team | `team/` | yes |
| People ⚠ PRIVATE | `people/` | per-user, never committed |

## Views
- `views/` - generated dashboards (e.g. `team-pending.html`), built by `views/build_team_pending.py` from `team/accountability/team-loops.md`.

## Self-accountability (private, per-user)
- `open-loops.md` - what I owe. `waiting-on.md` - what others owe me. Both gitignored.

## Getting started
See `README.md` (quickstart), `docs/build-your-own.md` (make it yours), `docs/reset.md` (clear the demo).
