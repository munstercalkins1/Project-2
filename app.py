"""Streamlit interface for the Project 2 Meridian portfolio decision tool.

Run: streamlit run app.py
"""

from __future__ import annotations

from io import StringIO
from pathlib import Path

import streamlit as st

from portfolio import (MERIDIAN_ASSETS, MERIDIAN_CORRELATIONS, MERIDIAN_OBJECTIVE,
                       MERIDIAN_RESERVE_ELIGIBLE, MERIDIAN_RESERVE_MINIMUM,
                       MERIDIAN_RETURNS, MERIDIAN_VOLATILITIES,
                       annual_equity_trend_signal, equal_weight_mix, estimate_from_prices, mandate_verdict,
                       portfolio_metrics, search_lowest_risk_mix, sixty_forty_mix)

PRICE_TICKER_TO_ASSET = {"BIL": "Bills", "IEF": "10-year", "LQD": "IG", "VTI": "Equity"}


def read_uploaded_estimates(uploaded_file, last_36_months):
    text = uploaded_file.getvalue().decode("utf-8-sig")
    return estimate_from_prices(StringIO(text), last_36_months)


def show_portfolio(title, weights, expected_returns, volatilities, correlations,
                   reserve_eligible, reserve_minimum):
    st.subheader(title)
    expected_return, volatility = portfolio_metrics(weights, expected_returns, volatilities, correlations)
    reserve_weight = sum(weights[asset] for asset in weights if asset in reserve_eligible)
    st.dataframe({"Asset": list(weights), "Weight": list(weights.values())},
                 hide_index=True, column_config={"Weight": st.column_config.NumberColumn(format="%.0%%")})
    one, two, three = st.columns(3)
    one.metric("Estimated return", f"{expected_return:.2%}")
    two.metric("Estimated volatility", f"{volatility:.2%}")
    three.metric("Reserve-eligible", f"{reserve_weight:.2%}")
    st.caption("Mandate verdict")
    for rule, detail, passed in mandate_verdict(weights, reserve_eligible, reserve_minimum):
        if passed is True:
            st.success(f"PASS — {rule}: {detail}")
        elif passed is False:
            st.error(f"FAIL — {rule}: {detail}")
        else:
            st.warning(f"MONITOR — {rule}: {detail}")


def estimates_from_teaching_prices(last_36_months):
    """Map teaching CSV tickers to the asset-sleeve names used by the optimizer."""
    returns, volatilities, correlations = estimate_from_prices(
        Path(__file__).with_name("prices.csv"), last_36_months
    )
    if set(returns) != set(PRICE_TICKER_TO_ASSET):
        raise ValueError("teaching prices.csv must contain BIL, IEF, LQD, and VTI")
    mapped_returns = {PRICE_TICKER_TO_ASSET[ticker]: value for ticker, value in returns.items()}
    mapped_volatilities = {PRICE_TICKER_TO_ASSET[ticker]: value for ticker, value in volatilities.items()}
    mapped_correlations = {
        PRICE_TICKER_TO_ASSET[left]: {
            PRICE_TICKER_TO_ASSET[right]: value for right, value in row.items()
        }
        for left, row in correlations.items()
    }
    return mapped_returns, mapped_volatilities, mapped_correlations


def stress_result(name, changed_input, returns, volatilities, correlations, objective,
                  reserve_eligible, reserve_minimum, current_weights, cost_rate):
    """Run one transparent sensitivity scenario and return one table row."""
    answer = search_lowest_risk_mix(
        returns, volatilities, correlations, objective, reserve_eligible, reserve_minimum
    )
    if answer is None:
        return {
            "Scenario": name, "Changed input": changed_input,
            "Status": "STOP — no feasible mix", "Net return after one-time cost": "—",
            "Volatility": "—", "Reserve": "—", "Weights": "—",
        }
    weights = answer["weights"]
    turnover = 0.5 * sum(abs(weights[asset] - current_weights[asset]) for asset in weights)
    implementation_cost = turnover * cost_rate
    net_return = answer["return"] - implementation_cost
    passes = net_return + 1e-12 >= objective
    weight_text = ", ".join(f"{asset} {weight:.0%}" for asset, weight in weights.items())
    return {
        "Scenario": name,
        "Changed input": changed_input,
        "Status": "PASS" if passes else "STOP — net return below objective",
        "Net return after one-time cost": f"{net_return:.2%}",
        "Volatility": f"{answer['volatility']:.2%}",
        "Reserve": f"{answer['reserve_weight']:.0%}",
        "Weights": weight_text,
    }


st.set_page_config(page_title="Meridian Portfolio Decision Tool", layout="wide")
st.title("Meridian Portfolio Decision Tool")
st.caption(
    "AI assisted with code organization and documentation. The analysis and committee decision are the student's; "
    "this is educational work, not investment advice."
)

with st.expander("Meridian Foundation Reserve mandate", expanded=True):
    mandate_left, mandate_right = st.columns(2)
    with mandate_left:
        st.markdown("""
        **Objective:** CPI + 4% net of costs over rolling five-year periods.

        **Horizon and governance:** Seven-year horizon; annual rebalancing;
        turnover above 25% requires committee approval.

        **Universe:** Bills, 10-year government bonds, investment-grade bonds,
        and global Equity sleeves. This classroom app does not claim issuer-level
        holdings or real investability.

        **Benchmark:** 60/40 Equity / 10-year government-bond mix, used as a
        comparison reference rather than a required allocation.
        """)
    with mandate_right:
        st.markdown("""
        **Risk measure:** Annualized volatility, shown for every portfolio.

        **Checkable limits:** Long-only; no borrowing, shorts, or derivatives;
        at least 90% redeemable within five business days; at least 3% in a
        cash/daily-liquid government reserve; and single-issuer exposure at or
        below 8% after underlying-holding look-through.

        **Unresolved limit:** “No calendar-year loss greater than 10%” requires
        CIO clarification of the measurement convention and breach action.

        **Teaching proxy:** The 6.5% model objective is a transparent classroom
        proxy only; it does not prove the CPI + 4% objective.
        """)

try:
    signal = annual_equity_trend_signal(Path(__file__).with_name("prices.csv"))
except ValueError as error:
    st.error(f"Could not calculate the annual point-in-time signal: {error}")
    st.stop()

st.subheader("Annual point-in-time signal")
signal_left, signal_middle, signal_right = st.columns(3)
signal_left.metric("Signal as of", signal["as_of"])
signal_middle.metric("VTI trailing 12-month return", f"{signal['trailing_return']:.2%}")
signal_right.metric("Regime for annual rebalance", signal["regime"])
st.info(
    f"Data card: VTI monthly adjusted closes from the included teaching dataset. "
    f"The signal uses {signal['start_date']} through {signal['as_of']} and can affect the "
    f"{signal['next_rebalance_year']} annual rebalance only; it does not use future prices."
)
st.caption("Project 2 · Built with AI help · teaching inputs, not investment advice.")

with st.expander("Point-in-time signal data card"):
    st.markdown(f"""
    - **Signal:** VTI 12-month trailing total-price return; positive is labeled **Growth**, otherwise **Defensive**.
    - **Decision date:** {signal['as_of']}; the signal may affect only the {signal['next_rebalance_year']} annual rebalance.
    - **Source and field:** monthly adjusted-close teaching data in `prices.csv`, column `VTI`.
    - **Lookback:** {signal['start_date']} through {signal['as_of']} (12 monthly observations).
    - **Point-in-time rule:** no price after {signal['as_of']} is used.
    - **Limitation:** the file is synthetic classroom data; the signal is not a forecast or an investment recommendation.
    """)

base_control_values = {
    "objective_control": MERIDIAN_OBJECTIVE * 100,
    "reserve_control": MERIDIAN_RESERVE_MINIMUM * 100,
    "last_36_control": False,
}
for control_key, control_value in base_control_values.items():
    if control_key not in st.session_state:
        st.session_state[control_key] = control_value

with st.sidebar:
    st.header("Controls")
    if st.button("Reset to base case"):
        st.session_state["objective_control"] = MERIDIAN_OBJECTIVE * 100
        st.session_state["reserve_control"] = MERIDIAN_RESERVE_MINIMUM * 100
        st.session_state["last_36_control"] = False
        for asset_name, return_value in MERIDIAN_RETURNS.items():
            st.session_state[f"return_{asset_name}"] = return_value * 100
        for asset_name in MERIDIAN_ASSETS:
            st.session_state[f"reserve_{asset_name}"] = asset_name in MERIDIAN_RESERVE_ELIGIBLE
        st.rerun()
    objective = st.number_input(
        "Objective expected return (%)", min_value=0.0, max_value=15.0,
        step=0.1, key="objective_control"
    ) / 100
    reserve_minimum = st.number_input(
        "Reserve minimum (%)", min_value=0.0, max_value=100.0,
        step=0.1, key="reserve_control"
    ) / 100
    uploaded_file = st.file_uploader("Upload prices.csv", type="csv")
    last_36 = st.toggle("Use only the last 36 months", key="last_36_control")

try:
    if uploaded_file is None:
        loaded_returns = MERIDIAN_RETURNS.copy()
        loaded_volatilities = MERIDIAN_VOLATILITIES.copy()
        loaded_correlations = MERIDIAN_CORRELATIONS
        source_label = "Meridian inputs"
    else:
        loaded_returns, loaded_volatilities, loaded_correlations = read_uploaded_estimates(uploaded_file, last_36)
        source_label = "CSV historical estimates (not forecasts)"
except ValueError as error:
    st.error(f"Could not read the CSV: {error}")
    st.stop()

assets = list(loaded_returns)
st.write(f"**Source:** {source_label}. Returns are annual estimates.")
st.subheader("Expected-return estimates")
edited_returns = {}
for asset in assets:
    return_key = f"return_{asset}"
    if return_key not in st.session_state:
        st.session_state[return_key] = float(loaded_returns[asset] * 100)
    edited_returns[asset] = st.number_input(
        f"{asset} return (%)", min_value=0.0, max_value=20.0,
        step=0.1, key=return_key
    ) / 100

st.subheader("Reserve eligibility")
reserve_eligible = set()
for asset in assets:
    default = asset in MERIDIAN_RESERVE_ELIGIBLE if uploaded_file is None else False
    reserve_key = f"reserve_{asset}"
    if reserve_key not in st.session_state:
        st.session_state[reserve_key] = default
    if st.checkbox(asset, key=reserve_key):
        reserve_eligible.add(asset)

try:
    equal_weights = equal_weight_mix(assets)
    benchmark_weights = sixty_forty_mix(assets)
except ValueError as error:
    st.error(f"The selected data cannot create the required baseline: {error}")
    st.stop()

constrained_answer = search_lowest_risk_mix(edited_returns, loaded_volatilities, loaded_correlations,
                                            objective, reserve_eligible, reserve_minimum)
if constrained_answer is None:
    st.error("No constrained Meridian portfolio reaches the selected return objective and reserve minimum.")
    st.stop()

first, second, third = st.columns(3)
with first:
    show_portfolio("Equal-weight baseline", equal_weights, edited_returns, loaded_volatilities,
                   loaded_correlations, reserve_eligible, reserve_minimum)
with second:
    show_portfolio("60/40 benchmark baseline", benchmark_weights, edited_returns, loaded_volatilities,
                   loaded_correlations, reserve_eligible, reserve_minimum)
with third:
    show_portfolio("Constrained Meridian portfolio", constrained_answer["weights"], edited_returns,
                   loaded_volatilities, loaded_correlations, reserve_eligible, reserve_minimum)

st.divider()
st.header("Illustrative annual rebalance")
st.caption(
    "For this classroom illustration, the Equal-weight baseline is treated as the current portfolio. "
    "Replace it with validated actual holdings before making a real recommendation."
)
target_weights = constrained_answer["weights"]
turnover = 0.5 * sum(abs(target_weights[asset] - equal_weights[asset]) for asset in assets)
estimated_cost = turnover * 0.001  # 10 basis points, disclosed teaching assumption.
rebalance_left, rebalance_middle, rebalance_right = st.columns(3)
rebalance_left.metric("One-way turnover", f"{turnover:.0%}")
rebalance_middle.metric("Estimated one-time cost", f"{estimated_cost:.2%}")
rebalance_right.metric("Annual rebalance schedule", "Yes")
if turnover > 0.25:
    st.warning("COMMITTEE APPROVAL REQUIRED — turnover is above the 25% Meridian governance limit.")
else:
    st.success("Turnover is at or below 25%; no special turnover approval is triggered.")

st.divider()
st.subheader("Mandate verdict")
st.error("NOT CLEARED — the displayed mix is a classroom screen, not an investment recommendation.")
st.markdown(
    "The 6.5% objective is an estimated-return proxy, and the included price file is "
    "synthetic teaching data. Validate inputs, costs, the actual mandate objective, "
    "and the loss-limit process before any allocation decision."
)

st.divider()
st.header("Stress run")
st.caption(
    "Every scenario uses the same long-only five-point search. One-time trading costs assume the "
    "current holding is the equal-weight baseline; this is a transparent classroom assumption, not evidence of the Foundation's actual holdings."
)

base_returns = MERIDIAN_RETURNS.copy()
lower_equity_returns = MERIDIAN_RETURNS.copy()
lower_equity_returns["Equity"] = 0.07

try:
    window_returns, window_volatilities, window_correlations = estimates_from_teaching_prices(True)
except ValueError as error:
    st.error(f"Could not run the 36-month window stress: {error}")
    window_returns, window_volatilities, window_correlations = None, None, None

stress_rows = [
    stress_result(
        "Base case", "Base estimates; 10 bp implementation cost",
        base_returns, MERIDIAN_VOLATILITIES, MERIDIAN_CORRELATIONS,
        MERIDIAN_OBJECTIVE, MERIDIAN_RESERVE_ELIGIBLE, MERIDIAN_RESERVE_MINIMUM,
        equal_weights, 0.001,
    ),
    stress_result(
        "Estimate stress", "Equity expected return: 8.0% → 7.0%",
        lower_equity_returns, MERIDIAN_VOLATILITIES, MERIDIAN_CORRELATIONS,
        MERIDIAN_OBJECTIVE, MERIDIAN_RESERVE_ELIGIBLE, MERIDIAN_RESERVE_MINIMUM,
        equal_weights, 0.001,
    ),
    stress_result(
        "Cost stress", "Implementation cost: 10 bp → 50 bp",
        base_returns, MERIDIAN_VOLATILITIES, MERIDIAN_CORRELATIONS,
        MERIDIAN_OBJECTIVE, MERIDIAN_RESERVE_ELIGIBLE, MERIDIAN_RESERVE_MINIMUM,
        equal_weights, 0.005,
    ),
    stress_result(
        "Constraint stress", "Reserve floor: 3% → 25%",
        base_returns, MERIDIAN_VOLATILITIES, MERIDIAN_CORRELATIONS,
        MERIDIAN_OBJECTIVE, MERIDIAN_RESERVE_ELIGIBLE, 0.25,
        equal_weights, 0.001,
    ),
]
if window_returns is not None:
    stress_rows.append(stress_result(
        "Window stress", "Historical estimates: most recent 36 monthly returns",
        window_returns, window_volatilities, window_correlations,
        MERIDIAN_OBJECTIVE, MERIDIAN_RESERVE_ELIGIBLE, MERIDIAN_RESERVE_MINIMUM,
        equal_weights, 0.001,
    ))

st.dataframe(stress_rows, hide_index=True, width="stretch")
if any(row["Status"].startswith("STOP") for row in stress_rows):
    st.error(
        "PROCESS STOP: Do not recommend allocation when a reasonable stress scenario has no feasible mix "
        "or cannot meet the estimated return objective after implementation costs. Escalate to the committee."
    )
else:
    st.success("No mechanical stop was triggered in these scenarios. The separate CIO clarification and data-validation requirements still prevent adoption.")

st.divider()
st.header("Committee recommendation")
recommendation_left, recommendation_right = st.columns(2)
recommendation_left.metric("Recommendation", "REJECT adoption")
recommendation_left.metric("Allocation range now", "0% to 0%")
recommendation_right.markdown("""
**Monitor before reconsidering a pilot or allocation:**

- validated market data and return assumptions;
- credible evidence for the CPI + 4% net-of-costs objective;
- observed implementation costs and annual turnover;
- issuer-level look-through for the 8% concentration rule; and
- CIO definition of the calendar-year-loss measure and breach action.
""")
st.info(
    "No allocation is recommended until these triggers are resolved. A later pilot range must be set by the committee "
    "after those inputs are validated."
)
