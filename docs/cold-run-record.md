# Cold-Run Record

## Clean-clone check

| Field | Record |
| --- | --- |
| Tester | Codex clean-clone validation; not represented as a partner observation |
| Date and time | 2026-11-21 14:02 -06:00 |
| Source | GitHub branch `main` (after root-level publication) |
| Exact install command | `py -m pip install -r requirements.txt` |
| Exact app command | `py -m streamlit run app.py` |
| First failure, or clean result | Clean result: dependency install completed and the Streamlit app returned HTTP 200 at a local address. |
| Resolution or limitation | No failure occurred. This check used the same Windows/Python environment as development; a separate human/partner cold run is still useful before submission. |
| Where result appeared | Local Streamlit page at `http://127.0.0.1:8506` during the check. |

The README commands were tested from a fresh clone of the published
`final-project2` branch before it is published to `main`.
