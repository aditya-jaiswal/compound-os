# /email-followups

Catch anything waiting on me or on others. Apply the Step 0 quarantine first (ignore automated senders). Cover ALL unread/relevant threads in-window (paginate), not just the first page.

## 1. Awaiting MY reply (I owe a response)
Find inbox threads where the latest message is from a human (not quarantined) and I haven't replied since. Heuristic: `in:inbox -in:sent newer_than:7d`, then check last sender ≠ me with no later SENT from me. Prioritize by urgency rules: boss > customer > external lead/intro > review > direct ask. Include Gmail `IMPORTANT`/`STARRED` items as a safety net.

## 2. Awaiting THEIR reply (nudge candidates)
Threads where my last SENT got no reply after 2+ business days - especially customers, prospects, and external leads where I asked a question.

## Output
- "You owe a reply" - each with a suggested **draft reply** (create_draft, don't send).
- "Waiting on them - consider nudging" - each with a suggested **draft nudge**.
- Flag overdue commitments tied to `customers/` follow-ups or `team/` accountability.
