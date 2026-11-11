#!/usr/bin/env python3
"""Default-alive check, after Paul Graham's "Default Alive or Default Dead?" (2015).

Assumes fixed costs stay flat and revenue keeps growing at its recent monthly
rate. Optionally models costs that scale with usage (e.g. AI compute), which
Graham's original test assumed away.

Usage:
  default_alive.py --cash 900000 --expenses 140000 --revenue 40000 --growth 0.04
  default_alive.py ... --variable-cost-share 0.3   # 30% of revenue goes to per-use costs
  default_alive.py --weekly 0.05                   # convert a weekly rate
"""
import argparse


def run(cash, expenses, revenue, growth, var_share, horizon=120):
    month = 0
    while month < horizon:
        variable = revenue * var_share
        net = revenue - expenses - variable
        if net >= 0:
            return month, cash, revenue, True
        cash += net
        if cash < 0:
            return month, cash, revenue, False
        revenue *= 1 + growth
        month += 1
    return month, cash, revenue, None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cash", type=float)
    p.add_argument("--expenses", type=float, help="monthly fixed expenses (people, rent, tools)")
    p.add_argument("--revenue", type=float, help="current monthly revenue")
    p.add_argument("--growth", type=float, help="monthly revenue growth rate, e.g. 0.04")
    p.add_argument("--variable-cost-share", type=float, default=0.0,
                   help="share of revenue spent on costs that scale with usage, e.g. 0.3")
    p.add_argument("--weekly", type=float, help="convert a weekly growth rate to monthly and yearly")
    a = p.parse_args()

    if a.weekly is not None:
        m = (1 + a.weekly) ** (52 / 12) - 1
        y = (1 + a.weekly) ** 52
        print(f"{a.weekly:.1%} weekly = {m:.1%} monthly = {y:.1f}x a year")
        if a.cash is None:
            return

    month, cash, rev, alive = run(a.cash, a.expenses, a.revenue, a.growth, a.variable_cost_share)
    burn = a.expenses + a.revenue * a.variable_cost_share - a.revenue
    print(f"Net burn now: {burn:,.0f}/month; simple runway: {a.cash / burn:.1f} months" if burn > 0 else "Already profitable at current numbers.")
    if alive is True:
        print(f"DEFAULT ALIVE: profitable in month {month}, with {cash:,.0f} cash left (revenue then {rev:,.0f}/month).")
    elif alive is False:
        need = a.expenses / (1 - a.variable_cost_share) if a.variable_cost_share < 1 else float("inf")
        print(f"DEFAULT DEAD: cash runs out in month {month}; revenue would then be {rev:,.0f}/month against {need:,.0f}/month needed to break even.")
        # growth rate that would make it alive
        lo, hi = a.growth, 2.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if run(a.cash, a.expenses, a.revenue, mid, a.variable_cost_share)[3]:
                hi = mid
            else:
                lo = mid
        print(f"Monthly growth needed to be default alive with these costs: about {hi:.1%}.")
        # expense level that would make it alive at current growth
        lo, hi = 0.0, a.expenses
        for _ in range(60):
            mid = (lo + hi) / 2
            if run(a.cash, mid, a.revenue, a.growth, a.variable_cost_share)[3]:
                lo = mid
            else:
                hi = mid
        print(f"Or: cut fixed expenses to about {lo:,.0f}/month (from {a.expenses:,.0f}) at the current growth rate.")
    else:
        print("Not profitable within 10 years at these numbers.")


if __name__ == "__main__":
    main()
