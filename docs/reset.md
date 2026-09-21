# Reset to a blank OS (make it yours)

Compound OS ships populated with the fictional **Acme Corp** demo so you can see a working, lived-in system. To start your own, clear the demo content but keep the framework. The `os-builder` skill does this for you; the rules below are what it (or you) apply.

## What to KEEP (the framework)
- `CLAUDE.md`, `INDEX.md`, `feature-index.yaml` (structure; roster + content get replaced)
- Every domain's `CLAUDE.md`
- `.claude/` (commands, skills, agents, sources.md), `views/build_team_pending.py`
- `team/accountability/classification.md` (the graduation rule)
- `README.md`, `LICENSE`, `docs/`, `.gitignore`, `.claude-plugin/`, `me.local.example.*`

## What to CLEAR (the demo content) - rule-based, so it covers everything
1. **Memory files:** in every domain, reset `knowledge.md` and `hypotheses.md` to just their `# <domain> - ...` header line, and reset `rules.md` to just its `# <domain> - rules...` header line. (Removes all Acme facts, hypotheses, and promoted rules.)
2. **Working subfolders:** delete everything inside them, keeping the folders:
   `customers/accounts/*`, `customers/*-directory.md`, `product/PRDs/*`, `product/positioning/*`, `product/product-context/*`, `product/roadmap/*`, `competitive/competitors/*`, `design/reviews/*`, `engineering/rfcs/*`, `engineering/backlog/*`, `quality/qa/*`, `quality/seo/*`, `team/dsu/*`, `team/advisors/*`.
3. **Board + index:** empty the table in `team/accountability/team-loops.md` (keep the header), reset `feature-index.yaml` to `features: {}`.
4. **Delete** `DEMO-GUIDE.md` (it describes demo data that no longer exists).
5. **Create the private layer:** `open-loops.md`, `waiting-on.md`, `daily/` (empty).

## Verify clean
`grep -rIn -iE 'acme|globex|initech|hooli|umbrella|datenwerk|insighto|jordan rivera' . --include='*.md' --include='*.yaml' | grep -vE 'README|docs/|DEMO-GUIDE|\.claude/skills/os-builder'` should return nothing.

Then run `/log-call` on a real call and `/morning-briefing` to start your own compounding memory.
