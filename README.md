# PG Advisor

A startup decision advisor for Claude, grounded in Paul Graham's essays and checked against today.

Describe a decision you're facing ("should we take this seed offer?", "should we hire three engineers?", "is this idea any good?") and the advisor:

- recommends what to do, using the two to four arguments from Graham's essays that bear most on it, each cited by title and year;
- says whether each argument **still holds**, **applies with more force** or **has changed** since he wrote it, especially since AI, and whether that verdict is Graham's own or the advisor's judgement;
- runs the numbers on your situation (for example a default-alive calculation);
- gives you the cheapest test you could run this week;
- names where Graham isn't a good guide for your decision.

It covers three kinds of decision: whether an idea is worth pursuing, whether the company will survive (runway, hiring, pivots), and fundraising.

**Not affiliated with or endorsed by Paul Graham.** The essays are his and are not included here. See [What's included](#whats-included).

## Install

### Claude Code

```
/plugin marketplace add MattVOLTA/pg-advisor
/plugin install pg-advisor@pg-advisor
```

Then start a new session and run `/pg-advisor` with your decision, or just describe it.

### claude.ai

Download [`dist/pg-advisor.zip`](dist/pg-advisor.zip) and upload it under **Settings → Capabilities → Skills**. This version merges the advisor and its three lenses into one skill.

### Optional: a local copy of the essays

The advisor reads the two to four essays it cites from paulgraham.com and caches them on your machine. To download all of them up front (a few minutes, for faster and offline use):

```
python3 plugins/pg-advisor/skills/pg-advisor/scripts/essays.py fetch-all
```

Essays are cached in `~/.pg-advisor/essays`, or in `$PG_ESSAYS_DIR` if you set it.

## What's included

| | |
|---|---|
| `pg-advisor` | The router: pins down the decision, picks lenses, runs the time check, checks citations, writes the answer. |
| `pg-idea-lens` | Is the idea good, and what would make the company hard to beat? |
| `pg-survival-lens` | Default alive or dead, the fatal pinch, hiring, growth rate, pivot or persist. Includes a runway calculator. |
| `pg-fundraising-lens` | Whether to raise, how much, the equity test, running or rescuing a raise. Splits lean AI-app startups from capital-heavy ones. |
| `references/assumptions.md` | The 22 assumptions behind Graham's advice, with their status today. **This is the part that goes stale.** It is dated, and is reviewed quarterly. |
| `references/knowledge/` | An index of all 235 essays with links, plus paraphrased summaries, key ideas and 1,215 claims tagged by the assumption each rests on. |

Everything here is paraphrase and analysis. Graham's essay text is fetched from [paulgraham.com](https://paulgraham.com/articles.html) by each user, never redistributed.

## How much to trust it

- In testing on 10 founder scenarios, answers with the advisor passed all 8 checks, against about half without it. The bigger difference: answers without it got Graham's views wrong twice, and answers with it made no errors across about 25 claims checked against the essays. The scenarios are in [`tests/scenarios.json`](tests/scenarios.json).
- Whether each assumption has changed is mostly the author's judgement, not market data. The advisor labels it that way in every answer.
- Graham wrote mostly about cheap software startups, from an investor's seat, with Y Combinator's sample. The advisor says so where it matters.

## Licence

The skills, scripts and analysis are MIT licensed (see [LICENSE](LICENSE)). Paul Graham's essays remain his copyright and are not part of this package.
