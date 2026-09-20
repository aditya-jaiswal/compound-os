---
name: email-voice
description: Write emails in the current user's voice for replies and drafts. Use whenever drafting an email from this OS.
---

# Email Voice

**Whose voice: the current user's.** Resolve their name, role and email from `me.local.md` first - never assume, never default to any teammate. If they have a personal voice guide (`<private_root>/voice/email.md` or `personal-brand/voice/guide.md`), it overrides the house defaults below.

House defaults (until a personal guide exists):

Tone: clear, concise, warm-professional, direct. Lead with the answer/ask. No filler.

Structure: brief greeting → the point → any specifics (tight) → clear next step.

Signature (from `me.local.md`):
```
Best Regards,
<name>
<role> | your company
```

Rules:
- Match the recipient: crisper for the boss (your boss), relationship-aware for customers, supportive+specific for teammates.
- Never invent commitments, dates, or data - if unknown, leave a [bracket] for the user to fill.
- Customer emails: no internal-only details; mind confidentiality.
- Always produce a DRAFT for the user's review; never auto-send.

- **No em dashes (-) ever.** Use commas, periods, or parentheses; "to" for ranges. This is a hard rule.

- **Reply-all by default.** Keep everyone who was on the thread: To = sender + original To, Cc = original Cc, minus the current user's own address. Do not drop recipients.
