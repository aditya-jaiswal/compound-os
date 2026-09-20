# /accountability-check

Find commitments that are slipping and prepare nudges.

1. **Gather open commitments:** `customers/` follow-ups, `delivery/` sprint tickets, `engineering/` backlog, `team/dsu/` notes, and recent call summaries.
2. **Cross-reference activity:** Slack, GitHub, and email for progress signals.
3. **Flag stale / overdue** items with owner, what was promised, and how long it has been quiet.
4. For each, draft a **respectful nudge** (`slack_send_message_draft` or an email draft) tagged to the owner. Never auto-send.
5. Log chronic patterns to `team/hypotheses.md` (promote to `rules.md` at 5 confirmations, e.g. "X consistently slips on documentation").

## Self mode (audit MY loops)
Run against `open-loops.md`:
1. For each draft pending send, check Gmail Sent / Slack "Sent" to see if it actually went out. Mark sent/done or keep pending.
2. Flag commitments past their by-when as OVERDUE (with how many days).
3. Re-scan inbox + Slack for new items I owe a reply to or new commitments; append them to `open-loops.md`.
4. Report: X drafts unsent, Y commitments overdue, Z new items. Offer to draft the follow-ups. Never auto-send.

## Ledgers
- MY items: `open-loops.md` (self mode above).
- OTHERS' items: `waiting-on.md` - for each `Nudge? = yes` that's stale, draft a respectful nudge to the owner (Slack/email draft, never send). Move done items to done; promote chronic slippers to `team/hypotheses.md`.

## Graduate to the shared board (Team-OS hand-off)
For team-relevant, work-tied items in `waiting-on.md` (owed by a teammate on shared work), flag candidates to GRADUATE into GitHub (a tracked issue with owner + due) so the team has visibility - sanitized of private email context, and only once the owner can confirm. Never push personal/sensitive items (boss, sales-confidential, hiring) to the shared board. Propose; never auto-create.

## Classification + team graduation
Use `team/accountability/classification.md` to decide personal vs team for every item. The daily team rollup + publish is handled by `/team-accountability` (review-then-commit → `team/accountability/team-loops.md` → `views/team-pending.html`). This command focuses on MY ledgers; team graduation flows through there.
