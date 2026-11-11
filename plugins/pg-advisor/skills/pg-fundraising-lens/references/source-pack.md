# Source pack: fundraising lens

Essays read in full (all 20, notes included): startupfunding (2005), venturecapital (2005), vcsqueeze (2005), hiring (2005), guidetoinvestors (2007), equity (2007), googles (2008), fundraising (2008), divergence (2008), ramenprofitable (2009), future (2010), hiresfund (2010), superangels (2010), control (2010), swan (2012), invtrend (2013), herd (2013), convince (2013), fr (2013), corpdev (2015).

Ledger ids used: P1 building cheap, P2 money can't speed software, P3 few people build it, P5 near-zero marginal cost, P8 founder leverage from low capital need, P9 investors herd, P10 fund economics shape behaviour, P11 period specifics, P12 human nature, P13 arithmetic, P15 big orgs slow, P16 proxies get gamed, P20 cheap failure means more attempts.

Source note: "fr" is How to Raise Money (2013), the practical playbook. "fundraising" is A Fundraising Survival Guide (2008), the morale and survival version. Do not confuse them.

---

## 1. Principles

1. **Raise only when you can genuinely convince, not when you need money or a deadline arrives.** (convince 2013; fr 2013) Investors decide quickly whether you look like a winner, and a "no" lasts about a year. So first decide honestly whether the company is worth investing in; if you cannot convince yourself, change what you're doing rather than raise. Premature fundraising burns the reputation you will need later. Rests on: P12, P9.

2. **Either be in fundraising mode or not; never half-way.** (fr 2013; fundraising 2008; ramenprofitable 2009) Fundraising takes over the "top idea in your mind", and growth stalls. Do it hard and fast, then stop. Outside that window take money only from people who need zero convincing and accept standard paper on terms you needn't negotiate. Rests on: P12.

3. **Fundraising is a means; the real test is the company's results.** (fr 2013; guidetoinvestors 2007; fundraising 2008) Pride in a round or a valuation is like pride in grades. Priority order: get the money you need, then good investors, with valuation a distant third. Rests on: P12, P16.

4. **Treat every non-commitment as a no; only a definite, uncontingent offer is a yes.** (fr 2013; guidetoinvestors 2007; startupfunding 2005) Investors rarely say no; they drift, stay warm, and keep a free option. Founders' wishful thinking meets this halfway. Judge by actions and by the steps remaining to money wired, not by enthusiasm. Rests on: P9, P12.

5. **Run investors in parallel, weighted by expected value, and pursue alternatives until the money is in the bank.** (fr 2013; startupfunding 2005; fundraising 2008) Competition is your only leverage; serial conversations kill it and waste time. Weight each investor by chance of yes times size/quality of the yes, with extra weight on the chance of yes. Deals fall through, so keep working alternatives until cash arrives. Rests on: P9, P10.

6. **Investors are driven by other investors, so the first commitment is the hardest and the rest get easier.** (herd 2013; hiresfund 2010; guidetoinvestors 2007; fundraising 2008) Most investors are weak judges and lean on each other's opinion, so interest compounds. The best investors lean less but still feel the deadline. Don't read a stampede as proof of quality (herd 2013). Rests on: P9.

7. **Accept good-enough offers greedily and finish; do not trade a sure acceptable offer for a possible better one.** (fr 2013; fundraising 2008; guidetoinvestors 2007) Best investors reject nearly everyone, so the expected value of waiting is poor and the process itself is costly. Startups win on product, not on the funding deal. Rests on: P9, P12.

8. **Don't optimize valuation; optimize speed, then investor quality; price rarely matters.** (fr 2013; guidetoinvestors 2007; equity 2007) Valuations are artifacts of a fund's need to own a percentage and write a certain check. A high valuation narrows your exits and sets a bar for the next round. Give the first committed investor a low-enough price to start the momentum, then raise the price for later ones if demand allows. Rests on: P10, P13.

9. **Cheapness is power: spend little, reach ramen profitable if you can, and make raising money optional.** (startupfunding 2005; fundraising 2008; ramenprofitable 2009; fr 2013; divergence 2008) A startup that doesn't need the money gets better terms, looks more attractive, has better morale and doesn't stall for fundraising. "Type A" fundraising (you don't need it) is far better than "type B" (you do). Rests on: P1, P3, P8, P5 (only if per-user cost is near zero).

10. **Judge any equity trade with 1/(1 − n).** (equity 2007) Giving up n of the company is worth it only if the average outcome improves by more than 1/(1 − n). The same test applies to investors, hires and partnerships. Rests on: P13.

11. **VC economics (funds, boards, power-law returns) explain how VCs behave; plan around the structure, not the personalities.** (venturecapital 2005; guidetoinvestors 2007; swan 2012; superangels 2010) A fund must deploy large sums, so deals must be big, boards limited, and only potential huge winners matter. They are rational about the fund's portfolio but not about yours (living-dead companies get pushed to kill-or-cure). Rests on: P10, P9.

12. **Don't sell too much early, and don't raise too much.** (fr 2013; equity 2007; guidetoinvestors 2007) Keep room for a later round and for founder motivation; money raised sets spending, hiring and the valuation hurdle you must clear next time. Rests on: P13, P10.

13. **Keep control and founder alignment in view: board composition, vesting, liquidation preferences, partial founder liquidity.** (startupfunding 2005; control 2010; vcsqueeze 2005; guidetoinvestors 2007) Board control isn't total control but changes what prevails in discussions; founders' risk appetite differs from investors', and a small early cash-out can align it. Rests on: P8, P10.

14. **Don't talk to acquirers unless you want to sell now.** (corpdev 2015; googles 2008; guidetoinvestors 2007) Corp dev conversations distract, demoralize and push you to chase them. Talk only when dying or doing so well you'd happily walk away. Rests on: P12.

15. **Rejection is a question, not an answer; use the data in it, don't absorb the verdict.** (guidetoinvestors 2007; fundraising 2008; convince 2013; swan 2012) Investors are often wrong and reject for superficial reasons; the best ideas look like bad ideas. Sort rejections, extract specific reasons, fix real problems. Rests on: P9, P12.

---

## 2. Concrete tests and numbers

All numbers checked against the text.

**Equity equation (equity 2007; P13)**
- Take a trade of n of the company if outcome improves by more than 1/(1 − n).
- Half the company: outcome must more than double. YC at 7%: 1/0.93 = 1.075, so needs a >7.5% improvement. Sequoia taking about 30%: 1/0.7 = 1.43, needs >43% improvement.
- Employee: if a hire raises average outcome to i (e.g. 1.2), break-even stake n = (i − 1)/i = 16.7%.
- Converting salary to stock: multiply annual salary+overhead by about 1.5 (valuation grows ~3x a year, so a year's pay costs ~1.5 years at today's valuation). Worked example: $60k salary and overhead x 1.5 = $90k; at a $2M valuation that is 4.5%. Target "profit" of 50% on a 16.7% break-even leaves 11.1% retail; 11.1% − 4.5% = about 6.6% offer.
- Valuation base: use last round's post-money, but PG says that probably undervalues the company.
- Sequoia detail in the essay: ~6000 plans, ~20 funded, so about 1 in 300 (2007; P11 for the figures).

**Round size and amounts (fr 2013; fundraising 2008; P13 formula, P11 inputs)**
- Upper limit on raise: people to hire x $15k/month x 18 months. Example: 20 x $15k x 18 = $5.4M. $15k/month is a deliberately high all-in cost per person (benefits, office); "don't actually spend that much".
- Announce a lower target than you want (e.g. say $250k when hoping for $500k) so that $150k reads as more than half done.
- Fundraising advice for 2008: tell investors the plan works at different sizes: $50k covers food and rent for a year; a couple hundred thousand adds office and a couple of smart friends; a couple million lets you "blow this thing out" (fundraising 2008; P11).

**Dilution caps (fr 2013; P11, P13)**
- Phase 1 (seed/YC-type): sell under 15%. Phase 2: sell no more than 25% on top. Over about 40% total sold makes a Series A hard because VCs fear too little stock left to motivate founders.
- Guess conservatively about eventual valuation if on uncapped notes.
- Series A history: 30-40% sold in a series A (superangels 2010), 40% once common, VCs holding at about 20% by 2013 (invtrend 2013). Sequoia alone takes about 30% (equity 2007).
- Option pool: in a traditional series A, 10-30% pool set aside pre-money (future 2010); example round added 100 shares to the pool (startupfunding 2005).

**Valuation sanity checks**
- Next-round hurdle: a $30M post-money round requires the next pre-money to be at least $50M (fr 2013).
- Pre-money $10M means you must sell for over $50M for a 5x VC return, and VCs would rather you hold out for $100M (guidetoinvestors 2007).
- Phase 2 prices vary at most about 10x while big winners return at least 100x, so price shouldn't drive investor choice (fr 2013). Dropbox and Airbnb raised post-YC at $4M and $2.6M pre-money (fr 2013).
- Valuation changes with amount invested: $50k at a $1M valuation does not scale to $6M at that valuation (guidetoinvestors 2007).
- Angel-round example: $600k on a note capped at $4M pre = 0.6/4.6 = 13% (superangels 2010).
- Series A math example: $2M at $4M pre = one-third (2/(4+2)) (startupfunding 2005).
- Angel round example: $200k at $1M pre = 200/1200 = a sixth (startupfunding 2005).

**Deal-speed and process thresholds**
- Exploding offers: a three-working-day deadline is acceptable; shorter signals a sketchy investor (fr 2013).
- "Know where you stand": never leave a meeting without asking what happens next, what they need to decide, and how long (fr 2013).
- A hot prospect: "close now or write off" (fundraising 2008).
- Test of yes vs no: "Look down at your hands. Are you holding a termsheet?" (guidetoinvestors 2007).
- First commitment: a $50k offer from a well-known VC or angel is usually enough to start the flow; friends and family money doesn't count (fr 2013).
- Ask a VC offering a term sheet how many of their last 10 term sheets became deals (startupfunding 2005). Lower-tier break rate could be as high as 50% per a CFO quoted there (startupfunding 2005).
- Intros: ask a committed investor for two more intros (note in fr 2013, credited to Joshua Reeves). Do not ask investors who said no.
- Fundraising mode math: a YC company closing in 8 weeks after a 10-week Demo Day spent 44% of its first 18 weeks raising (guidetoinvestors 2007). Rounds take 5-6 months typically, 6 weeks is fast (guidetoinvestors 2007); about 6 weeks "can easily take" early on (invtrend 2013); about 2 months is "reasonably fast" (future 2010).
- VC funnel (David Hornik, via fundraising 2008): 500-800 plans read, 50-100 first meetings, ~20 interesting, ~5 serious, 1-2 deals per year. A partner does at most about 2 new investments a year.
- Series A: chance of rejection after the full partner meeting averages about 25%, over 50% at some firms (superangels 2010). A VC fund does about 2 series A deals per partner per year (6-year company life, ~12 boards; future 2010; superangels says ~5 years and ~10 boards).
- Stop signal: "air in the straw" when options run out (fr 2013).

**Ramen profitable (ramenprofitable 2009; fundraising 2008; divergence 2008; P1, P3)**
- Definition: revenue covers founders' living expenses. Examples in the text: $3000/month revenue; $2000/month (fundraising 2008); profitable after 2 months.
- Benefits: better terms, more attractive, morale, no fundraising interruption. Fundraising cuts productivity to "a third" of normal (ramenprofitable).
- Caveat: can be a path into consulting (ramenprofitable).

**Default alive / runway**: PG does not give a formula in these essays. The essays say only: when you have five months of runway, start looking for the next round immediately because closing always takes longer than you expect (startupfunding 2005); a startup in these essays "never spent more than half of one round before securing the next" as the ideal (startupfunding 2005). Do not attribute a default-alive calculation to this set.

**Power-law numbers (swan 2012; convince 2013; invtrend 2013; P10)**
- Two companies (Dropbox, Airbnb) were about three quarters of about $10B of YC value in 2012. 1000x variation in outcomes; 10,000x for the largest.
- Conventional wisdom: about 15 big successes a year; PG argued it could rise to 50-100 (invtrend 2013).
- If 100% of a batch raised after Demo Day, YC was being too conservative. Taking 10x the risk of Demo Day investors implies about 30% fundable. In summer 2010 it was 94% (33 of 35 that tried).
- 2013 YC numbers: 564 startups, $11.7B valuation on 287, top 10 about $8.6B (invtrend 2013). Dated (P11).

**Hiring/exit side numbers**
- Rule of thumb that employee equity falls "polynomially" with company age (startupfunding 2005).
- Consistently cited: 90% startup failure rate is "urban legend", odds probably slightly worse (hiring 2005, note 3).
- Accredited investor: net liquid assets over $1M or income over $200k (startupfunding 2005; P11).
- VC fund fees about 2% a year management fee plus about 20% of gains; about 50 of ~1000 US funds likely to make money (startupfunding 2005; P11).
- VC fund size logic: $400M across 10 partners means $40M each; hence big deals (guidetoinvestors 2007).
- Top-tier = about the top 20 firms (guidetoinvestors 2007; P11).
- Sale thresholds: some VCs demanded 4x liquidation preference, called an abuse to resist (startupfunding 2005).
- Rate of return logic: 10x in one year beats what a VC could get from a company taking 6 years to IPO, which would need 10^6 (superangels 2010).

---

## 3. Questions he would ask the founder

1. Can you tell a skeptical investor, concisely and in plain language, why this company is worth investing in, and do you actually believe it? Which of your conclusions do you really believe? (convince 2013)
2. Are you a domain expert on this market well enough to answer hard questions or to show how you'd find the answer? (convince 2013)
3. Do you need to raise, or would money merely speed you up? Would you succeed without it? Can you reach ramen profitability or profitability on what you have? (fr 2013; fundraising 2008; ramenprofitable 2009)
4. Why now? What changed that makes this idea possible and makes others not yet have done it? What is the plausible chain of hops to a big market? (convince 2013)
5. What is your plan at each funding level, including zero? Can you tell what you'd do with $50k, a few hundred thousand, a couple of million? (fr 2013; fundraising 2008)
6. If a good offer arrived tomorrow on acceptable terms, would you take it and stop? What would make you refuse? (fr 2013; fundraising 2008)
7. What exactly does each investor have to do before money is wired, and how long does each step take? What happens after the meeting? (fr 2013; fundraising 2008)
8. Is anyone's yes confirmed with a definite, uncontingent offer, or is it enthusiasm? (fr 2013; guidetoinvestors 2007)
9. How much of the company have you sold, and what will your cap table look like if the next round goes as hoped? Would you be at 40%+ sold before an A? (fr 2013)
10. If you are the person leading fundraising, who is building the product while you do it? Are you the CEO and the most formidable founder? (fr 2013; fundraising 2008)
11. What worried the investors who turned you down, and are they right? Have you sorted the rejections into specific reasons? (convince 2013; fundraising 2008; guidetoinvestors 2007)
12. Do you want to sell the company right now, not eventually? (corpdev 2015)
13. What is the upside you need to take VC money, and are you prepared for the rule that VC money blocks early sales? (guidetoinvestors 2007)
14. What would you do with the cash: more people or something you cannot do otherwise? How fast do you plan to hire? (fr 2013; fundraising 2008; vcsqueeze 2005)

---

## 4. Failure patterns he warns about

1. **Wishful-thinking pipeline.** Founder hears "we're excited" and relaxes, counts money not in the bank ("we've raised $800,000" with zero wired). (fr 2013; fundraising 2008; startupfunding 2005)
2. **Half-fundraising.** Trying to build and raise at once; the company stalls for months and looks lifeless to investors, who then cool on the founder because of their own slowness. (fr 2013; fundraising 2008; ramenprofitable 2009)
3. **Fundraising before you can convince.** Raising on a deadline or because you've run low; burns investor relationships. (convince 2013; fr 2013)
4. **Optimism about timing.** Assuming a two-week round will take two weeks; four months is normal. Deals fall through. (fundraising 2008; startupfunding 2005)
5. **Pitching rather than telling the truth.** Imitating the swagger of smooth founders; bluffing about other investors ("several are about to commit"). Uncanny valley. (convince 2013; fundraising 2008)
6. **Valuation vanity / too-high valuation.** Competing on valuation, then failing to clear the bar next round; a high valuation narrows exits; the first over-eager investor sets a price you can't sustain. (fr 2013; guidetoinvestors 2007; startupfunding 2005)
7. **Raising too much and spending it.** More people means rigidity and a worse chance of profitability; VCs push to hire aggressively because they want to sell you more equity next round. (fr 2013; venturecapital 2005)
8. **Fundraising addiction.** Good at it, enjoying the lunches, and thinking you're already successful; PG lowers his estimate for young founders who are fabulously successful at fundraising. (fr 2013)
9. **Slipping into consulting.** Consulting funds you but pulls you into service work and low-margin money, "weed tree", and excuse for failure. (startupfunding 2005; fundraising 2008; ramenprofitable 2009)
10. **Talking to corp dev too early.** The slow, demoralizing process that ends in a lowball. (corpdev 2015)
11. **Wrong ordering of investors.** Approaching "valuation-sensitive" investors first so they set a low price, or spending early time on investors who won't commit until others do (the "I don't lead" kind). (fr 2013; future 2010)
12. **Letting termsheet become "the deal".** Relaxing at the term sheet; negotiation continues to close; rivals drop away. (guidetoinvestors 2007; startupfunding 2005)
13. **Novice-angel paperwork.** 70-page agreements, cold feet, delays; or a non-accredited investor creating later securities problems. (startupfunding 2005; fundraising 2008)
14. **Ignoring anti-dilution and down-round terms because "we'll be a big hit or a bust."** (startupfunding 2005, note 10)
15. **Ignoring that investors' risk profile differs from yours.** Being pushed to turn down acquisition offers; being encouraged to roll the dice for a bigger outcome while you have no diversification. (guidetoinvestors 2007; vcsqueeze 2005)
16. **Being arrogant to investors.** Especially when doing well; the world is small. (fr 2013)

---

## 5. How his view changed over time

- **2005 (startupfunding):** Funding is a "gears" metaphor: take just enough to shift to the next gear. Describes five sources (friends and family, consulting, angels, seed firms, VCs) and a sequence seed, angel, series A. Says investors cause the worst problems ("investors have you by the balls"). Predicts founders will increasingly stay CEO and partially cash out. Treats angels as more flexible and VCs as structurally constrained, but warns that individual angels have less reputation to protect than name-brand VCs. Warns that VC-style terms (board, vesting, 4x preference) are negotiable though "standard" is claimed. Already has: don't believe it till you get the check, never stop pursuing alternatives, deals fall through, spend little.
- **2005 (venturecapital, vcsqueeze, hiring):** Explains VC behavior as an effect of fund structure (2% fee, deal size, board capacity). Predicts a squeeze: startups want less money; acquirers buy early; he said the big IPO route was damaged by Sarbanes-Oxley (his stated reason). Predicts investors' power erodes as cost falls. Advice: let founders sell some stock in a series A. These are early statements of the "cost falls, founders gain leverage" thread.
- **2007 (guidetoinvestors, equity):** Adds the "momentum investors" model (traffic, then what other investors think, then team). Still recommends taking money from a top-20 VC if you have the luxury of choosing and says it's particularly important if you're a hacker (less likely to be given a business CEO). Adds equity equation, so top-VC dilution is a bargain on paper. Still says "you need investors" empirically.
- **2008 (googles, fundraising, divergence):** Moves from "VCs are unscrupulous" (2005) to "VCs are bureaucrats, timid and conservative" (googles). Fundraising survival guide introduces low expectations, consulting as the one fallback, ramen profitable as the independence tool. Divergence argues the founder-VC bolt is loosened: funding could go from must-have to nice-to-have, in the recession. Points to the gap between $20k and $2M as an opportunity. Still says bootstrapping works rarely and consulting is the only dependable route.
- **2009 (ramenprofitable):** Names and defines the concept. Clarifies it's not a promise to never raise: few startups succeed without investment, but being less needy gets better terms.
- **2010 (future, superangels, hiresfund, control):** The advice shifts from "survive investors" to "founders are gaining power; predict the future by asking what founders would like". Super-angels, VCs doing angel rounds, rolling closes, convertible notes with different caps per investor, startup-led rounds, founders keeping board control after A rounds (a dozen YC companies). He now advises taking a Series A from a good VC over an angel round (future), while in a note he ranks good angels above a mediocre VC (note 3, future). Predicted valuation spike may not last (superangels). Notes the shift is exaggerated by a seller's market (future note 10).
- **2012 (swan):** Reframes investor behavior from the investor side: fundraising success is a misleading metric for picking winners; the big winners look like bad ideas and often struggle to raise. It's the one essay where "being fundable" is explicitly a weak signal of being great.
- **2013 (invtrend, herd, convince, fr):** Consolidates into a procedural playbook. Now: pre-A rounds usually have no "leads" and are raised one investor at a time; don't sell more than 25%; "the bar will be higher next time"; assume phase 2 is the last money you'll raise; be profitable if you can. The 2007 advice to prefer top-tier VCs becomes "get the best investors" only subordinate to "accept offers greedily". Also adds that investors who won't "lead" have zero early expected value. He also says series A rounds may be skipped (Weebly), tentatively assuming the path still goes through an A.
- **2015 (corpdev):** Adds the M&A side: do not take the first meeting. Consistent with googles (2008), which observed that startups turning down offers usually do better; in 2005 (hiring) he had expected acquisitions of early startups to accelerate, while 2015 focuses on the founder's distraction and lost leverage.

Shift in tone: 2005 "investors are a hazard to manage" leads to 2010 "investors are being forced to change because founders have power" leads to 2013 "here is a disciplined process; don't leave the path".

---

## 6. Where his advice is time-bound

Ledger status given in brackets. "PG text" = his own words; "Inference" = mine, not stated in the essays.

**P2, money can't make software get built faster [reversed for some startups]**
- PG text (hiring 2005; vcsqueeze 2005; divergence 2008): more money buys only sales and marketing, so startups need little; the stated rule is "spend little, work fast" (startupfunding 2005). Fundraising rule of $15k/person/month assumes all cost is people (fr 2013).
- Inference: for a company whose main cost is compute or model training, cost is not only people. The $15k x people x 18 months ceiling no longer sets the upper bound; model it as people plus compute/inference spend. The "don't hire too many people" and "cheapness is power" advice still applies to teams building on top of existing models, but not to those that must buy frontier compute. In such cases "raise only what you need and be profitable" becomes harder, and the investor set narrows.

**P8, founders gain leverage because startups need less capital [split]**
- PG text: future 2010 says the rule of thumb is to ask "how would founders like it to be?"; invtrend 2013 and control 2010 say founders retain more control and stock; divergence 2008 says VC could become optional; note 10 in future flags that the shift is exaggerated in a seller's market.
- Inference: the "founders hold power" prediction is a market-cycle statement as well as a structural one. For lean application companies the structural part still holds. For capital-heavy companies the opposite holds: power sits with a few very large investors, so the "accept good offers, then stop" and "keep 75%+" advice should be read as aspirations. Advice such as "founders keep board control after A" (control 2010) should be treated as market-dependent and negotiated, not assumed.

**P11, period specifics [dated]**
- PG text, but dated: Sarbanes-Oxley killing IPOs (vcsqueeze 2005); accredited investor thresholds ($1M / $200k, startupfunding 2005); super-angels as a new category (superangels 2010); convertible notes with caps as the novelty (hiresfund 2010); YC-era round sizes ($15k, $20k-50k angels, $100k super-angel check, $250-500k typical raise, $600k round at $4M cap, series A $1-5M); Sequoia 1-in-300; "about 50 of 1000 funds"; top 20 firms; 15 big hits a year; Boston investors as timid; AngelList/FundersClub/WeFunder as auxiliary; Demo Day dynamics; Weebly's skipped A; YC statistics in invtrend.
- Inference: treat all dollar figures as examples of reasoning. Seed rounds, SAFEs (not discussed in these essays), and the series A/seed boundary have shifted since. The specific instruments he recommends (uncapped note with MFN, convertible notes with different caps) are one era's tools; the reasoning (don't fix a price too early, reward early risk, avoid deadlock) transfers.

**P13, arithmetic and logic [holds; inputs change]**
- PG text: equity equation, 1.5x salary conversion (assumes valuation roughly triples per year), $15k/person/month, 18 months, 25%/15%/40% dilution limits.
- Inference: formula holds. The inputs are time-bound: the 3x/year valuation growth in equity 2007 is a boom-startup assumption; $15k is far below fully loaded cost in many hubs today; the 25%/15%/40% rule was set when a seed round was a few hundred thousand and an A was the standard next step. Rerun with current figures, and add compute cost where relevant.

**P1 and P3, building is cheap and a few people can build it [amplified]**
- PG text: ramen profitability, "cheapness is power", expensive-to-start startups put you at investors' mercy (guidetoinvestors 2007 #23); fr 2013 note 19 quotes a YC founder (not PG himself) recommending leaving capital-intensive ideas to founders with established reputations.
- Inference: strengthens the case for being default-independent and for smaller first rounds. But it also removes the "built a prototype" signal that convinced investors in 2005; a working demo (startupfunding: "spend most time on the demo") convinces less when anyone can produce one. What convinces is evidence of users and revenue, which the essays already prefer.

**P5, near-zero cost per user [weakened]**
- PG text: ramen profitable assumes $3000/month revenue covers living costs and that costs are mostly living expenses (ramenprofitable 2009; divergence 2008).
- Inference: with per-use model costs, a startup may show growing revenue and growing losses; ramen profitability needs gross margin after inference costs and a check that heavy users don't make you unprofitable. A low-revenue "we're profitable" claim is weaker evidence if pricing is subsidized.

**P10, VC fund economics shape investor behaviour [holds; numbers don't]**
- PG text: fund size forces large deals and boards; power-law returns; 2% and 20%.
- Inference: logic holds (it is why big funds want big checks and a shot at a fund-returner), but "VCs want to invest large amounts and can't do small deals" was partly overturned in his own 2010 essays by micro-VCs; funds now range widely in size and stage. Ask which type of fund you're talking to and compute what exit it needs to matter to that fund (inference).

**P9 and P12 [hold]:** The herd, don't-trust-wishful-thinking, parallel process, hear-no-until-yes, greedy-accept, be-nice advice is behavioral and carries over (ledger says so). Inference only: during an AI-hype window the stampede phenomenon is stronger and its dangers (herd demand is weakly correlated with quality; herd's withdrawal can be abrupt) are the same.

**P15, big orgs slow [split]**
- PG text: hiring 2005 and vcsqueeze 2005 argue acquirers buy early because big companies can't build; googles 2008 argues acquirers underpay and lose the best deals; corpdev 2015 treats acquirers as adversarial.
- Inference: for frontier-compute areas incumbents may out-build rather than out-buy you, and may have less need to acquire. The talk-to-corp-dev rule is behavioral and stands; the claim that acquirers will "buy early" as a general trend is time-bound.

**P16, proxies get gamed [amplified]**
- Inference: decks, demos, essays and growth screenshots are cheaper to fake or inflate. PG's statements that investors judge by traffic, then other investors, then team (guidetoinvestors 2007) imply the proxies investors lean on are exactly the ones easiest to game with AI help; verified revenue is harder to fake. Treat as inference.

**P20, cheaper failure means more attempts [amplified]**
- PG text: invtrend 2013 predicts a pyramid of many more early failures and "idea clashes".
- Inference: more simultaneous competitors make being the first to a "hot" signal less meaningful and increase the investor's problem of which one to back; raises the value of an unusual, defensible position over speed alone.

---

## 7. Limits and tensions

1. **Best investors vs greedy acceptance.** fr 2013 says "get the best investors" is a goal, but only rarely in conflict with accepting offers greedily; if conflict arises, take the sure offer because best investors reject nearly everyone. guidetoinvestors 2007 says to want top-20 VCs if you have the luxury; future 2010 prefers a series A from a good VC over an angel round; and note 3 there prefers good angels to a mediocre VC. These fit only if "acceptable" is defined, and PG never defines it.
2. **Valuation: unimportant yet carefully managed.** He says valuation is third priority and "fiction" (fr 2013; guidetoinvestors 2007), yet also warns that too-high valuation sets an impossible hurdle (fr 2013) and that lower prices are easier to raise at. The advice to give the first investor "as low a price as they need" conflicts with the earlier caution against letting an eager investor set a price you can't hold; the bridge is notes with caps or MFN, which are a technical fix that depends on the instrument.
3. **Rule-based advice vs "formidable" founders.** fr 2013 tells inexperienced founders to follow rules because their intuition is unreliable; convince 2013 says the secret is truth and formidability, and that smooth-founder tactics backfire. Both hold, but when a founder is formidable the rules (e.g. hold back price, don't name investors) get bent without cost, and PG says so in fr ("if you're a wizard"; "experienced at negotiations"). No test for which founder you are: "if you're not sure, you're not" (herd 2013).
4. **Exaggerated versus honest competition.** herd 2013 says it's safe to tell investor A you're far along with B if true, but never name B. convince 2013 calls the "several about to commit" bluff arguably permissible but advises against. fundraising 2008 calls the optimal answer to "who else?" a skilled implication, but advises not to try unless good. The ethical line is soft.
5. **Consulting.** startupfunding 2005 says consulting is a plan for founders with kids and the only route that takes the risk out; fundraising 2008 calls it the only dependable route and a fallback; ramenprofitable 2009 warns of sliding into it; a VC quoted in fundraising 2008 note 3 avoids consulting-bootstrapped companies because it builds bad habits. Tension between consulting as bridge and as trap is left to judgment.
6. **"Bootstrapping rarely works" versus "be profitable".** fundraising 2008 says bootstrapping is rare and famous cases are survivors; ramenprofitable 2009 and divergence 2008 say profitability on small revenue makes investors optional; fr 2013 says type A fundraising is "so much better" and suggests founders should avoid up-front capital-intensive ideas. These are reconciled by "ramen profitable doesn't mean never raise", but PG never gives a rule for when to raise at all if you are profitable beyond "growth faster than revenues allow" (fr 2013).
7. **Predictions that were wrong or mixed (his flagged uncertainty).** future 2010 note 10 admits the founder-power shift is exaggerated by a seller's market; superangels 2010 says "no one knows" what top-VC advice is worth versus super-angel money; invtrend 2013 says the VC response is "hell if I know". He predicted founders partially cashing out and boards: partly happened. Treat prediction passages as hypotheses.
8. **Selection bias in YC evidence.** His fundraising advice comes from YC companies who get demo-day access, brand halo and a batch of investors at once (fr 2013: "this essay is the advice we give them"). Several pieces of advice (breadth-first search, "Demo Day approaches an auction", fundraising 2008) assume many investors available at the same time. An outside founder with few intros lacks that structure; he does recommend self-sourced intros (fr 2013) but offers little for founders without a network. Inference: weaker generalization to founders outside YC-like channels.
9. **Fundraising success as signal.** swan 2012 shows fundraising success is uncorrelated or inversely correlated with big wins at YC; yet fr 2013 and convince 2013 tell founders to raise only when they can convince investors, and rely on investor confidence as a gate. Reconciled by distinction between "worth funding by an investor like us" and "can an average Demo Day investor be convinced", but a founder with an unusual idea gets two opposite messages (flagged in convince 2013: Dropbox rejected by Boston; Airbnb).
10. **Scope: only cheap software startups.** He addresses only startups that need small sums. future 2010 note 1 and invtrend 2013 limit scope to software; biotech, energy and hardware are explicitly outside the rules (ramenprofitable 2009: "not feasible" for most biotech). Anything capital-heavy needs different advice, not covered here.
11. **Thin evidence.** Several claims rest on a few anecdotes or a handful of YC alumni: "a dozen" companies with board control after A (control 2010); "no deal that began with an associate cold email" (fr 2013, note 5: "I don't know of a single"); two-firm deals (one founder quote); 44% of first 18 weeks (one stylized example); "best VCs are the least VC-like" (fundraising 2008 note 7); his own mix of "VCs are jerks because of fund structure" (venturecapital 2005), later softened to bureaucrats (googles 2008). Treat these as heuristics from one vantage point.
12. **PG's role as investor.** He writes as a seed investor with a portfolio view (swan 2012: only one company per batch matters financially). Advice such as "take 10x the risk", "who cares what investors think" (swan) fits his incentives, not a single founder's; guidetoinvestors 2007 #18 and vcsqueeze 2005 acknowledge that founders and investors have different risk preferences. A founder with one company should weigh that gap, including when deciding whether to take a hits-driven investor's money (inference built on his own text).
