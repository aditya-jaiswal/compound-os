# os-builder - team phase (detailed)

Run only when the user is ready to share with teammates. The repo already ships the primitives; this phase turns a personal OS into a shared one.

## 1. Shared vs private (already enforced by `.gitignore`)
Shared: customers, product, roadmap, delivery, competitive, design, quality, team-ops, commands, skills.
Private, per-user, never committed: `people/`, `personal-brand/`, `open-loops.md`, `waiting-on.md`, `daily/`, `me.local.*`.
Confirm nothing private is tracked: `git ls-files | grep -Ei 'me\.local|open-loops|waiting-on|people/|daily/'` must be empty.

## 2. Multi-user
Each teammate clones the repo, copies `me.local.example.md` to `me.local.md`, connects their own tools, and keeps their own private files locally. One shared repo, many people.

## 3. Accountability graduation + published board
- Personal items live in each person's private `open-loops` / `waiting-on`.
- Team-relevant items graduate to `team/accountability/team-loops.md` per `team/accountability/classification.md` (sanitized, owner-confirmed; `task` mirrors to a GitHub issue, `follow-up` stays on the board).
- Regenerate the shared dashboard with `python3 views/build_team_pending.py` and commit. Publish via GitHub Pages so viewers need no clone.

## 4. Rollout
Onboard one role at a time. Shared-domain edits go in via small commits or PRs. The rule: a piece of work is not done until the repo reflects it.

## Guardrails
Never publish `people/`. Drafts and proposals only. Keep the privacy check in every commit.
