"""Journal and preference persistence for Scribe."""

from __future__ import annotations

from datetime import date
from typing import List, Optional, Tuple

from .db_manager import DatabaseManager
from .. import JOURNAL_DB

JOURNAL_SCHEMA = """
CREATE TABLE IF NOT EXISTS journal_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    entry_type TEXT DEFAULT 'note',
    tags TEXT,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS preferences (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


class JournalStore:
    """CRUD operations for journal entries and preferences."""

    def __init__(self, db_path=JOURNAL_DB):
        self.db = DatabaseManager(db_path)
        self.db.executescript(JOURNAL_SCHEMA)

    def add_entry(
        self,
        content: str,
        entry_type: str = "note",
        tags: Optional[list[str]] = None,
        entry_date: Optional[date] = None,
    ) -> int:
        """Create a journal entry and return its row id."""
        tag_str = ",".join(tags) if tags else None
        entry_date = entry_date or date.today()
        cursor = self.db.execute(
            """
            INSERT INTO journal_entries (content, entry_type, tags, date)
            VALUES (?, ?, ?, ?)
            """,
            (content, entry_type, tag_str, entry_date.isoformat()),
        )
        return cursor.lastrowid or 0

    def entries_on(self, entry_date: date) -> List[Tuple[int, str, str]]:
        """Fetch entries for a given date."""
        rows = self.db.fetch_all(
            """
            SELECT id, content, entry_type
            FROM journal_entries
            WHERE date = DATE(?)
            ORDER BY created_at ASC
            """,
            (entry_date.isoformat(),),
        )
        return [(row["id"], row["content"], row["entry_type"]) for row in rows]

    def search(self, keyword: str) -> List[Tuple[int, str, str]]:
        """Search entries by keyword."""
        like = f"%{keyword}%"
        rows = self.db.fetch_all(
            """
            SELECT id, content, entry_type
            FROM journal_entries
            WHERE content LIKE ? OR tags LIKE ?
            ORDER BY created_at DESC
            """,
            (like, like),
        )
        return [(row["id"], row["content"], row["entry_type"]) for row in rows]

    def set_preference(self, key: str, value: str) -> None:
        """Upsert a user preference."""
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

    def get_preference(self, key: str) -> Optional[str]:
        """Return a preference by key."""
        row = self.db.fetch_one(
            "SELECT value FROM preferences WHERE key = ?", (key,)
        )
        return row["value"] if row else None
