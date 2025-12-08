"""Workflow assembly helpers."""

from __future__ import annotations

from ..prompts.context_builder import build_daily_briefing_context
from ..tools.local import budget_status, upcoming


def build_morning_briefing() -> str:
    """Compose a text briefing using local data."""
    context = build_daily_briefing_context()
    budgets = budget_status("Groceries")
    tasks = upcoming()
    return (
        "Morning briefing:\n"
        f"{context}\n"
        f"Budget check: {budgets}\n"
        f"Tasks:\n{tasks}"
    )
