"""User profile storage backed by SQLite preferences table."""

from __future__ import annotations

from typing import Dict, Optional

from .db_manager import DatabaseManager
from .. import JOURNAL_DB


class ProfileStore:
    """Stores simple key/value preferences."""

    def __init__(self, db_path=JOURNAL_DB):
        self.db = DatabaseManager(db_path)

    def set(self, key: str, value: str) -> None:
        """Persist a preference value."""
        self.db.execute(
            """
            INSERT INTO preferences (key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET
                value=excluded.value,
                updated_at=CURRENT_TIMESTAMP
            """,
            (key, value),
        )

    def get(self, key: str) -> Optional[str]:
        """Fetch a stored preference."""
        row = self.db.fetch_one(
            "SELECT value FROM preferences WHERE key = ?", (key,)
        )
        return row["value"] if row else None

    def all(self) -> Dict[str, str]:
        """Return all preferences."""
        rows = self.db.fetch_all("SELECT key, value FROM preferences")
        return {row["key"]: row["value"] for row in rows}
