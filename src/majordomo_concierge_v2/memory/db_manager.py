"""Shared SQLite database utilities."""

from __future__ import annotations

import logging
import sqlite3
from pathlib import Path
from typing import Iterable, Optional

logger = logging.getLogger(__name__)


class DatabaseManager:
    """Lightweight helper around sqlite3 with safe defaults."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self) -> sqlite3.Connection:
        """Create a connection with row factory enabled."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def execute(
        self,
        query: str,
        params: Iterable | tuple | dict | None = None,
        many: bool = False,
    ):
        """Execute a statement and commit automatically."""
        params = params or ()
        with self.connect() as conn:
            cursor = conn.cursor()
            if many:
                cursor.executemany(query, params)  # type: ignore[arg-type]
            else:
                cursor.execute(query, params)  # type: ignore[arg-type]
            conn.commit()
            return cursor

    def executescript(self, script: str) -> None:
        """Execute a multi-statement SQL script."""
        with self.connect() as conn:
            conn.executescript(script)
            conn.commit()

    def fetch_all(
        self, query: str, params: Iterable | tuple | dict | None = None
    ) -> list[sqlite3.Row]:
        """Run a query and return all rows."""
        params = params or ()
        cursor = self.execute(query, params=params)
        return cursor.fetchall()

    def fetch_one(
        self, query: str, params: Iterable | tuple | dict | None = None
    ) -> Optional[sqlite3.Row]:
        """Run a query and return a single row."""
        params = params or ()
        cursor = self.execute(query, params=params)
        return cursor.fetchone()
