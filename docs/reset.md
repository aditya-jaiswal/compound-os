# Reset to a blank OS (make it yours)

Compound OS ships populated with the fictional **Acme Corp** demo so you can see a working system. To start your own, clear the demo content but keep the framework (rules, memory-engine files, commands, skills).

## Quick reset
1. **Identity:** `cp me.local.example.md me.local.md` and fill it in. Update `team/roster.md` and the roster table in `CLAUDE.md` with your real team.
2. **Clear demo content** (keep each domain's `CLAUDE.md`, `rules.md`, and empty `knowledge.md` / `hypotheses.md`):
   - `customers/accounts/*`, `customers/*-directory.md`
   - `product/PRDs/*`, `product/product-context/*`, `product/roadmap/*`
   - `competitive/competitors/*`
   - `delivery/sprints/current/*`
   - `team/accountability/team-loops.md` (empty the table, keep the header)
   - `feature-index.yaml` (reset to your features)
3. **Regenerate the board:** `python3 views/build_team_pending.py`.
4. **Start capturing:** run `/log-call` on a real transcript and `/morning-briefing` to see it work on your data.

Keep it minimal at first. Add content as you go; the memory engine compounds from there.
