# Connected sources
How this OS reaches external systems. Each user connects their OWN accounts; nothing here is shared or committed. Configure via `.mcp.json` (gitignored; see `.mcp.json.example`).

| System | Used by | Notes |
|--------|---------|-------|
| Gmail | `/triage-inbox`, `/draft-reply`, `/email-followups` | Drafts only; sending needs explicit approval |
| Slack | `/slack-catchup`, `/team-accountability` | Resolve people via `team/roster.md` |
| Calendar | `/morning-briefing`, `/day-plan` | Meeting detection, availability |
| GitHub | `/sprint-board`, `/capacity` | Available in Claude Code; ticket suggestions only |

If a connector is not configured, the command degrades gracefully (reads the repo and tells you what it could not fetch). Never commit tokens.
