import json
import os

from .models import Expense

DEFAULT_PATH = "expenses.json"


def load_expenses(path=DEFAULT_PATH):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Expense.from_dict(item) for item in data]


def save_expenses(expenses, path=DEFAULT_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=2)
