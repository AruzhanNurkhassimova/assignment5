# AGENTS.md

Instructions for AI coding agents working in this repository.

## Purpose
Expense Tracker is a small Python command-line tool that records personal
expenses in a local JSON file and prints totals by category, plus the amount a
company would reimburse. It is a learning project: keep it small and simple.

## Architecture
- `expense_tracker/models.py`: `Expense` dataclass (description, amount, category, date).
- `expense_tracker/storage.py`: `load_expenses` / `save_expenses` (JSON file).
- `expense_tracker/calculator.py`: totals, per-category totals, reimbursement rules.
- `expense_tracker/cli.py`: argparse interface (`add`, `list`, `summary`).
- `expense_tracker/__main__.py`: entry point for `python -m expense_tracker`.
- `tests/`: pytest tests for calculator and storage.

Dependencies: Python 3.10+, pytest (see `requirements.txt`). No other runtime dependencies.

## Setup (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Safe commands (allowed without asking)
```powershell
python -m pytest -v
ruff check .
mypy expense_tracker
python -m expense_tracker --file demo.json summary
git status
git diff
git log --oneline
```
Always use a temporary data file (for example `demo.json`) when running the CLI.
Delete temporary data files afterwards.

## Commands that need human approval first
- `pip install` / `pip uninstall` or any edit to `requirements.txt`
- `ruff --fix`, `black`, or any tool that rewrites many files
- `git commit`, `git checkout`, `git merge`, `git rebase`

## Forbidden actions
- No secrets: never create, read, print or commit API keys, tokens, passwords or `.env` files.
- No real personal or financial data in code, tests, examples or commits.
- No production deployments or publishing of packages.
- No destructive commands: `rm -rf` / `Remove-Item -Recurse -Force`, `git reset --hard`,
  `git push --force`, `git clean -fd`, deleting the `.git` folder.
- No unreviewed dependency changes (adding, removing or upgrading packages).
- Do not delete or weaken tests to make them pass.
- Do not edit the `baseline` git tag or the `evidence/` folder.
- Do not touch files outside this repository.

## Coding conventions
- Python 3.10+, PEP 8, 4-space indentation, lines up to 100 characters.
- Add type hints to new or changed functions.
- Keep business logic in `calculator.py`; keep input/output in `cli.py`.
- Prefer small, focused changes: one concern per change.

## Test expectations
- Every behaviour change needs a pytest test in `tests/`.
- Run `python -m pytest -v` before and after your change and report both results.
- Never claim a test passed unless you ran it and saw the output.
- Report any check that you could not run.

## Acceptance criteria that must stay true
1. `add` stores an expense and `list` shows it.
2. `summary` prints correct totals per category and overall.
3. Reimbursement rules: food 80% capped at 50, transport capped at 100,
   office capped at 200, all other categories 0.
4. Expenses survive between runs (save and load roundtrip).
5. `python -m pytest` exits with code 0.

## Review gates
- Show the full diff and a short change summary before any commit.
- A human reviews and approves every change; the agent never merges or deploys.
- If unsure about scope, stop and ask instead of guessing.
