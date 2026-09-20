# Compound OS

> A compounding-memory operating system for product teams, run by AI in Claude Code.
> **This root file loads every session. Keep it LEAN.** Do not add to it automatically; edit only when explicitly asked.
> The content below is a **fictional demo** (Acme Corp). Replace it with your own: run the `os-builder` skill (guided setup), see `docs/reset.md`, or edit by hand.

## Who am I
This is a shared **Team OS**. Your identity is personal and local, never committed. On first run, copy `me.local.example.md` to `me.local.md` (gitignored) and fill in your name, email, role, and handles. Read `me.local.md` to learn the current user. Never infer the user from this file or the roster's order.

## How to navigate this OS
- Organized by **domain**. Each domain has a `CLAUDE.md` (what's here + rules); larger domains also get an `INDEX.md` map once they grow.
- **For anything feature-related** check `feature-index.yaml` FIRST; it maps every feature to its artifacts across domains.
- Read a domain's `rules.md` before acting in it.
- Read **summary** files before raw transcripts. Open raw material only if the summary lacks the answer.
- See `INDEX.md` for the full route map.

## Team
Compact resolution table (always loaded). Full directory in `team/roster.md`. Internal domains: your company's email domains (set during setup).

| Name | Role | Email | Slack |
|------|------|-------|-------|
| Chris Vale | Founder & CEO | chris@acme.com | U0CEO |
| Jordan Rivera (you) | Director of Product | jordan.rivera@acme.com | U0PM1 |
| Sam Chen | Director of Engineering | sam@acme.com | U0ENG |
| Robin Park | Director, AI | robin@acme.com | U0AI1 |
| Priya Nair | Product Designer | priya@acme.com | U0DSN |
| Dana Osei | QA / Delivery | dana@acme.com | U0QA1 |
| Alex Kim | Senior Engineer | alex@acme.com | U0EN2 |
| Devon Ross | Founding Engineer | devon@acme.com | U0EN3 |
| Sasha Ito | Full-stack Engineer | sasha@acme.com | U0EN4 |
| Noah Berg | Full-stack Engineer | noah@acme.com | U0EN5 |
| Riley Fox | Engineering Intern | riley@acme.com | U0INT |
| Taylor Vance | Business Development | taylor@acme.com | U0BD1 |
| Jamie Lang | Growth | jamie@acme.com | U0GRW |

## Connected sources
External systems and how to use them are indexed in `.claude/sources.md`. Each user connects their own Gmail / Slack / Calendar / GitHub. Never commit secrets; connectors are per-user.

## Email & response urgency rules
Classify on the **latest message body** plus the mail client's own signals.

**Step 0 - quarantine automated mail (never urgent):** `noreply` / `no-reply`, calendar notifications, auto meeting-notes, recurring digests/newsletters. Calendar accepts/declines are FYI.

**Urgent, surface FIRST, in order:** (1) Boss (your boss, marked in team/roster.md, is sender or cc, or the body cites a request from them). (2) Customer / prospect (sender domain in `customers/customer-directory.md`, or a named-account thread). (3) External lead / intro (a human external sender with me in `To`, signaling connect / next-steps). (4) Review request from a teammate. (5) Direct ask to me.

**Booster:** if a human email is marked IMPORTANT or STARRED, surface it. **Coverage:** page through ALL unread, not just the latest N. **Be quick:** draft replies for urgent items; drafts only unless I say otherwise.

## Drafting style (applies to ALL drafts, email / posts / docs)
- **Never use em dashes.** Use commas, periods, or parentheses; "to" for ranges.
- **Create drafts directly, do not ask permission.** A draft is reversible and never sends. Only **sending** needs explicit approval.
- **Reply-all by default, preserve recipients.** To = original sender plus everyone in the original To; Cc = everyone in the original Cc. Remove only the current user's own address (from `me.local.md`). Never silently drop a recipient.

## The compounding memory engine (apply in every insight domain)
Each insight domain holds three files:
- `knowledge.md` - stable facts and patterns
- `hypotheses.md` - unconfirmed, needs more data
- `rules.md` - confirmed, **apply by default**

Loop: **before a task** review the domain's `rules.md` and apply by default; check if an open hypothesis can be tested today. **After a task** append new insights to `hypotheses.md` (or `knowledge.md` for plain facts). **Promote** a hypothesis to a rule when confirmed 5+ times. **Demote** a rule to a hypothesis when new data contradicts it.

## Auto-sharding rules (never shard early)
Keep memory files and folders **flat** until a file exceeds ~40 entries OR a folder exceeds ~20 children. When a threshold is crossed: create theme subfolders, move items, add a nested `CLAUDE.md` + `INDEX.md`, and update the **nearest** index (never this root file automatically).

## Privacy (structural, not a setting)
Shared with the team: customers, product, roadmap, delivery, competitive, design, quality, team-ops. Private and per-user, never committed (see `.gitignore`): `people/`, `personal-brand/`, `open-loops.md`, `waiting-on.md`, `daily/`, `me.local.*`. Team-relevant items graduate from a private ledger to the shared board, sanitized and owner-confirmed (see `team/accountability/classification.md`).

## Top-level doc index
| Domain | Path | What |
|--------|------|------|
| Customers | `customers/` | Accounts, call summaries, follow-ups |
| Product | `product/` | Vision, PRDs, positioning, roadmap |
| Competitive | `competitive/` | Competitor intel |
| Design | `design/` | Design reviews, vision alignment |
| Engineering | `engineering/` | Backlog, RFCs, tech research |
| Delivery | `delivery/` | Sprints, board sync, velocity |
| Quality | `quality/` | QA on production, SEO |
| Team | `team/` | Roster, DSU digests, accountability |
| People ⚠ | `people/` | PRIVATE, per-user, never committed |
| Feature index | `feature-index.yaml` | Cross-domain feature lookup |
