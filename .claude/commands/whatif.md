# /whatif  (run from Claude Code - needs GitHub + Calendar)

Model an ad-hoc task (or several) before committing. Input: task(s) with rough estimate + candidate owner(s).

1. Load current capacity (as in /capacity).
2. For each candidate owner, add the new estimate → recompute load. If it pushes them over available hours, compute the overflow and which of their existing tasks slip (lowest priority first).
3. **Timeline impact:** if the task or the displaced work is on the alerts module critical path, compute how June 30 moves. If not, show the local slip only.
4. **Bandwidth routing:** rank who can absorb it with least disruption (most 🟢 bandwidth, right skills/TZ).
5. Output: per-owner before/after load, timeline delta, and a recommendation. Nothing is written to GitHub unless I approve creating the task.
