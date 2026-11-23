# Visible Baseline Output

## Material inputs and as-of boundary

- **Mandate objective:** CPI + 4% net of costs over rolling five-year periods.
- **Teaching-model proxy:** 6.5% annual expected return.
- **Reserve floor:** 3% in Bills or 10-year government bonds.
- **Return inputs:** Bills 3.0%, 10-year bonds 4.3%, IG bonds 5.0%, Equity 8.0%.
- **Portfolio rules:** long-only, five-percentage-point weights, annual review,
  and committee approval when turnover exceeds 25%.
- **Teaching-data boundary:** `prices.csv` contains synthetic monthly closes from
  2021-10-31 through 2026-10-31. The annual point-in-time signal uses data only
  through 2025-12-31 for the 2026 rebalance decision.

## Baseline output

The constrained search selects **0% Bills, 20% 10-year bonds, 25% IG bonds,
and 55% Equity**. It has a **6.51%** estimated return, **9.44%** estimated
volatility, and **20%** reserve-eligible weight.

The equal-weight and 60/40 baselines appear beside this portfolio in the app,
each with a visible mandate verdict.

## Committee decision

**Reject adoption; allocation range now: 0% to 0%.** The mix clears the
classroom model proxy and checkable reserve rule, but synthetic teaching inputs
do not establish a credible CPI + 4% net-of-costs path. The app also identifies
cost and other stress scenarios that trigger the process-stop rule. Reconsider
only after the committee validates data, costs, issuer look-through, and the
calendar-year loss definition.
