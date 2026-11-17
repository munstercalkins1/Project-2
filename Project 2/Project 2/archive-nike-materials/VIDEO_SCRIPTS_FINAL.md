# Project 1 Final Recording Scripts

## Video 1 Research Evolution

Show `SOURCE_MAP.md` and `ASSUMPTION_REGISTER.md`.

“My target is NIKE, and the committee question is whether to initiate, watch/defer, or not initiate a position over a five-year horizon. My valuation date is September 10, 2026, in U.S. dollars. I began with FY2026’s 10-K as the source of record. Revenue was essentially flat, but the mix was uneven: wholesale improved while NIKE Direct and digital remained weak. That changed my original instinct from a simple recovery thesis to a conditional watch/defer view.

“On screen are two documents. First, `SOURCE_MAP.md` separates reported facts, normalizations, forecasts, and model outputs, and gives the filing source and date for each material input. Its main normalization is that I do not treat the $986 million IEEPA tariff-recovery benefit as recurring margin improvement. Second, `ASSUMPTION_REGISTER.md` lists each load-bearing forecast driver, its basis, the challenge to it, and the evidence that would make me change it. My main research triggers are Direct and digital stabilization, promotion intensity, Greater China, Converse, and inventory conversion. Those facts would either support or weaken the recovery forecast.”

## Video 2 Code and Validation

Show `nike_fcff_application.py`, then `nike_fcff_output.md`.

“First, this is my locally runnable NIKE FCFF application. It builds income statement, balance sheet, cash flow, and FCFF forecasts from FY2027 through FY2031. Revenue is driven separately by wholesale and Direct growth, then gross margin, SG&A, working capital, capex, and tax flow through the statements. FCFF is discounted at WACC, and the model bridges enterprise value to equity by adding cash and short-term investments and subtracting debt. I use the disclosed FY2026 diluted weighted-average share count consistently and disclose that limitation. The code fails loudly if the balance sheet does not balance or cash flow does not tie to cash. It also runs a synthetic known-answer DCF test, base-year reconciliation, WACC and terminal-growth monotonicity checks, and an enterprise-to-equity bridge check.

“Second, this is the visible output produced by that code. It shows the five-year forecast tables, the downside, base, and upside cases, the WACC and terminal-growth sensitivity table, the reverse DCF, and the passed validation checks. My changed-input test moved FY2027 Direct growth from 0% to -4%; value fell from $44.68 to $44.17 per share, then I restored the base case.”

## Video 3 Committee Defense

Show `COMMITTEE_MEMO.md`, then `Project_1_Edition_B_NIKE.md`.

“First, this is my committee memo. My recommendation is watch/defer, not a single-price call. The DCF produces a downside, base, and upside range of $28.52 to $62.20 per share, and the output shows how WACC and terminal growth change it. The base case requires a gradual recovery in NIKE Direct, wholesale growth, and gross margin. I do not average it with the P/E result or the EV/EBIT reference. The peer work has only one qualified peer, lululemon, and its more vertically retail-led apparel mix is materially different from NIKE’s scale and wholesale exposure. It is a cautionary reference, not a peer range.

“Second, this is my Edition B decision document. It connects the recommendation to the source map, assumptions, model, peer multiples, and validation record. I would move toward initiating only after Direct and digital stabilize, gross margin improves without temporary benefits or heavy promotions, and cash conversion improves. I would move toward do-not-initiate if those conditions deteriorate or the market price exceeds the high-case range without new supporting evidence.”

## AI Disclosure if Asked

“AI helped accelerate organization and code scaffolding; I independently checked cited filing facts, retained responsibility for assumptions and judgment, and recorded the qualified use in the validation record.”
