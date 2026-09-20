# os-builder - personal phase (detailed)

Goal: a working personal OS in about 10 minutes, seeded lightly, everything runs.

## 1. Identity
Write `me.local.md` and `me.local.json` from the interview (name, email, role, github, slack_id, timezone). These are gitignored. Confirm the email, since reply-all and inbox rules key off it.

## 2. Roster
Replace the demo roster table in `CLAUDE.md` and rewrite `team/roster.md` with the real team (name, role, email, github, slack, tz). If solo, keep just the user plus a note that teammates get added later.

## 3. Clear the demo (confirm first)
Per `docs/reset.md`, empty the Acme content but KEEP each domain's `CLAUDE.md`, `rules.md`, and the empty `knowledge.md` / `hypotheses.md`:
- `customers/accounts/*`, `customers/*-directory.md`
- `product/PRDs/*`, `product/product-context/*`, `product/roadmap/*`
- `competitive/competitors/*`
- `delivery/sprints/current/*`
- `team/accountability/team-loops.md` (empty the table, keep the header)
- `feature-index.yaml` (reset to their features)
Show the list and get a yes before deleting.

## 4. Seed one real thing
Ask for their top customer or current sprint and write one real file (a customer summary, or a sprint). An OS that is not empty on first open feels alive.

## 5. Connectors
Copy `.mcp.json.example` to `.mcp.json` and add the tools they named. Confirm each is reachable. If a tool is not connected, note that the relevant command will degrade gracefully.

## 6. Prove it
Run `/morning-briefing`. Fix anything that references a file you cleared. Then hand off: show the daily-loop commands and stop.
