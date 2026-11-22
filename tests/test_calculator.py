from expense_tracker.calculator import (
    reimbursable_amount,
    total,
    total_by_category,
    total_reimbursable,
)
from expense_tracker.models import Expense


def make(amount, category="food"):
    return Expense("test", amount, category, "2026-11-22")


def test_total():
    assert total([make(10), make(5.5)]) == 15.5


def test_total_empty():
    assert total([]) == 0


def test_total_by_category():
    expenses = [make(10, "food"), make(20, "transport"), make(5, "food")]
    assert total_by_category(expenses) == {"food": 15, "transport": 20}


def test_food_is_reimbursed_at_80_percent():
    assert reimbursable_amount(make(50, "food")) == 40


def test_food_reimbursement_is_capped():
    assert reimbursable_amount(make(200, "food")) == 50


def test_transport_reimbursement_is_capped():
    assert reimbursable_amount(make(500, "transport")) == 100


def test_unknown_category_is_not_reimbursed():
    assert reimbursable_amount(make(100, "entertainment")) == 0


def test_total_reimbursable():
    expenses = [make(50, "food"), make(30, "transport"), make(10, "games")]
    assert total_reimbursable(expenses) == 70
