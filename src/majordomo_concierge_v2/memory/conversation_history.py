"""Conversation history store backed by SQLite."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable, List, Tuple

from .db_manager import DatabaseManager
from .. import JOURNAL_DB

CONVERSATION_SCHEMA = """
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


class ConversationHistory:
    """Persists conversation turns for recall by Scribe and Majordomo."""

    def __init__(self, db_path=JOURNAL_DB):
        self.db = DatabaseManager(db_path)
        self.db.executescript(CONVERSATION_SCHEMA)

    def log(self, role: str, content: str) -> None:
        """Record a conversation turn."""
        self.db.execute(
            """
            INSERT INTO conversations (role, content, timestamp)
            VALUES (?, ?, ?)
            """,
            (role, content, datetime.now(timezone.utc).isoformat()),
        )

    def recent(self, limit: int = 20) -> List[Tuple[str, str]]:
        """Return the most recent conversation entries."""
        rows = self.db.fetch_all(
            """
            SELECT role, content
            FROM conversations
            ORDER BY timestamp DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [(row["role"], row["content"]) for row in rows]

    def by_date(self, date_str: str) -> List[Tuple[str, str]]:
        """Return all messages on a given date (YYYY-MM-DD)."""
        rows = self.db.fetch_all(
            """
            SELECT role, content
            FROM conversations
            WHERE DATE(timestamp) = DATE(?)
            ORDER BY timestamp ASC
            """,
            (date_str,),
        )
        return [(row["role"], row["content"]) for row in rows]
