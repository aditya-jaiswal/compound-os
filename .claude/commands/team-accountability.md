# /team-accountability  (daily producer - review then commit)

Build the shared team accountability picture from the common signals I see, hold each person to it, and publish a pull-free dashboard. Run daily. **Review before commit** - I approve the diff; nothing graduates silently.

## Inputs (the common signals)
- Today's **common-call transcripts**: DSU, design call, architecture call, customer calls (calendar-first; process all).
- The **GitHub board** (open issues / project items + assignees).
- New commitments surfaced in **multi-person threads** (group Slack / multi-recipient email).

## Steps
1. **Pull latest** the team repo (so I build on current state).
2. **Extract** action items + commitments from the signals, each with: owner, item, source-type, since, due, blocker.
3. **Classify** every item with `team/accountability/classification.md`. Keep TEAM items; drop PERSONAL ones into my own private ledger (never here). Flag sensitive items to the owner privately.
4. **Sanitize** TEAM items (strip inbox quotes / private framing) per the rule.
5. **Diff + review:** show me adds / status-changes / closes against `team/accountability/team-loops.md`. I approve or edit. (This is the control point - keep it in my hands.)
6. **Write** approved items to `team-loops.md` with a **Kind** (`task` vs `follow-up`, per `classification.md`). Only `task` items mirror to GitHub as issues (propose, then create on approval; never auto-create). `follow-up` items (email replies, sending docs, pings) stay page-only and never become tickets.
7. **Regenerate** the dashboard: run `python3 views/build_team_pending.py`.
8. **Commit + push** (`team: accountability <date>`). GitHub Pages serves the refreshed `team-pending.html` - teammates just open the link, no pull.

## Rules
- Review-then-commit always. Drafts/proposals only for anything that sends or creates (issues, nudges).
- Each teammate can run this for their own domain too; same review-then-commit.
- Nudges to owners are drafted for my review (no em dashes), never auto-sent.

## Account tagging (so account pages show the right pending items)
- The generator (`build_team_pending.py`) tags each item with an explicit **account slug** and the app's account page matches on that slug exactly (no fuzzy title-matching). Resolution order: (1) an explicit `[acct:<slug>]` token in the Notes column, (2) an `Account Name:` prefix on the item, (3) a unique known-account name mentioned in the item. Known accounts come from `customers/customer-directory.md` + the folders under `customers/accounts/`.
- **Convention:** when a loop belongs to an account, start the item with `Account Name: ...` (e.g. `IKS Health: send proxy doc`). If the account is not named in the item text, add `[acct:<slug>]` to Notes (the tag is stripped from the displayed note). This keeps every customer account's board reliable.
