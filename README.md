# Project-2Project 2 — Meridian Portfolio Decision Tool
This is the runnable FIN 390 Project 2 package. It evaluates five-point, long-only portfolio mixes across BIL, IEF, LQD, and VTI using the included teaching inputs. It is for course work, not investment advice.

Cold-run command
From the repository root, run:

python -m streamlit run "Project 2/app.py"
The app opens a local browser page. Move an expected-return control or switch to My saved prices.csv, then read the Mandate verdict shown below the two portfolio tables.

Decision
Do not adopt the allocation as an investment recommendation. The tool may identify a lowest-risk mix that reaches the course's 6.5% estimated-return proxy and 3% reserve minimum, but the included price data are synthetic teaching data and historical estimates are not forecasts. A committee would need validated data, a confirmed mandate, transaction-cost evidence, and a defined loss-limit process before any allocation decision.

Package map
File	Purpose
app.py	Streamlit tool with editable return and reserve controls.
portfolio.py	Search, historical-estimation, and risk calculations.
prices.csv	Synthetic teaching price data, not market evidence.
docs/decision-memo.md	Decision, conditions, and limits.
docs/visible-output.md	Baseline decision numbers readable without running code.
docs/validation-and-ai-use.md	Baseline, changed-input, and AI-use record.
docs/cold-run-record.md	Partner cold-run record; fill it only after an actual run.
Changed-input record
Before changing a load-bearing input, write your prediction in docs/locked-changed-input-record.md, commit it, and then run the app. Keep the before and after result and state whether the decision changes. Do not backdate the record or invent a partner result.
