# /gap-check  (run from Claude Code - needs GitHub)

Make sure the June 30 release plan is fully represented as GitHub tasks, so we don't miss deadlines from untracked work.

1. Read `delivery/sprints/current/release-plan-june-30.md` (every Week 1/2/3 deliverable).
2. Pull the GitHub Project (issues/items, status, assignee, estimate, iteration/due) for the relevant repo/project.
3. Diff:
   - **Missing:** release-plan items with NO matching GitHub task → list them.
   - **Incomplete:** GitHub tasks missing an owner, an estimate, or an iteration/due date → list them.
   - **Orphan:** GitHub tasks in this iteration not tied to any release-plan item → list (scope creep check).
4. Map each item to its week + the alerts module critical-path dependency.
5. Write `delivery/sprints/current/coverage.md` (the diff) and surface the top gaps. Offer to create the missing GitHub issues (with owner/estimate/iteration) on approval - never auto-create silently.
