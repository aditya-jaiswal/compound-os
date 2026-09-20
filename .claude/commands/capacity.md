# /capacity  (run from Claude Code - needs GitHub + Calendar)

Show who's loaded, who has bandwidth, this week (or a window I give).

1. Read `delivery/capacity.md` (effective h/wk per person, TZ) and `delivery/rules.md` (velocity adjustments).
2. Pull GitHub assigned tasks for the current iteration with their estimates, per person.
3. Pull each person's calendar busy time + OOO for the window; subtract from effective hours → available hours.
4. Compute load = committed estimate (velocity-adjusted) vs available hours. Classify: 🟢 bandwidth · 🟡 full · 🔴 overloaded.
5. Render a week grid (person × day, load heatmap) to `delivery/views/capacity-week.html` and write a data snapshot `delivery/views/capacity-snapshot.json`. (Optionally push the snapshot to the Drive folder so a Cowork artifact can render it.)
6. Summary: who's overloaded, who has bandwidth, and any critical-path (alerts module) person at risk.
