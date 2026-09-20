# Demo Guide - try Compound OS in 5 minutes

Open this folder in Claude Code, `cp me.local.example.md me.local.md`, then try these. Everything works against the built-in **Acme Corp** demo, no connectors or keys required.

1. **See the daily cockpit**
   `/morning-briefing`
   Assembles what's overdue, what to chase, customer follow-ups due, and sprint health from the repo.

2. **Ask the knowledge base**
   `What do we know about Globex, and what are they asking for?`
   Answers from `customers/accounts/globex/` with citations.

3. **Log a call (watch it compound)**
   `/log-call` then paste: *"Initech call: they want saved views before renewal, and asked about fleet alerts too."*
   It writes a summary, extracts commitments, and proposes a roadmap/feedback update.

4. **Keep the roadmap honest**
   `/roadmap-update`
   Reconciles `product/roadmap/roadmap.md` against `product/roadmap/gtm-feedback-themes.md` and cites the signal.

5. **See the team board**
   Open `views/team-pending.html` (or run `python3 views/build_team_pending.py` first).
   Every open item, grouped by owner, task vs follow-up.

6. **Plan next**
   `/suggest-plan`
   Synthesizes customer asks, competitive gaps, and QA signals into a ranked backlog proposal.

That is the loop: capture once, and every view gets sharper.
