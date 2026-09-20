# /slack-catchup

Catch up on Slack: DMs, @-mentions, and key channel activity I need to act on. Resolve people/channels via `team/roster.md`. Window: last 24h unless I specify.

## Pull
- **@-mentions of me** (the current user's `slack_id` from `me.local.md` - resolve it first, never assume): `slack_search_public_and_private` for recent mentions.
- **DMs:** recent direct-message threads needing a reply.
- **Key channels** (from roster): #dev, #dev-rel, #dev-qa, #dev-design, and customer channels (#globex, #initech-dev, #hooli-dev).
- **AI-note meeting transcripts** posted in channels: flag them and offer to run `/log-call`.

## Classify (same urgency rules as email)
Boss (your boss), customer/prospect channels, review requests, and direct questions to me = urgent. Surface those first; group the rest as FYI.

## Output
- "Needs my reply" with a suggested **draft per item** (`slack_send_message_draft`, never send).
- "FYI / status" digest.
- Any meeting AI-notes found, offer `/log-call`.
Drafts only. Never auto-send.
