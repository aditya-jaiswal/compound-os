# /draft-reply

Draft a reply to a specific email thread. Input: a thread (subject, sender, or thread ID) + optional intent.

1. `get_thread` to read the full latest message.
2. Pull relevant OS context: if customer → `customers/`; if feature → `feature-index.yaml`; if internal review → the doc in question.
3. Write the reply using the `email-voice` skill (my tone + signature).
4. Create it as a **Gmail draft** (create_draft) on that thread - do not send.
5. Show me the draft text and what context informed it.

## Recipients (reply-all by default)
- To = original sender + all original To recipients. Cc = all original Cc recipients.
- Remove only the current user's own address (their email from `me.local.md`). Never drop anyone else unless I say so.
- Read the thread's To/Cc first; pass cc=[...] to create_draft so Cc is preserved.
