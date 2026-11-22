import argparse
import sys
from datetime import date

from . import calculator
from .models import Expense
from .storage import load_expenses, save_expenses, DEFAULT_PATH


def build_parser():
    parser = argparse.ArgumentParser(prog="expense-tracker")
    parser.add_argument("--file", default=DEFAULT_PATH, help="path to the data file")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add an expense")
    add.add_argument("description")
    add.add_argument("amount", type=float)
    add.add_argument("category")
    add.add_argument("--date", default=date.today().isoformat())

    sub.add_parser("list", help="list all expenses")
    sub.add_parser("summary", help="show totals by category")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    expenses = load_expenses(args.file)

    if args.command == "add":
        expenses.append(Expense(args.description, args.amount, args.category, args.date))
        save_expenses(expenses, args.file)
        print(f"Added: {args.description} ({args.amount:.2f}, {args.category})")
    elif args.command == "list":
        for e in expenses:
            print(f"{e.date}  {e.category:<10} {e.amount:>9.2f}  {e.description}")
    elif args.command == "summary":
        for category, amount in sorted(calculator.total_by_category(expenses).items()):
            print(f"{category:<10} {amount:>9.2f}")
        print(f"{'TOTAL':<10} {calculator.total(expenses):>9.2f}")
        print(f"{'REIMBURSABLE':<12} {calculator.total_reimbursable(expenses):>7.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
