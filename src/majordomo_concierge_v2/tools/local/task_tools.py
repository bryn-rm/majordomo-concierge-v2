"""Task and habit management tools."""

from __future__ import annotations

from datetime import date
from typing import Optional

from ...memory.task_store import TaskStore
from ...utils.date_utils import parse_human_date

store = TaskStore()


def add_task(
    title: str,
    description: str = "",
    priority: str = "medium",
    due: Optional[str] = None,
) -> str:
    """Create a task with optional due date."""
    due_date = parse_human_date(due) if due else None
    task_id = store.add_task(
        title=title, description=description, priority=priority, due_date=due_date
    )
    return f"Task {task_id} created with priority {priority}."


def complete_task(task_id: int) -> str:
    """Mark a task complete."""
    store.update_status(task_id, "done")
    return f"Task {task_id} marked as done."


def upcoming(limit: int = 5) -> str:
    """Return a formatted list of upcoming tasks."""
    tasks = store.upcoming(limit)
    if not tasks:
        return "No upcoming tasks."
    lines = []
    for task_id, title, priority, due in tasks:
        due_str = due or "unscheduled"
        lines.append(f"- [{priority}] {title} (due {due_str}) #{task_id}")
    return "\n".join(lines)


def list_tasks() -> str:
    """List all tasks with status."""
    tasks = store.upcoming(50)
    if not tasks:
        return "No tasks found."
    lines = []
    for task_id, title, priority, due in tasks:
        due_str = due or "unscheduled"
        lines.append(f"- #{task_id} [{priority}] {title} (due {due_str})")
    return "\n".join(lines)


def add_habit(name: str, frequency: str = "daily") -> str:
    """Create a habit."""
    habit_id = store.add_habit(name, frequency)
    return f"Habit {habit_id} created for {frequency} tracking."


def complete_habit(habit_id: int) -> str:
    """Increment habit streak."""
    store.complete_habit(habit_id)
    return f"Habit {habit_id} recorded for today."


def list_habits() -> str:
    """List habits and streaks."""
    habits = store.habits()
    if not habits:
        return "No habits tracked yet."
    return "\n".join(f"- {name}: {streak}-day streak (#{hid})" for hid, name, streak in habits)
