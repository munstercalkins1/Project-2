# Project 2 Video Scripts and Screen Cues

Use your webcam in every recording. Speak naturally rather than reading too
fast. Keep the app, code, or document named in the **Show** column visible.

## Required opening for every video

> AI assisted with code organization and documentation. The analysis and
> committee decision are mine. This is educational work, not investment advice.

## Video 1 - System, thinking changes, and AI check (target: 2:30)

| Time | Show | Say |
| --- | --- | --- |
| 0:00 | Webcam and app visible | Required opening above. |
| 0:15 | App mandate panel | My client is the Meridian Foundation Reserve. Its objective is CPI plus 4 percent net of costs over rolling five-year periods. The mandate also requires liquidity, a reserve, long-only implementation, issuer limits, and annual rebalancing. |
| 0:45 | Three portfolio columns | I compare equal weight, the transparent 60/40 benchmark, and my constrained portfolio. This lets a committee see whether the proposed portfolio improves on simple alternatives without hiding the tradeoffs. |
| 1:15 | `docs/locked-ai-off-record.md` | I made one AI-off prediction before changing Equity expected return from 8 percent to 9 percent, committed that prediction to GitHub, and then ran the test. |
| 1:45 | App constrained portfolio / record result | The Equity allocation moved from 55 percent to 45 percent. The investment recommendation did not change because a better expected-return input does not validate the synthetic data or prove the CPI plus 4 percent objective. |
| 2:15 | App stress run | AI helped organize the tool, but I checked the result using the app output and the validation record. My decision remains reject adoption and allocate 0 percent for now. |

## Video 2 - Code walkthrough (target: 4:00)

| Time | Show | Say |
| --- | --- | --- |
| 0:00 | Webcam and `app.py` | Required opening above. This video explains how the app works. |
| 0:15 | Top of `app.py` | The app is built in Streamlit. The mandate panel makes the committee objective, benchmark, risk measure, constraints, and unresolved loss-rule issue visible. |
| 0:55 | Controls / relevant code in `app.py` | The driver panel has bounded inputs and a reset button. Users can change expected returns, the objective proxy, reserve requirement, and estimation window without editing the code. |
| 1:30 | `portfolio.py` | This file calculates expected return and volatility and searches long-only five-percentage-point portfolios. It also builds the equal-weight and 60/40 baselines. |
| 2:10 | `portfolio.py` mandate function | The mandate verdict checks weights, long-only status, reserve, liquidity, and flags items that need issuer look-through, turnover history, or CIO clarification. |
| 2:45 | `prices.csv` and signal code | The point-in-time signal uses the synthetic monthly VTI teaching data only through its stated decision date. The data card discloses that the inputs are synthetic and not forecasts. |
| 3:20 | Stress-run area of `app.py` | The stress run changes expected return, historical window, transaction cost, and reserve constraint. If a reasonable scenario has no feasible mix or cannot meet the proxy after cost, the process stops. |
| 3:50 | `docs/validation-and-ai-use.md` | The validation record documents sources, limits, tests, AI uses, and the locked changed-input record. |

## Video 3 - Committee presentation (target: 3:30)

| Time | Show | Say |
| --- | --- | --- |
| 0:00 | **Live Streamlit app already running**, webcam visible | Required opening above. This is the live Meridian Portfolio Decision Tool. |
| 0:15 | Mandate panel | The mandate seeks CPI plus 4 percent net of costs. The benchmark is 60/40, but it is a comparison reference rather than a required allocation. The risk measure shown is annualized volatility. |
| 0:45 | Three portfolio columns | The app shows equal weight, 60/40, and the constrained portfolio side by side. Each has a mandate verdict so a committee can see which rule passes, fails, or requires monitoring. |
| 1:20 | Annual rebalance section | This is the annual rebalance screen. If turnover is above 25 percent, the app flags that committee approval is required. |
| 1:45 | Stress run | These scenarios change estimates, the historical window, implementation costs, and a reserve constraint. The red process-stop rule prevents us from treating a fragile output as an investment recommendation. |
| 2:25 | Committee recommendation section | My recommendation is reject adoption and allocate 0 percent at this time. The tool is transparent, but synthetic teaching data do not prove the CPI plus 4 percent objective. |
| 2:55 | Recommendation monitor list | Before reconsidering a pilot, I would require validated market data, credible return evidence, actual costs and turnover, issuer look-through, and a defined calendar-year-loss breach process. |
| 3:20 | Webcam / app | Thank you. |
