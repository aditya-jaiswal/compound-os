# /morning-briefing

My daily start-of-day briefing. Save to `daily/briefings/YYYY-MM-DD.md`.

0a. **Open loops (mine)** - read `open-loops.md`. Verify "draft pending send" against Gmail Sent / Slack (mark done if shipped). Flag anything past its by-when as OVERDUE. Lead with what's overdue or still on me.
0b. **Waiting on others (chase)** - read `waiting-on.md`. List items where `Nudge? = yes`, sorted by most overdue first; for each, a one-line **draft nudge** (Slack via roster ID, or email) I can fire. Keep "monitor" items as a short FYI line.
1. **Competitor & market** - latest from `competitive/` (competitor registry + profiles). Lead with anything that changes a decision.
2. **Inbox triage** - run the `/triage-inbox` logic (urgency rules; create drafts for urgent items).
3. **Slack** - overnight DMs, @-mentions (me = the current user's `slack_id` from `me.local.md`), key channels; resolve people via `team/roster.md`. Surface what needs my reply (draft, never send). When searching for my mentions, pass the mention **literally** as `<@SLACKID>` - never HTML-escaped (`&lt;@…&gt;` matches nothing, so those mentions are silently missed).
4. **Customer follow-ups due** - from `customers/accounts/` (commitments, demos, features promised).
5. **Delivery status** - current sprint health from `delivery/sprints/current/`; flag blockers and at-risk items.

End with the 3 things that most need my attention today (do + chase).
