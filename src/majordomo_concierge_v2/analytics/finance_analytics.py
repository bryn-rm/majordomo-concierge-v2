"""Finance analytics helpers."""

from __future__ import annotations

from typing import Dict

from ..memory.finance_store import FinanceStore


def spending_breakdown() -> Dict[str, float]:
    """Return month-to-date spend by category."""
    store = FinanceStore()
    return store.monthly_spend_by_category()
