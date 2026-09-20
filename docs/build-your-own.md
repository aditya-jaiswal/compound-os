# Build your own

1. Clone the repo. Copy `me.local.example.md` to `me.local.md` and fill it in.
2. Open in Claude Code. Run `/morning-briefing` to see it work against the Acme demo.
3. Replace the demo: clear the demo content in each domain, keep the `rules.md` + memory files, and start logging your own calls with `/log-call`.
4. Connect your tools (Gmail, Slack, Calendar, GitHub) as your own MCP connectors.
5. Optional: set up the semantic-search layer (`scripts/setup-brain.sh`) with your own embedding key.

The `os-builder` skill automates steps 1 to 4 with an interview.
