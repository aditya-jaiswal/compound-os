---
name: os-builder
description: Set up the user's own Compound OS. Use when the user says "set up my Compound OS", "set up my OS", "make this mine", "onboard me", "build my team OS", "customize this repo", or opens Compound OS for the first time. One-sentence front door: it interviews briefly, then scaffolds a working personal OS. Do NOT use for daily work (that is the individual commands like /morning-briefing) or for the team-sharing split alone (say "share my OS with my team").
---

# os-builder

The single front door for a new user. In one sentence ("set up my Compound OS") this turns the Acme demo into the user's own working OS. Interview briefly, do all the file work yourself, end on a win that needs no connectors. Keep it dead simple.

## Constraints (read first, these override convenience)
- Do ALL file edits yourself. The user never has to open or edit a file, run a shell command, or read a doc.
- Confirm ONCE before clearing the demo (show a one-line summary of what changes). Otherwise do not interrogate.
- Drafts and proposals only for anything that sends or creates externally. Never send. Never use em dashes.
- Privacy wall: never create content in `people/`; it stays empty and gitignored.
- Minimal first. Do not ask for anything you do not need to produce a working OS.

## Step 0 - Detect context
- **Repo present** (a `CLAUDE.md` with the memory-engine section + domain folders exist here): customize in place.
- **Plugin-only** (installed via the marketplace, no domain tree in this folder): offer to scaffold the Compound OS tree into the current folder (or `git clone` the template), then customize. Ask once which folder.
- **First run** = `me.local.md` is missing OR still contains the demo values ("Jordan Rivera"). If it already has real values and the user asks about teammates, load `team.md` instead.

## Step 1 - Ask only the essentials (one short batch)
Required: name, email, role, company + one line on what it does, teammates (names + roles, or "solo").
Say these are optional and can be added later: Slack ID, GitHub handle, and connecting Gmail/Slack/Calendar/GitHub. Do not block on them.

## Step 2 - Scaffold (do it all; see `personal.md` for detail)
1. Write `me.local.md` + `me.local.json` from the answers (gitignored).
2. Replace the roster in `CLAUDE.md` + `team/roster.md` with their team (or just them).
3. Clear ALL Acme demo content per `docs/reset.md` (rule-based: reset every domain's knowledge/hypotheses/rules to their headers, empty all working subfolders, empty the team-loops table, reset feature-index, delete DEMO-GUIDE.md). Confirm once first.
4. Create the empty private layer: `open-loops.md`, `waiting-on.md`, `daily/` (so the daily commands have something to read).
5. Seed one real thing if they offered a customer or current sprint.
6. Reset `feature-index.yaml` to a stub with their features (or empty with the header).
7. Remove the demo banner line from `CLAUDE.md` (the `> ...fictional demo...` note) and set the internal email domain(s) from their company.
8. Delete `DEMO-GUIDE.md` (it references demo data that no longer exists).

## Step 3 - First win (no connectors needed)
Prove it works with repo-only output: open `views/team-pending.html`, or answer a question about the seeded item, or run `/suggest-plan` on what exists. Do NOT lead with `/morning-briefing` (it needs a connected inbox).

## Step 4 - Offer the optional next steps
Briefly: "Want to connect your inbox/Slack so `/morning-briefing` and `/triage-inbox` work? Or add teammates and share it?" Only proceed if they say yes (connectors: `personal.md` step 5; sharing: `team.md`).

## Output template (end every run with this)
```
Your Compound OS is set up.
- You: <name>, <role> at <company>
- Team: <n> people in team/roster.md
- Demo cleared, framework kept (8 domains, memory engine, commands)
- Seeded: <the one real thing, or "nothing yet">
- Try it now: <the exact first-win action you ran>
Next (optional): connect tools, add teammates, or run /log-call on a real call.
```

## Worked example (one run, condensed)
> User: "set up my Compound OS"
> You: "Welcome. Quick setup. What's your name, email, and role? Your company and one line on what it does? And your teammates (names + roles), or are you solo for now? (Slack ID, GitHub, and connecting your inbox are optional, we can add them after.)"
> User: "Sam Okafor, sam@nimbus.io, Senior PM. Nimbus, a B2B scheduling tool. Team: Lee (eng lead), Mia (designer), Ravi (QA)."
> You: "Got it. I'll set you as the user, put your 4-person team in the roster, clear the Acme demo (keeping all the rules and structure), and create your private files. Confirm?"
> User: "yes"
> You: [write me.local, roster; clear demo; create open-loops/waiting-on/daily; stub feature-index] then: "Done. Opening your team board (empty for now). Try: 'log my last customer call' to start the memory. Want me to connect your inbox next?"

## Shortcuts you take (do not)
| Shortcut | Why it is wrong |
|---|---|
| Telling the user to edit a file or run `cp`/`git` themselves | The point is one sentence; you do the file work |
| Asking for Slack ID / connectors before scaffolding | Blocks a new user on question one; these are optional |
| Ending with `/morning-briefing` as the proof | It needs connectors a new user does not have yet; the "win" fails |
| Skipping the clear-demo confirmation | Deleting their view of the demo without a yes feels unsafe |
| Populating `people/` with the roster | `people/` is private notes only, never the team list |

## Exit checklist (all must be true)
- [ ] `me.local.md` has real values, no "Jordan Rivera" left anywhere.
- [ ] Roster in `CLAUDE.md` + `team/roster.md` is theirs.
- [ ] No demo residue anywhere live: `grep -rIn -iE 'acme|globex|initech|hooli|umbrella|datenwerk|insighto|jordan rivera' . --include='*.md' --include='*.yaml' | grep -vE 'README|docs/|DEMO-GUIDE|skills/os-builder'` returns nothing.
- [ ] `open-loops.md`, `waiting-on.md`, `daily/` exist (even if empty).
- [ ] The first-win action actually ran and returned something.
- [ ] No em dashes in anything written.

## Next
Daily use: `/morning-briefing`, `/log-call`, `/sprint-board`. Sharing with the team: load `team.md`.
