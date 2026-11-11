---
name: pg-survival-lens
description: Paul Graham's survival and growth reasoning (default alive or dead, the fatal pinch, ramen profitability, growth rate as compass, hiring too fast, persistence versus obstinacy), with a time check for post-AI conditions. Use whenever a founder is weighing runway, burn, whether to hire, cutting costs, a flat growth curve, whether to pivot or keep going, or whether they're about to run out of money, even if they don't mention Graham. Part of the pg-advisor set.
---

# Survival lens

Will this company survive long enough to work, and is it growing fast enough to matter? Graham's answer is a sequence of hard questions founders tend to avoid. The arithmetic behind them is timeless; some of the inputs and cost assumptions are not.

If you haven't already, read the pg-advisor `SKILL.md` (at `../pg-advisor/SKILL.md` relative to this skill's base directory) for the answer format, time check and citation rules. The full source material, with every number checked against the essays, is in `references/source-pack.md`; read it when you need a specific number, quote location or tension.

## Work through these in order

### 1. Default alive or default dead?

The first question for any company older than about 8–9 months (Default Alive or Default Dead?, 2015): if expenses stay flat and revenue keeps growing at its recent rate, does the company reach profitability before the money runs out?

Run the calculator (in this skill's `scripts/` folder) rather than estimating in your head. It also tells you the growth rate or cost level that would make the company alive:

```bash
python3 -I scripts/default_alive.py \
  --cash 900000 --expenses 140000 --revenue 40000 --growth 0.04 [--variable-cost-share 0.3]
```

**Time check (P5, weakened):** Graham's test assumes costs stay flat while revenue grows. That was close to true for classic software. For AI products, every use costs compute, so set `--variable-cost-share` to the share of revenue that goes to usage-driven costs. If the founder doesn't know it, that is the first thing to find out. Say that this adjustment is the advisor's, not Graham's.

### 2. If default dead: is this the fatal pinch?

Heavy burn, mediocre growth, a few months of cash, and a plan to raise more (The Fatal Pinch, 2014). Graham's stark advice: assume the chance of raising is zero and fix it from inside, by cutting cost (in practice, people) or making money quickly, including bounded consulting-style work. Shut down only if certain it will fail whatever you do. Investor herd behaviour (P9) still holds, so this advice still holds.

### 3. Should they hire?

Hiring too fast is, in Graham's words, by far the biggest killer of startups that raise money (2015). Big staffs are mostly an effect of growth, not a cause. Hire only people who write code or get users (2006).

**Time check (P3, amplified):** small teams with AI tools now do what needed several engineers. The case against hiring early is stronger than when he wrote it. Ask what the founders could do with AI tools before adding headcount.

### 4. What is the growth rate, and is it enough?

A startup is a company designed to grow fast, and the weekly growth rate is the compass (Startup = Growth, 2012). It must be a rate, not a count. His YC-era benchmarks were 5–7% a week good, 10% exceptional, 1% a sign you haven't figured it out. Use `--weekly` on the calculator to convert.

**Time check (P11, P6):** those benchmarks came from YC batches in the early 2010s. Treat them as rough markers, not targets. With distribution harder (P6 weakened) and copies appearing faster (P20 amplified), fast growth is still the signal, but ask what keeps the growth once competitors arrive. Graham's own 2026 essay (How to Earn a Billion Dollars) uses 15% a month as a strong-but-not-rare rate.

### 5. Is there a small group who love it?

Better a few users who love you than many who are lukewarm (13 Sentences, 2009; How Not to Die, 2007). Growth starts with doing things that don't scale: recruiting users by hand and delighting them (Do Things That Don't Scale, 2013). This rests on users deciding (P22, holds), and with distribution harder it applies with more force.

### 6. Keep going or change course?

Startups mostly die because founders give up (How Not to Die, 2007). But persistence means attachment to the goal, not to the first plan. His 2024 test (The Right Kind of Stubborn): do you get more engaged when someone points out a flaw? A pivot that reuses most of what was built, toward something users are excited about, is a good sign. Restarting from scratch each time is a bad one (2006).

Watch for the euphemisms for quitting: "we'll keep working on it, but…" alongside grad school, consulting or a side project (2007).

A pivot "to AI" because AI is fashionable is not an idea. Hand it to the idea lens.

## Tensions to be honest about

- **Survive versus grow.** Graham says be cheap and grow fast, and claims spending and growth are barely related. That is asserted more than shown.
- **"Don't give up" has survivorship bias.** He offers no stopping rule beyond shutting down if certain of failure.
- **Raise generously, but spend as though there's no more.** His 2006 and 2014–15 advice only reconciles this way, and he never says it outright.
- **Everything assumes the goal is a fast-growing startup.** He says little about a profitable business growing slowly.

When one of these bears on the decision, name it in the answer's limits section.
