---
title: "Boring Tech Wins"
date: "2024-10-03"
categories: ["tech"]
description: "Every new framework promises to solve the same problems. Most of the time, the boring choice is the right one."
featured: false
---

Every year a new framework launches with the promise of solving the fundamental problems of software development. Every year engineers adopt it with enthusiasm. Every year the same problems resurface, just in a new form.

## The appeal of new

New technology is exciting because it represents possibility. Before you've built anything real with a new tool, you can project onto it all the things you wish your current stack could do. The ergonomics feel better because you haven't hit the edges yet.

This is mostly a cognitive trick.

## What boring tech actually means

When I say "boring tech" I mean: technology with a long track record, a large community, well-understood failure modes, and predictable performance characteristics.

Postgres is boring. Linux is boring. HTTP is boring. These things are boring because they've been run in production at massive scale for decades. Every edge case has been discovered. Every weird behavior is documented. The documentation doesn't have open issues because it was written in 2014 and still works.

## The real cost of novelty

The cost of picking a new technology is rarely the initial adoption. It's everything that comes after:

- Debugging something that has three Stack Overflow results
- Upgrading when breaking changes ship and the migration guide is incomplete
- Onboarding a new engineer who has never used the tool
- Being unable to hire because the talent pool is thin

None of these costs show up in the benchmark blog post.

## My rule of thumb

I use new technology in toy projects. I use boring technology in production. The toy projects are where I figure out if the new thing is actually better — and most of the time, it isn't, just different.

The few times I've bet on new technology in production have been expensive lessons. The many times I've bet on boring technology, I've been grateful for it.
