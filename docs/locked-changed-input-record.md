# Locked Changed-Input Record

Status: **write this prediction yourself before the run**.

| Field | Record |
| --- | --- |
| Commit SHA and URL created before the run | |
| Input and units | Equity expected return, percent |
| Old value | 8.0% |
| New value | 7.0% |
| My predicted direction and decision effect | I predict that lowering Equity's expected return from 8.0% to 7.0% will make it harder to reach the 6.5% return objective. Therefore, the optimizer should use a larger allocation to Equity and smaller allocations to 10-year bonds and investment-grade bonds, which will likely increase portfolio risk. |
| Actual result | The constrained portfolio changed from 0% Bills, 20% 10-year bonds, 25% IG bonds, and 55% Equity to 0% Bills, 10% 10-year bonds, 10% IG bonds, and 80% Equity. Portfolio volatility increased. |
| Did the decision change? Why? | No. The decision remains NOT CLEARED because the tool uses synthetic teaching data and does not validate the real mandate objective, costs, or calendar-year loss process. |
