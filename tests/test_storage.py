from expense_tracker.models import Expense
from expense_tracker.storage import load_expenses, save_expenses


def test_missing_file_returns_empty_list(tmp_path):
    assert load_expenses(str(tmp_path / "nope.json")) == []


def test_save_and_load_roundtrip(tmp_path):
    path = str(tmp_path / "data.json")
    expenses = [Expense("lunch", 12.5, "food", "2026-11-22")]
    save_expenses(expenses, path)
    assert load_expenses(path) == expenses
