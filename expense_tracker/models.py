from dataclasses import dataclass, asdict


@dataclass
class Expense:
    description: str
    amount: float
    category: str
    date: str  # ISO format, e.g. 2026-11-22

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data["description"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
        )
