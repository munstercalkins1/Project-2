# Cold-Run Record

## Clean-clone check

| Field | Record |
| --- | --- |
| Tester | Codex clean-clone validation; not represented as a partner observation |
| Date and time | 2026-11-21 14:41 -06:00 |
| Source | GitHub branch `main` |
| Exact install command | `py -m pip install -r requirements.txt` |
| Exact app command | `py -m streamlit run app.py` |
| First failure, or clean result | Clean result: dependency install completed and the Streamlit app returned HTTP 200 at a local address. |
| Resolution or limitation | No failure occurred. This check used the same Windows/Python environment as development; a separate human/partner cold run is still useful before submission. |
| Where result appeared | Local Streamlit page at `http://127.0.0.1:8506` during the check. |

## Isolated-environment check

On 2026-11-21, a new virtual environment was created from a fresh `main`
clone. `requirements.txt` installed Streamlit 1.66.1 without relying on the
developer's global packages. The app launched under Python 3.13.15 and returned
HTTP 200 at `http://127.0.0.1:8508`.

The README commands were tested from a fresh clone of the published `main`
branch after the root-level repair.
