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
