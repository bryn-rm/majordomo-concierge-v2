"""Finance persistence layer for Comptroller agent."""

from __future__ import annotations

from datetime import date
from typing import Dict, List, Optional, Tuple

from .db_manager import DatabaseManager
from .. import FINANCE_DB


class FinanceStore:
    """Handles expenses and budgets in SQLite."""

    def __init__(self, db_path=FINANCE_DB):
        self.db = DatabaseManager(db_path)

    def add_expense(
        self, amount: float, description: str, category: str, when: Optional[date] = None
    ) -> int:
        """Insert an expense row and return its id."""
        when = when or date.today()
        cursor = self.db.execute(
            """
            INSERT INTO expenses (amount, description, category, date)
            VALUES (?, ?, ?, ?)
            """,
            (amount, description, category, when.isoformat()),
        )
        return cursor.lastrowid or 0

    def recent(self, limit: int = 10) -> List[Tuple[str, float, str]]:
        """Fetch recent expenses."""
        rows = self.db.fetch_all(
            """
            SELECT description, amount, category
            FROM expenses
            ORDER BY date DESC, created_at DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [(row["description"], row["amount"], row["category"]) for row in rows]

    def upsert_budget(self, category: str, monthly_limit: float) -> None:
        """Create or update a budget limit for a category."""
        self.db.execute(
            """
            INSERT INTO budgets (category, monthly_limit)
            VALUES (?, ?)
            ON CONFLICT(category) DO UPDATE SET
                monthly_limit=excluded.monthly_limit,
                updated_at=CURRENT_TIMESTAMP
            """,
            (category, monthly_limit),
        )

    def get_budget(self, category: str) -> Optional[float]:
        """Return monthly limit for a category if present."""
        row = self.db.fetch_one(
            "SELECT monthly_limit FROM budgets WHERE category = ?", (category,)
        )
        return float(row["monthly_limit"]) if row else None

    def spend_this_month(self, category: Optional[str] = None) -> float:
        """Calculate spend for current month optionally filtered by category."""
        params = []
        category_clause = ""
        if category:
            category_clause = "AND category = ?"
            params.append(category)
        rows = self.db.fetch_one(
            f"""
            SELECT COALESCE(SUM(amount), 0) AS total
            FROM expenses
            WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
            {category_clause}
            """,
            tuple(params),
        )
        return float(rows["total"]) if rows else 0.0

    def monthly_spend_by_category(self) -> Dict[str, float]:
        """Return current month spend broken down by category."""
        rows = self.db.fetch_all(
            """
            SELECT category, COALESCE(SUM(amount), 0) AS total
            FROM expenses
            WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
            GROUP BY category
            ORDER BY total DESC
            """
        )
        return {row["category"]: float(row["total"]) for row in rows}
