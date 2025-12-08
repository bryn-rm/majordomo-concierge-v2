"""Input validation helpers."""

from __future__ import annotations


def ensure_positive_amount(amount: float) -> float:
    """Ensure amount is a positive float."""
    if amount < 0:
        raise ValueError("Amount must be positive.")
    return round(float(amount), 2)
