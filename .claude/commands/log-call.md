# /log-call

Orchestrator: one transcript upload fans out across every system. Input: a transcript or notes (path or pasted). Run ALL steps in order - do not skip any, and call each skill explicitly (don't rely on auto-invocation).

1. **Summarize** - call the `call-summary` skill to produce the standard-format summary.
2. **File it** - save to `customers/accounts/<account>/calls/YYYY-MM-DD.md`; create the account folder if new.
3. **Update account summary** - refresh `customers/accounts/<account>/summary.md` (contacts, segment, open items).
4. **Commitments & follow-ups** - extract every commitment (ours and theirs) with owner + due date; if a teammate owes something, note it for `team/` accountability.
5. **Customer insights** - add new patterns to `customers/hypotheses.md`; promote to `rules.md` at 5 confirmations.
6. **People info** - for each your company teammate mentioned, call the `person-note` skill to update `people/profiles/<name>.md` (enablement-focused; private). Capture speculative reads in `people/hypotheses.md`.
7. **Feature index** - if the call touches a feature, add/update its entry in `feature-index.yaml`.
8. **Roadmap signal** - if the call implies a roadmap change, flag it for `product/roadmap/` (don't silently edit the roadmap).
9. **Verify** - list everything you created/updated so I can confirm nothing was missed.

This is the model for any "ingest one artifact, update many systems" workflow: a single command that conducts the existing skills.

## Sources
Transcripts can come from uploaded files, pasted text, or **Slack AI-note meeting transcripts** (pull via `slack_read_thread` / `slack_read_channel`). Same capture loop applies regardless of source.

## Transcript retention policy (summary-first; Hannah-aligned)
ALWAYS produce the standard summary, extract commitments into `open-loops.md`, and capture insights into the domain's `hypotheses.md`. Then decide what to do with the RAW transcript:
- **Keep raw** in `<domain>/sources/` - external-facing calls (customer, prospect/lead, partner, advisor) and internal meetings that produce decisions, vision, or strategy. High re-read value.
- **Link only** (summary in the OS + a link to the source, no copy) - when the transcript already lives in a system of record (Slack AI-notes, Gmail "Notes:" emails). Do not duplicate data.
- **Skip raw** - routine standups and pure logistics. These become a rolling digest in `team/dsu/`, not stored transcripts.
Test: "would I ever re-read the exact words?" If yes, keep raw; if the summary suffices, summary-only or link.

> When linking an AI-note (Gemini/Slack), link the ACTUAL meeting-notes doc (the "Open meeting notes" Google Doc URL), not the Gmail message URL. The doc link is what opens the notes.

## Classify: customer call vs internal prep
- **Customer call** = external customer/prospect attendees present. Full fan-out + keep raw (or link if AI-note).
- **Internal meeting ABOUT a customer** (prep, strategy, demo dry-run with only internal people) = log as ACCOUNT CONTEXT in `customers/accounts/<slug>/calls/<date>-internal-*.md`, summary-only, link the notes doc. Do NOT treat as a customer call; still capture decisions + any commitments into open-loops.

## Calendar as the detection signal
The calendar is the source of truth for whether a call happened and who attended. A meeting with any EXTERNAL attendee (domain not your-company.com / @your company.studio) is a customer call. Use it to find calls even when the transcript lives only in Attio: if no transcript is accessible, log a stub from calendar metadata (date, attendees, account) and flag "transcript in Attio - enrich."

## Attio (CRM) - pull the real transcript
When operating from an Attio-connected host (Claude Code), prefer Attio over a Gemini note for customer-call transcripts:
1. Use the Attio MCP to find the company/account record (e.g., "a customer").
2. Pull its recent calls / activities / notes; retrieve the transcript+summary for the target date.
3. Discover the exact Attio tool names at runtime (search records, get record, list activities/call recordings, get notes) - they vary by connector version.
4. Keep the raw transcript in `customers/accounts/<slug>/sources/` (real customer call) and summarize per the standard format; split action items into open-loops (mine) vs waiting-on (others); feedback -> account + product themes.
Host note: Attio is connected in Claude Code, NOT the Cowork desktop app. So Attio pulls/enrichment run from Claude Code; the desktop scheduled scan logs an Attio STUB flagged "transcript in Attio - enrich," which you (or a Claude Code run) then enrich.

## Full propagation checklist (run for EVERY customer call - do not stop at the call file)
After writing the call summary + raw, verify ALL of these fanned out:
1. Refresh `customers/accounts/<slug>/summary.md` - status, contacts, use case, next steps, decisions (don't leave it stale/"pending enrichment").
2. Write insight candidates to `customers/hypotheses.md` (promote at 5 confirmations).
3. Route feedback/signals to `product/roadmap/gtm-feedback-themes.md`.
4. Add the account to `customers/accounts/CLAUDE.md` if new.
5. Itemize NEW commitments into `open-loops.md` (mine) and `waiting-on.md` (others) - specific line items, not a generic "follow up."
6. Update `feature-index.yaml` if the call names features.
List what you updated.
