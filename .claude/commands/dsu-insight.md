# /dsu-insight  (run from Claude Code - needs GitHub; "Sprint OS" daily standup insight)

Generate the daily standup-insight report that fuses the DSU transcript with GitHub - the visual accountability artifact (match `team/dsu/templates/dsu-insight-template.html`). Ethos: **to help and align, not to rank.**

## Inputs
Today's DSU transcript (Gemini "Daily standup" notes / Slack) + GitHub (open PRs, issues, statuses).

## Produce (same structure as the template)
1. **Headline + one "Act now"** - the week's #1 flow risk (e.g. an unreviewed PR stack, a single-point bottleneck).
2. **KPIs:** open PRs to review · blockers to clear · commitments traced · # people in standup.
3. **Per person - "who said what vs what shipped":** each stated commitment as ○ open / ✓ shipped, **linked to the actual GitHub PR/issue**; verify shipped-vs-said against GitHub (did the PR merge?). Blockers as ⚠ with a one-line workaround. "Asks" as → who-owes-what.
4. Render to `team/dsu/insight-<date>.html`.

## Then fan out (so it drives outcomes, not just displays)
- Action items + asks → `open-loops.md` (mine) / `waiting-on.md` (others).
- Flow risks (review latency, single-point bottlenecks, off-this-week owners) → `delivery/sprints/current/status.md` + recompute June-30 reachability.
- Recurring patterns → `team/hypotheses.md`; chronic → `rules.md`.

> Alternative generator: your team's Sprint OS via `your company.pipe` already produces this - dogfood it, then fan out into the OS here. Pair with `/sprint-board` + the daily scan.
