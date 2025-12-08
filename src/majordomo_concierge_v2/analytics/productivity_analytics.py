"""Productivity analytics for tasks and habits."""

from __future__ import annotations

from ..memory.task_store import TaskStore


def task_summary() -> str:
    """Summarize open tasks."""
    store = TaskStore()
    tasks = store.upcoming(20)
    open_count = len([t for t in tasks])
    high_priority = [t for t in tasks if t[2] == "high"]
    return f"{open_count} open tasks; {len(high_priority)} high priority."
