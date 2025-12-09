"""Finance tools for expense tracking and budgeting."""

from __future__ import annotations

import re
from datetime import date
from typing import Dict, Optional

from ...memory.finance_store import FinanceStore
from ...utils.date_utils import days_remaining_in_month, parse_human_date
from ...utils.validators import ensure_positive_amount

CATEGORY_KEYWORDS: Dict[str, list[str]] = {
    "Groceries": ["tesco", "sainsbury", "asda", "morrisons", "grocery", "food"],
    "Utilities": ["electric", "gas", "water", "internet", "phone", "utility"],
    "Transport": ["petrol", "fuel", "bus", "train", "uber", "taxi", "parking"],
    "Entertainment": ["cinema", "netflix", "spotify", "game", "concert"],
    "Dining Out": ["restaurant", "cafe", "coffee", "pizza", "takeaway"],
    "Shopping": ["amazon", "mall", "shop", "clothes"],
    "Health": ["pharmacy", "chemist", "doctor", "dentist", "gym"],
}

DEFAULT_BUDGETS: Dict[str, float] = {
    "Groceries": 400.0,
    "Utilities": 300.0,
    "Transport": 200.0,
    "Entertainment": 150.0,
    "Dining Out": 180.0,
    "Shopping": 250.0,
    "Health": 120.0,
}

store = FinanceStore()


def _parse_amount(raw_amount: str | float) -> float:
    """Convert freeform amount strings like '£52.30' to floats."""
    if isinstance(raw_amount, (int, float)):
        return ensure_positive_amount(float(raw_amount))
    cleaned = re.sub(r"[^0-9.]", "", raw_amount)
    if not cleaned:
        raise ValueError("Unable to parse amount.")
    return ensure_positive_amount(float(cleaned))


def categorize_expense(description: str) -> str:
    """Infer category based on keywords."""
    text = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return category
    return "Other"


def log_expense(
    amount: str | float,
    description: str,
    when: Optional[str] = None,
    category: Optional[str] = None,
) -> str:
    """Record an expense, auto-categorize, and return budget context."""
    parsed_amount = _parse_amount(amount)
    expense_date: date = parse_human_date(when) if when else date.today()
    category = category or categorize_expense(description)

    # Seed default budget if none exists for the category
    if category in DEFAULT_BUDGETS and store.get_budget(category) is None:
        store.upsert_budget(category, DEFAULT_BUDGETS[category])

    store.add_expense(parsed_amount, description, category, expense_date)
    spend = store.spend_this_month(category)
    budget = store.get_budget(category)
    response = f"Logged £{parsed_amount:.2f} for '{description}' under {category}."

    if budget:
        pct = (spend / budget) * 100 if budget else 0
        remaining = max(budget - spend, 0)
        days_left = days_remaining_in_month()
        response += (
            f" This month: £{spend:.2f}/£{budget:.2f} ({pct:.2f}%)."
            f" £{remaining:.2f} remaining for {days_left} days."
        )
        if pct >= 80:
            response += " ⚠️ Budget alert: consider reducing spend."
    return response


def budget_status(category: str) -> str:
    """Return current month budget status for a category."""
    spend = store.spend_this_month(category)
    budget = store.get_budget(category)
    if not budget:
        return f"No budget set for {category}. Spent £{spend:.2f} this month."
    pct = (spend / budget) * 100 if budget else 0
    remaining = max(budget - spend, 0)
    days_left = days_remaining_in_month()
    return (
        f"{category}: £{spend:.2f}/£{budget:.2f} used ({pct:.2f}%)."
        f" £{remaining:.2f} left for {days_left} days."
    )


def monthly_summary() -> str:
    """Summarize spend by category for the current month."""
    breakdown = store.monthly_spend_by_category()
    if not breakdown:
        return "No expenses logged yet."
    lines = [f"- {cat}: £{total:.2f}" for cat, total in breakdown.items()]
    return "Month-to-date spend:\n" + "\n".join(lines)
