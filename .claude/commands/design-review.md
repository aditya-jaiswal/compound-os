# /design-review  (the designer-call workflow)

Run the design sync end-to-end: vision → review → similar products → validate need → align → prioritize. Input: Figma link / screenshots / the design topic.

1. **Ground in vision** - read `design/vision.md` + `product/product-context/*` (positioning, unified-UI/friction goals).
2. **Critique the design** - use the `design:design-critique` skill (usability, hierarchy, consistency); `design:accessibility-review` if it's near handoff.
3. **Find similar products** - web-research how others solve this (what "good" looks like); cross-ref `competitive/`.
4. **Validate the need** - check it against real demand in `customers/accounts/*` + `product/roadmap/gtm-feedback-themes.md`. Is a customer actually asking? How many?
5. **Vision alignment** - does it serve the positioning + the unified-UI/friction thesis? Flag drift.
6. **Prioritize** - if validated + aligned, add to `product/roadmap/roadmap.md` (Now/Next/Later) and propose tickets (review → create).
7. **Log** - write the decision to `design/reviews/<date>-<topic>.md`; capture design insights to `design/hypotheses.md`; update the designer's people-note with signal.

Skills: `design:design-critique`, `design:ux-journey-architect`, `design:research-synthesis`, `design:accessibility-review`.
