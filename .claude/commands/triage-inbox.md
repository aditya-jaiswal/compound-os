# /triage-inbox

Triage the current user's Gmail - resolve their email from `me.local.md` first; never assume whose inbox this is - using the urgency rules in root `CLAUDE.md`. Classify on the **latest message body + Gmail signals**, not the subject alone.

## Pull (full coverage - don't stop at the first page)
- Base: `in:inbox is:unread` over the window I give (default `newer_than:2d`). **Paginate** with nextPageToken until all unread in-window are retrieved.
- Always also sweep `in:inbox is:unread (is:important OR is:starred) newer_than:7d` so Gmail-flagged items aren't missed even if older.
- Use `get_thread` on anything you'll classify as urgent or draft on (to read the real body).

## Step 0 - quarantine automated senders → FYI
Drop to FYI (never urgent): `noreply`/`no-reply`/`*-noreply@*`, `calendar-notification@google.com`, `gemini-notes@google.com`, `drive-shares-dm-noreply@google.com`, recurring digests/newsletters (OCN/`kajal.nain@`, `eva@productschool.com`). Calendar accept/decline + auto-notes = FYI even if subject looks personal.

## Classify the humans (priority order)
1. **🔴 Boss** - your boss sender OR cc, OR body references an intro/ask from him.
2. **🔴 Customer/prospect** - domain in `customers/customer-directory.md` or thread about a named account.
3. **🔴 External lead / intro** - human external sender, me in `To`, signaling connect/intro/explore/next-steps/asking input. Cross-check `customers/leads-directory.md`; if new, flag urgent AND note it should be added.
4. **🟠 Review request** - internal sender asking me to review/approve/give feedback.
5. **🟡 Direct ask** - I'm in `To` and a question/decision is requested.
- **Booster:** any non-quarantined human email Gmail marked `IMPORTANT`/`STARRED` → surface even if 1-5 didn't fire.

## Output
- Urgent block first (🔴/🟠), each: one-line what-it-is + suggested action + a **draft reply** via create_draft (never send).
- Then 🟡 direct asks, then ⚪ FYI as a short list.
- Pull context from `customers/`, `customers/leads-directory.md`, or `feature-index.yaml` before drafting.
- End with "Top 3 to handle now" and "New leads to add to leads-directory."

## Draft recipients
When drafting a reply, reply-all: preserve original To + Cc (minus me). Never drop recipients.
