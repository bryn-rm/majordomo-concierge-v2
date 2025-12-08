"""Recipe and meal-planning store."""

from __future__ import annotations

from typing import List, Optional, Tuple

from .db_manager import DatabaseManager
from .. import RECIPE_DB


class RecipeStore:
    """Stores recipes and meal plans for the Concierge agent."""

    def __init__(self, db_path=RECIPE_DB):
        self.db = DatabaseManager(db_path)

    def add_recipe(
        self,
        title: str,
        ingredients: str,
        instructions: str,
        tags: Optional[str] = None,
    ) -> int:
        """Insert a recipe row."""
        cursor = self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                instructions TEXT NOT NULL,
                tags TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        cursor = self.db.execute(
            """
            INSERT INTO recipes (title, ingredients, instructions, tags)
            VALUES (?, ?, ?, ?)
            """,
            (title, ingredients, instructions, tags),
        )
        return cursor.lastrowid or 0

    def search(self, keyword: str) -> List[Tuple[str, str]]:
        """Return recipes matching keyword in title or tags."""
        keyword_like = f"%{keyword}%"
        rows = self.db.fetch_all(
            """
            SELECT title, instructions
            FROM recipes
            WHERE title LIKE ? OR tags LIKE ?
            ORDER BY created_at DESC
            """,
            (keyword_like, keyword_like),
        )
        return [(row["title"], row["instructions"]) for row in rows]
