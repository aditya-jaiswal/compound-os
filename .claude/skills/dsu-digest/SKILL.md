---
name: dsu-digest
description: Turn daily standup updates (Slack or notes) into a structured team digest with accountability tracking. Use after the DSU.
---

# DSU Digest

From the standup input, produce:
- **Per person:** what they did / doing / blockers.
- **Accountability check:** anything promised previously that's now overdue (cross-check `team/` and `delivery/`).
- **Cross-functional flags:** dependencies, handoffs, things needing my decision.
- **Follow-ups for me:** who I need to unblock, chase, or support today.

Save to `team/dsu/YYYY-MM-DD.md`. Capture recurring patterns (e.g. chronic blockers) into `team/hypotheses.md`.

## Retention
Produce the digest only. Do NOT store raw standup transcripts (summary-first; see the retention policy in /log-call). Keep a rolling digest in team/dsu/.
