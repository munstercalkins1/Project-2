# Project 2 Video Recording Guide

This is a recording guide, not a transcript. After recording, enable YouTube
transcripts and link or attach the actual transcripts in the final manifest.

## Required opening for every video

Say this at the beginning of **each** video:

> AI assisted with code organization and documentation. The analysis and
> committee decision are mine. This is educational work, not investment advice.

Keep your webcam visible in the frame for the recording.

## Video 1 — System and thinking changes; AI output checked

1. State the opening above.
2. Explain the Meridian mandate: CPI + 4% objective, liquidity reserve,
   long-only rule, issuer limit, annual rebalancing, and unresolved loss rule.
3. Explain why passing constraints alone is not proof of meeting the objective.
4. Describe the changed-input test: Equity return 8.0% to 7.0%, prediction,
   result, and increased Equity allocation/risk.
5. Identify one AI output you checked: the claim that lower Equity expected
   return makes the 6.5% proxy harder to reach. Explain the weighted-return
   arithmetic recorded in `validation-and-ai-use.md`.

## Video 2 — Code walkthrough

1. State the opening above.
2. Show `app.py`: mandate panel, bounded controls, reset button, baselines,
   constrained search, rebalance approval test, stress table, and decision.
3. Show `portfolio.py`: portfolio return/volatility calculation, long-only
   five-point search, baseline construction, mandate verdict, and point-in-time
   signal function.
4. Show `prices.csv` and explain that it is labeled synthetic teaching data.
5. Show `locked-changed-input-record.md` and the validation record.

## Video 3 — Committee presentation

1. Start with the app already running live in the browser; operate it first.
2. State the opening above while webcam is visible.
3. Show the mandate, three portfolios, and which mandate rules pass, fail, or
   require clarification.
4. Show the annual rebalance: turnover above 25% requires committee approval.
5. Show the stress table and the red process-stop condition.
6. State the conclusion: reject adoption; allocation range now is 0% to 0%;
   explain the monitoring triggers required before reconsidering a pilot.
