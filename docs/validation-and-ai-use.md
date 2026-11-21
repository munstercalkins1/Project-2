# Validation and AI-Use Record

## Baseline checks

- Weights must sum to 100%.
- Every candidate is long-only.
- A feasible mix must meet the 6.5% estimated-return proxy and 3% reserve
  minimum.
- The price parser rejects malformed rows, duplicate/missing tickers, and
  nonpositive prices.

## Changed-input record

The documented one-point equity-return stress changes the estimated equity
return from 8.0% to 7.0%. It materially changes the selected allocation. The
student must write and commit a prediction before any new changed-input run;
see `locked-changed-input-record.md`.

## AI use

AI assisted with code organization and documentation. Course inputs and any
partner observation must be verified by the student; missing evidence remains
missing rather than estimated.

## Concrete AI-output check

**Claim checked:** Lowering the Equity expected-return input from 8.0% to 7.0%
would make the 6.5% return proxy harder to reach and increase the model's
Equity allocation.

**Disposition:** Accepted after an independent arithmetic check and an app run.
The base mix has a 6.51% weighted expected return
(`0.20 × 4.3% + 0.25 × 5.0% + 0.55 × 8.0%`). After the change, the app selected
10% 10-year bonds, 10% IG bonds, and 80% Equity, with a 6.53% weighted expected
return (`0.10 × 4.3% + 0.10 × 5.0% + 0.80 × 7.0%`). The allocation becomes more
Equity-heavy and its shown volatility increases, consistent with the claim.
