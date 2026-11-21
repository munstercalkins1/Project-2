# Project 2 — Meridian Portfolio Decision Tool

**AI-use statement:** AI assisted with code organization and documentation.
The analysis and committee decision are the student's. This is educational work,
not investment advice.

This is the runnable FIN 390 Project 2 package. It evaluates five-point,
long-only portfolio mixes across BIL, IEF, LQD, and VTI using the included
teaching inputs. It is for course work, not investment advice.

## Start the app

From this repository's root folder, run:

```powershell
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

The app opens a local browser page. If `py` is unavailable on another computer,
install Python 3 first, then rerun the two commands above. The app works without
an account, external data download, or a notebook.

Read the pages in this order: visible Meridian mandate, point-in-time signal and
data card, three portfolio comparisons, illustrative annual rebalance, mandate
verdict, and stress run.

## Decision

**Do not adopt the allocation as an investment recommendation.** The tool may
identify a lowest-risk mix that reaches the course's 6.5% estimated-return
proxy and 3% reserve minimum, but the included price data are synthetic
teaching data and historical estimates are not forecasts. A committee would
need validated data, a confirmed mandate, transaction-cost evidence, and a
defined loss-limit process before any allocation decision.

## Package map

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit tool with editable return and reserve controls. |
| `portfolio.py` | Search, historical-estimation, and risk calculations. |
| `prices.csv` | Synthetic teaching price data, not market evidence. |
| `docs/decision-memo.md` | Decision, conditions, and limits. |
| `docs/visible-output.md` | Baseline decision numbers readable without running code. |
| `docs/validation-and-ai-use.md` | Baseline, changed-input, and AI-use record. |
| `docs/cold-run-record.md` | Partner cold-run record; fill it only after an actual run. |
| `docs/project-2-requirements-checklist.md` | Map from the Project 2 requirements to visible app sections and evidence files. |

## Changed-input record

Before changing a load-bearing input, write your prediction in
`docs/locked-changed-input-record.md`, commit it, and then run the app. Keep
the before and after result and state whether the decision changes. Do not
backdate the record or invent a partner result.
