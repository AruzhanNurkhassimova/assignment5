# Expense Tracker

A small command-line tool for recording personal expenses and summarising them
by category. Data is stored in a local JSON file.

## Requirements

- Python 3.10+
- pytest (for the tests)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python -m expense_tracker add "Lunch" 12.50 food
python -m expense_tracker add "Bus ticket" 3.00 transport --date 2026-11-20
python -m expense_tracker list
python -m expense_tracker summary
```

Use `--file path/to/data.json` before the command to choose another data file.

## Tests

```bash
python -m pytest
```

## Project layout

```
expense_tracker/
  models.py      Expense dataclass
  storage.py     load/save expenses as JSON
  calculator.py  totals and reimbursement rules
  cli.py         argparse command-line interface
tests/           pytest tests
```
