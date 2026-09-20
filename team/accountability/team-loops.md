# Team Loops - shared accountability ledger (demo: Acme Corp)
> Owner-confirmed list of what's pending teamwide and under whom. `views/team-pending.html` is generated from this table.

## How to read
- Kind: task (mirrors to a GitHub issue) or follow-up (page only)
- Status: open | in-progress | blocked | done
- Source: standup | design | arch | customer | board | thread

## Team loops
| ID | Owner | Item | Source | Kind | Status | Since | Due | Notes |
|----|-------|------|--------|------|--------|-------|-----|-------|
| TL-001 | Sam Chen | Ship smart-alerts backend (thresholds + anomaly) | arch | task | in-progress | 2026-09-02 | 2026-09-12 | Q4 launch must-land |
| TL-002 | Priya Nair | Alerts config UI + empty states | design | task | in-progress | 2026-09-03 | 2026-09-11 | Consumes design system |
| TL-003 | Alex Kim | AQL query parser v1 | arch | task | open | 2026-09-04 | 2026-09-18 | Natural-language query layer |
| TL-004 | Dana Osei | Staging stabilization + regression suite | arch | task | blocked | 2026-09-01 | 2026-09-15 | Blocks integration testing |
| TL-005 | Jordan Rivera | Globex: send pilot recap + success criteria | customer | follow-up | open | 2026-09-08 | 2026-09-11 | Post-demo |
| TL-006 | Jordan Rivera | Put all Q4-launch workstreams on the board | standup | task | open | 2026-09-08 | 2026-09-10 | Only backend is tracked |
| TL-007 | Taylor Vance | Initech: send saved-views proposal | customer | follow-up | open | 2026-09-07 | 2026-09-12 | Renewal lever |
| TL-008 | Robin Park | Anomaly model eval + thresholds tuning | arch | task | in-progress | 2026-09-05 | 2026-09-16 | Feeds TL-001 |
| TL-009 | Noah Berg | Saved-views API + sharing | arch | task | open | 2026-09-06 | 2026-09-20 | Next after alerts |
| TL-010 | Jordan Rivera | Reconcile roadmap after Globex feedback | board | follow-up | open | 2026-09-09 | 2026-09-11 | Move fleet-alerts up |
