# /qa-check  (QA-on-production loop)

Run a production-quality pass and route findings. Input: optional area/URL.
1. **Production QA** - pull the latest QA status (Dana's reports / `quality/qa/`), staging health, and known criticals/regressions. For UX walkthroughs, use the `ux-audit` skill (dogfood as a real user; friction, broken flows).
2. **SEO / LLM-visibility** - run `seo-llm-visibility-audit` (uses `quality/seo/`); flag drops.
3. **Triage** - rank issues (critical / high / regression); map to the release critical path if relevant.
4. **Route** - file fixes into `open-loops` (mine) / `waiting-on` (owner) + flag on `/sprint-board`; recurring quality patterns → `quality/hypotheses.md`.
5. **Log** - write the pass to `quality/qa/<date>.md`.
