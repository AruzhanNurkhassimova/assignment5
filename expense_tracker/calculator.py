from collections import defaultdict


def total(expenses):
    """Sum of all expense amounts."""
    return sum(e.amount for e in expenses)


def total_by_category(expenses):
    """Return {category: total amount}."""
    result = defaultdict(float)
    for e in expenses:
        result[e.category] += e.amount
    return dict(result)


def reimbursable_amount(expense):
    """How much of an expense the company would reimburse.

    Rules differ per category.
    """
    if expense.category == "food":
        # meals: 80% reimbursed, capped at 50
        amount = expense.amount * 0.8
        if amount > 50:
            amount = 50
        return amount
    elif expense.category == "transport":
        # transport: 100% reimbursed, capped at 100
        amount = expense.amount
        if amount > 100:
            amount = 100
        return amount
    elif expense.category == "office":
        # office supplies: 100% reimbursed, capped at 200
        amount = expense.amount
        if amount > 200:
            amount = 200
        return amount
    else:
        # everything else is not reimbursed
        return 0


def total_reimbursable(expenses):
    return sum(reimbursable_amount(e) for e in expenses)
