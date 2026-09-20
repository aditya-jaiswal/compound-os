# Architecture

Three layers:
1. **The repo** - domain-organized knowledge + a compounding-memory engine + commands/skills.
2. **The engine** - Claude Code, run locally, reads the repo and your connectors, does the work.
3. **The app (optional, fast-follow)** - a local UI that renders the views and runs the engine as chat.

Key patterns: lean root router + progressive disclosure; knowledge/hypotheses/rules with promote/demote; two-sided accountability with a privacy wall; the `me.local` identity layer so one shared repo serves many people.
