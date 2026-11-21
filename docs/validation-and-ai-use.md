# Validation and AI-Use Record

**AI-use statement:** AI assisted with code organization, test setup, and
documentation formatting. The analysis and committee decision are the student's.
This is educational work, not investment advice.

## Sources and as-of boundary

- `prices.csv` is synthetic classroom data, not a market-data source.
- The file covers monthly observations from 2021-10-31 through 2026-10-31.
- The point-in-time VTI trend signal uses only data through 2025-12-31 and may
  affect only the following annual rebalance.
- Annual return, volatility, and correlation estimates derived from these inputs
  are teaching estimates, not forecasts.

## Tests and results

- **Portfolio invariants:** all candidates sum to 100% and are long-only.
- **Constraint screen:** the app checks reserve eligibility, daily liquidity,
  and visible monitor items for issuer look-through, turnover, and the undefined
  calendar-year-loss rule.
- **Known mandate cases:** `mandate.py` produced the Lab 13 expected results:
  A passes checkable rules, B fails three, C fails one, and D illustrates why
  constraints alone do not prove the return objective.
- **App render:** automated Streamlit validation completed with no app exceptions.
- **Clean launch:** a fresh clone of the clean Project 2 branch installed dependencies and
  returned HTTP 200 when launched; see `cold-run-record.md`.
- **Arithmetic check:** the displayed 6.51% base expected return equals
  `20% × 4.3% + 25% × 5.0% + 55% × 8.0%`.

## Limitations

The app does not validate real prices, forecast CPI, establish a five-year
real-return probability, provide issuer-level fund look-through, use actual
Foundation holdings, or define the calendar-year-loss measure and breach action.
Those limits support the reject-adoption decision.

## Material AI uses and dispositions

| AI/tool, model/version, and date | Material use | Disposition and independent check |
| --- | --- | --- |
| OpenAI ChatGPT/Codex, GPT-5 session, 2026-11-19 to 2026-11-21 | Organized the Streamlit app, portfolio calculations, and documentation. | **Accepted in part.** Runtime validation and a fresh-clone launch verified the app executes; the student owns the finance judgment. |
| OpenAI ChatGPT/Codex, GPT-5 session, 2026-11-19 | Suggested the earlier changed-input prediction wording. | **Rejected for final Locked Changed-Input Record.** The Project 2 rule requires a human-authored AI-off prediction committed before the run. |
| OpenAI ChatGPT/Codex, GPT-5 session, 2026-11-21 | Suggested a manual weighted-return check for the Equity-return stress. | **Accepted after arithmetic verification.** The base and changed weight/return calculations are shown in the visible output and app. |

## Final Locked Changed-Input Record

The final required record is [`locked-ai-off-record.md`](locked-ai-off-record.md).
It remains incomplete until the student writes the prediction without AI,
commits and pushes it to GitHub, runs the selected change, and records the
observed result and decision effect.
