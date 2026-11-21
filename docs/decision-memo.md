# Project 2 Decision Memo — Meridian Portfolio Tool

**AI-use statement:** AI assisted with code organization and documentation.
The analysis and committee decision are the student's. This is educational work,
not investment advice.

## Decision

I think we will need to reject adoption because the CPI + 4 has not actually
been proven, and there are some stress cases that activate the stop rule.

**Reject adoption of the displayed allocation as an investment recommendation.**
The tool is a transparent classroom search, not a validated investment process.
It identifies a lowest-volatility long-only five-point mix that reaches a 6.5%
estimated-return proxy and 3% reserve minimum under its stated inputs.

## Allocation range and monitoring triggers

**Allocation range now: 0% to 0%.** No allocation to this process is justified
until the committee validates market data and return assumptions, can evaluate
the CPI + 4% net-of-costs objective, documents costs and annual turnover,
completes issuer-level look-through, and defines the calendar-year-loss
measurement and breach action. These are the triggers to monitor before
considering a pilot or allocation range.

## Committee ask

Do not approve adoption, allocation, or rebalance into this process today.
Direct the portfolio owner to provide validated market data, a defensible
real-return objective analysis, transaction-cost and turnover evidence,
issuer-level look-through, and a defined calendar-year-loss process before the
committee considers a pilot.

## Conditions that would reverse the decision

Reconsider only after the portfolio owner supplies validated price data and
return assumptions, confirms the actual mandate objective, documents costs and
turnover, and defines the calendar-year loss measure and breach response.

## Stress-run stop rule

The app reruns the constrained search for a lower Equity expected return, a
36-month historical-estimation window, higher implementation costs, and a
tighter reserve floor. Stop the process and escalate to the committee when a
scenario has no feasible mix or its estimated return after the stated one-time
implementation cost falls below the 6.5% course proxy. This is a screening
rule, not proof that the Foundation can meet CPI plus 4% net of costs.

## Evidence limits

`prices.csv` is synthetic teaching data. Historical arithmetic means and
volatilities are estimates, not forecasts. The tool does not establish a
five-year CPI-plus objective, transaction-cost impact, taxes, issuer look-
through, or a loss-limit procedure.
