"""Unit tests for finance tools."""

from majordomo_concierge_v2.tools.local.finance_tools import categorize_expense


def test_categorize_expense_uses_keywords():
    assert categorize_expense("Bought groceries at Tesco") == "Groceries"
    assert categorize_expense("Paid my gas utility bill") == "Utilities"
