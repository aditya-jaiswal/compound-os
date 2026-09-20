# /suggest-plan  (the evergrowing planning engine)

Propose a prioritized backlog / next-month plan / product improvements by synthesizing every signal in the OS. Output is a DRAFT proposal for review (never auto-commits to the roadmap or GitHub).

## Signals to read (weight by convergence)
- **Customer needs:** `customers/accounts/*` (open asks, feedback), feedback frequency across accounts, and `product/roadmap/roadmap.md`.
- **Product vision:** `product/product-context/*` (overview, positioning), `product/roadmap/roadmap.md`.
- **Platform QA / reliability:** `quality/*` (QA findings, SEO), staging-fragility + bug signals from `team/` + DSU digests.
- **Competitive:** `competitive/competitors/*` (white space = moat opportunities; frontier threats), the registry.
- **Ad-hoc + in-flight:** `open-loops.md`, `waiting-on.md`, `delivery/sprints/current/*`.
- **Compounding memory:** promoted `rules.md` across domains (confirmed patterns outrank one-off requests).

## Method
1. Cluster signals into candidate themes/initiatives.
2. Score each by: customer demand (# accounts), vision-fit, competitive leverage (white space > parity), QA/risk urgency, effort, and dependency on the current release.
3. Rank; mark each as Now / Next / Later. Note which are product improvements vs new bets vs reliability.
4. For the top items, write a one-paragraph rationale citing the signals, a rough size, and a suggested owner/quarter.
5. Output `product/roadmap/backlog-proposal-<date>.md` (proposal) + surface the top 5 + what changed since the last proposal. Offer to turn approved items into `/day-plan` + proposed GitHub tickets.

## Cadence
Run monthly (next-month plan) or on demand (after a big customer call, a competitor move, a QA spike). It compounds: as hypotheses promote to rules, suggestions get sharper. Good candidate for a monthly scheduled task.
