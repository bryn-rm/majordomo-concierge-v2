"""Dynamic context construction for agents."""

from __future__ import annotations

from datetime import date

from ..memory.finance_store import FinanceStore
from ..memory.task_store import TaskStore
from ..memory.journal_store import JournalStore
from ..utils.date_utils import format_date


def build_daily_briefing_context() -> str:
    """Collect budget, tasks, and notes for morning briefings."""
    finance = FinanceStore()
    tasks = TaskStore()
    journal = JournalStore()

    spend = finance.monthly_spend_by_category()
    tasks_text = "\n".join(
        f"- [{priority}] {title} (due {due or 'unscheduled'})"
        for _, title, priority, due in tasks.upcoming()
    )
    entries = journal.entries_on(date.today())
    notes = "\n".join(f"- {etype}: {text}" for _, text, etype in entries)

    return (
        f"Date: {format_date(date.today())}\n"
        f"Budgets: {spend}\n"
        f"Tasks:\n{tasks_text or '- none'}\n"
        f"Notes:\n{notes or '- none'}"
    )
