---
name: pg-fundraising-lens
description: Paul Graham's fundraising reasoning (whether to raise at all, how much, ramen profitability as leverage, the equity test, treating anything short of yes as no, investor herd behaviour, running a raise in parallel, valuation, corp dev), with a time check that splits lean AI-app startups from capital-heavy ones. Use whenever a founder is deciding whether or how much to raise, weighing a term sheet or valuation, running or rescuing a stalled raise, or talking to acquirers, even if they don't mention Graham. Part of the pg-advisor set.
---

# Fundraising lens

Should this company raise, how much, and how should it run the process? Graham's tactics rest on investor psychology, which hasn't changed. His answer to how much rests on what money can buy, which has changed and now splits by type of company.

If you haven't already, read the pg-advisor `SKILL.md` (at `../pg-advisor/SKILL.md` relative to this skill's base directory) for the answer format, time check and citation rules. Full source material, with numbers checked against the essays, is in `references/source-pack.md`. Note: `fr` is How to Raise Money (2013), the playbook. `fundraising` is A Fundraising Survival Guide (2008). Don't confuse them.

Most raise decisions also need the survival lens. Is the company default alive? That decides whether a raise is optional or urgent.

## First: which kind of company is this?

This is the split that decides how much of Graham's sizing advice transfers (see the pg-advisor skill's `references/assumptions.md`, P2 and P8):

- **Lean (builds on existing models or ordinary software).** Graham's core logic applies with more force. Extra money mostly can't make the product get built faster, small teams with AI tools go further (P1, P3 amplified), and the founder's leverage over investors is high. But check gross margin after compute costs (P5 weakened).
- **Capital-heavy (trains models, buys large amounts of compute, hardware, biotech).** Graham's raise-little logic doesn't transfer. He assumed extra money mostly bought marketing (Hiring is Obsolete, 2005). He noted that ramen profitability isn't feasible for most biotech startups (2009), and in a 2013 footnote he passed on a YC founder's advice to leave capital-intensive ideas to founders with established reputations. That is the founder's line, not Graham's own rule, so cite it that way. Here money buys speed (P2 reversed), and a few large investors hold the power (P8 split). What still transfers: start with a cheaper subset and expand as you raise more (A Guide to Investors, 2007), plus all the process advice below.

## Work through these

### 1. Do they need to raise at all?

Graham's strongest lever is not needing the money. Ramen profitability, where revenue covers the founders' living costs (2009), means better terms, more attractive to investors, better morale, and no months lost to fundraising. A raise you don't need is far better than one you do (2013).

**Time check (P5):** for an AI product, compare revenue against living costs plus compute and other usage costs, not living costs alone. Ramen profitability on subsidised pricing isn't the real thing.

### 2. If raising, how much?

His 2013 ceiling: the number of people you'd hire × about $15k a month all-in × 18 months. He meant it as a deliberately high upper bound. Take generously, but act as if it's the last money you'll get (2006, 2014). Raise enough to reach the next visible milestone.

**Time check:** keep the shape of the formula and replace the inputs. Lean: probably fewer people than he'd assume, because AI tools do part of the work (P3). Capital-heavy: add compute, model training and inference to the people cost; people are no longer most of the spend (P2). His dollar figures and round sizes are from a 2005–2013 market (P11), so don't quote them as current.

### 3. Is the deal worth the dilution?

The equity test (The Equity Equation, 2007): giving up a fraction n of the company is worth it only if it improves the expected outcome by more than 1/(1 − n). Selling 20% needs at least a 1.25× improvement. Compute it for the actual offer. This is arithmetic and holds (P13).

His 2013 guidance on how much to sell: under 15% in the first phase, no more than 25% more on top, and over about 40% total sold makes later rounds hard. **Time check:** the logic holds (keep founders motivated and leave room for later rounds), but the specific limits were set in the 2013 market (P11). Present them as his rule of thumb from that time.

### 4. Running the raise

These rest on investor herd behaviour and human nature (P9, P12: holds), so apply them as he gave them (How to Raise Money, 2013, unless noted):

- Raise only when you can genuinely convince someone. Be fully in fundraising mode or not at all. Fundraising takes over your thinking, and growth stalls while it does.
- Treat anything short of a definite offer as a no. Enthusiasm, "keep us posted" and "love to see more traction" are not yes.
- Talk to investors in parallel, weighted by how likely each is to say yes.
- Investors follow other investors (2013), so the first commitment is the hardest. Make it easy to say yes early.
- Accept good-enough offers greedily, then stop and get back to work.
- Valuation comes a distant third, after getting the money and getting good investors. Too high a valuation sets a bar the next round must clear.
- An offer with a deadline of three working days is acceptable. A shorter one is a warning sign.
- Don't talk to corporate development teams unless you want to sell now (2015).

**Time check (P9 amplified in hype cycles, judgement):** during AI hype, herd behaviour is if anything stronger. A stampede of interest says little about quality and can reverse just as fast.

### 5. If the raise has stalled

Combine with the survival lens. Graham's advice (2013, 2014): set a deadline, stop fundraising if it isn't working, and make the company not need the money by cutting costs or making money. A long run of "maybe" means no.

## Tensions to be honest about

- **His position.** He writes as an investor with a portfolio. Swinging for a huge outcome suits his incentives more than a single founder's, which he acknowledges in 2007 and 2012.
- **His sample.** The advice comes from YC companies with Demo Day and a batch of investors all at once. Founders without that network have less leverage than the process assumes.
- **Valuation.** He calls it unimportant, yet also warns about valuations that are too high. The two only reconcile if you take an acceptable price fast and avoid one you can't grow into.
- **Scope.** The advice was written for cheap software startups. He says so in passing (ramen profitability isn't feasible for most biotech, 2009) rather than as a formal limit. Anything capital-heavy needs the adjustments above, and beyond those he isn't a guide.
