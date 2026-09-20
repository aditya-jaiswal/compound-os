<div align="center">

# Compound OS

**A compounding-memory operating system for product teams, run by AI in your terminal.**

*Turn scattered context into a shared brain that gets smarter every day.*

</div>

---

## The problem

A product team runs on scattered context. Customer calls live in transcripts, commitments live in inboxes, plans live in someone's head, competitor moves live in a newsletter, the roadmap drifts from what customers actually said, and "who is free, and by when" takes a day to answer. Knowledge does not compound. The same questions get re-answered every week, and the answers walk out the door when someone leaves.

## The idea

Compound OS is a git repo plus a library of AI commands you run in [Claude Code](https://docs.claude.com/en/docs/claude-code). The repo is a **domain-organized knowledge base** with a **compounding-memory engine** at its core: every call, decision, and commitment is captured once, structured, and reused everywhere. An AI chief of staff sits on top and runs the daily work, capturing calls, triaging email, planning sprints, holding the team accountable, and keeping the roadmap honest.

It compounds because memory is a first-class idea, not an afterthought. Facts get promoted from *hypothesis* to *rule* as they're confirmed, and demoted when reality disagrees. The longer you run it, the sharper it gets.

## How it works

Three ideas do most of the work:

**1. Domain-organized memory with a lean router.** The repo is split by domain (customers, product, roadmap, delivery, competitive, design, quality, team). A lean root `CLAUDE.md` loads every session and routes; detail lives in each domain and loads only when needed. This is progressive disclosure applied to a knowledge base, so context stays cheap even as the OS grows.

**2. A compounding-memory engine.** Every insight domain holds three files: `knowledge.md` (stable facts), `hypotheses.md` (unconfirmed), and `rules.md` (confirmed, applied by default). A hypothesis becomes a rule after it's confirmed five times; a rule that gets contradicted drops back to a hypothesis. Your team's judgment accretes instead of evaporating.

**3. Two-sided accountability with a privacy wall.** Each person keeps a private ledger of what they owe and what they're owed, derived from their own inbox and calls. Team-relevant commitments *graduate* to a shared board, sanitized and owner-confirmed. Private stays private (a hard, structural boundary), the team still gets the visibility.

## What's inside

- **A curated set of commands** (`.claude/commands/`) for the daily loop: `/morning-briefing`, `/triage-inbox`, `/log-call`, `/sprint-board`, `/capacity`, `/whatif`, `/team-accountability`, `/roadmap-update`, `/design-review`, `/qa-check`, `/draft-reply`, and more.
- **6 skills** (five for daily work, plus `os-builder` for first-run setup) and **2 agents** for call summaries, DSU digests, voice-matched drafting, person notes, and research.
- **A compounding-memory engine** and **retention + classification rules** baked into the structure.
- **Two-sided accountability** with a graduation flow and a hard privacy wall.
- **Generated dashboards** (`views/`), like a live team-pending board.
- **The `me.local` pattern**: one shared repo, many people, each with their own private layer.

## Quickstart

Two ways in. Either way, once it's open in Claude Code, just say: **"set up my Compound OS"**. The setup runs itself, you never edit a file.

**A) Install as a plugin (no cloning)**
```
/plugin marketplace add aditya-jaiswal/compound-os
/plugin install compound-os
```
then say: **set up my Compound OS**

**B) Clone the repo**
```bash
git clone https://github.com/aditya-jaiswal/compound-os
cd compound-os
# open in Claude Code, then say: set up my Compound OS
```

Want to explore the **fictional Acme Corp demo** first? Open `views/team-pending.html` or run `/suggest-plan`, everything works out of the box. When ready, "set up my Compound OS" makes it yours (or see `docs/reset.md` / `docs/build-your-own.md` to do it by hand).

> Plugin install commands can change between Claude Code versions, verify the exact syntax in the current Claude Code docs.

## A note on the demo

This is a **generalized, open template**. It is not any real company's data. It was distilled from a production Team OS that a product team uses daily, then rebuilt from scratch as a clean-room repo with a fictional company (Acme Corp) so it leaks nothing. The `people/` domain ships empty on purpose: private notes on teammates are the one thing that never belongs in a shared repo, and the structure shows you where they live locally.

## Why it matters

Most "AI for PMs" is a chatbot you re-explain your context to every morning. Compound OS is the opposite bet: give the AI a durable, structured memory of how your team actually works, and let it compound. The result is less an assistant and more an operating system, one that answers "what's at risk, who's free, what did the customer say" in seconds, and gets better the longer it runs.

## License

MIT. Use it, fork it, make it yours.

---

<div align="center">
Built by [Aditya Jaiswal](https://github.com/aditya-jaiswal), a working product manager. If Compound OS is useful to you, a star helps others find it.
</div>
