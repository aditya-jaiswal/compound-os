# Personal vs Team - classification rule (baked)
> Applied when deciding whether an extracted action item stays in a private ledger or graduates to the shared board. Default when unsure: PERSONAL.

## TEAM (graduates to the shared board)
An item is team if ANY is true: it comes from a common call (standup, design, architecture, customer); it is customer-related; it is on the GitHub board; or it comes from a multi-person thread.

## PERSONAL (stays private, never published)
Only if ALL are true: it is a 1:1 DM or a solo-addressed email, AND it is not customer-related. Anything sensitive (HR, hiring, personnel) stays personal regardless.

## Kind (page vs ticket)
`task` = real tracked work, mirrors to a GitHub issue. `follow-up` = lightweight loop (an email reply, a doc to send, a ping), lives on the board/page only, never a ticket. Default when unsure: follow-up.
