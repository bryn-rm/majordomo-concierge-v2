"""Productivity data store for tasks and habits."""

from __future__ import annotations

from datetime import date
from typing import List, Optional, Tuple

from .db_manager import DatabaseManager
from .. import TASK_DB


class TaskStore:
    """Handles todo items and habit tracking."""

    def __init__(self, db_path=TASK_DB):
        self.db = DatabaseManager(db_path)

    def add_task(
        self,
        title: str,
        description: str = "",
        priority: str = "medium",
        status: str = "todo",
        due_date: Optional[date] = None,
    ) -> int:
        """Create a task and return its id."""
        cursor = self.db.execute(
            """
            INSERT INTO tasks (title, description, priority, status, due_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, description, priority, status, due_date.isoformat() if due_date else None),
        )
        return cursor.lastrowid or 0

    def update_status(self, task_id: int, status: str) -> None:
        """Update status of a task."""
        self.db.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (status, task_id),
        )

    def upcoming(self, limit: int = 5) -> List[Tuple[int, str, str, Optional[str]]]:
        """Return upcoming tasks ordered by due date."""
        rows = self.db.fetch_all(
            """
            SELECT id, title, priority, due_date
            FROM tasks
            WHERE status != 'done'
            ORDER BY COALESCE(due_date, date('now')) ASC, priority DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [(row["id"], row["title"], row["priority"], row["due_date"]) for row in rows]

    def add_habit(
        self, name: str, frequency: str = "daily", current_streak: int = 0
    ) -> int:
        """Insert a habit row."""
        cursor = self.db.execute(
            """
            INSERT INTO habits (name, frequency, current_streak)
            VALUES (?, ?, ?)
            """,
            (name, frequency, current_streak),
        )
        return cursor.lastrowid or 0

    def complete_habit(self, habit_id: int) -> None:
        """Mark a habit done for today and increment streak."""
        self.db.execute(
            """
            UPDATE habits
            SET current_streak = current_streak + 1,
                last_completed = DATE('now')
            WHERE id = ?
            """,
            (habit_id,),
        )

    def habits(self) -> List[Tuple[int, str, int]]:
        """Return all habits with streaks."""
        rows = self.db.fetch_all(
            "SELECT id, name, current_streak FROM habits ORDER BY current_streak DESC"
        )
        return [(row["id"], row["name"], row["current_streak"]) for row in rows]
