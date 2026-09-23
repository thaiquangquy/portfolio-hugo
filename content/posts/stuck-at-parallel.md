---
title: "Stuck at Parallel"
date: "2026-09-23"
categories: ["tech"]
tags: ["engineering", "ai", "reflection"]
description: "I've settled into running several AI agents at once. The next step means letting go of something I'm not sure I'm ready to let go of."
featured: false
---

Someone at work drew this maturity curve on a whiteboard a few months back: gated, assisted, parallel, supervised, AI-native. Cute framing. I laughed at "AI-native" because it sounded like a LinkedIn post. Then I actually looked at where I sit on it and stopped laughing.

Parallel. Third box from the left. I've been sitting there since maybe June.

## What Parallel actually feels like

Nobody warns you that "parallel" mostly means more browser tabs. Right now I've got six worktrees open — `feat/rate-limit`, `fix/flaky-webhook-test`, four others I'd have to alt-tab to name — each running its own agent, each waiting on me for something. My job title didn't change but the job did. I used to produce the diff. Now I referee five diffs I didn't write and one I'm too tired to remember starting.

Is that less work? On paper, sure. In practice I closed my laptop last Thursday more drained than I've been in a year, and it wasn't from typing.

To be fair, a chunk of the grunt review is gone. CI catches the obvious stuff. Our security scanner flagged a leaked test credential last week before I'd even opened the PR. Great. But "caught most of it" and "caught all of it" are different sentences, and I live in the space between them more hours a day than I'd like to admit.

## Why step 3 isn't just "step 2 but more"

Here's the part that actually unsettles me. Supervised autonomy isn't parallel with extra agents bolted on — it's a different question entirely. Right now I ask "is this diff correct?" At the next stage the question is supposed to become "what did I forget to tell it?" Trusting the output by default, and only stepping in upstream, before the run, not downstream after.

I say that sentence to myself and then, an hour later, catch myself re-opening a diff that already passed three checks. Not because anything's wrong with it. Because checking is the muscle I've spent years building, and I don't fully trust that a different muscle will hold my weight yet.

## Where I actually am, plainly

I'm comfortable at parallel. Uncomfortably comfortable, if that makes sense — the guardrails for the next stage are sitting right there, built, tested, ready, and I keep finding reasons to open one more diff instead of trusting the pipeline that already vetted it. That's not a tooling gap. That's just me.

If I'm honest about what actually moves the needle, it's not reviewing more carefully. It's spending less time re-checking work a scanner already vouched for and more time upstream, in the brief, in the context I hand the thing before it starts — because that's where the real failures are hiding, not in the diff itself.

---

No neat wrap-up here — I haven't made the jump yet. Mostly writing this down so six-months-from-now me can check whether I actually moved, or just got better at describing the box I'm stuck in.
