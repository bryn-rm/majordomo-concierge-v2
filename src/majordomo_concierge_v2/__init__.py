"""Majordomo Concierge V2 package initialization."""

from pathlib import Path

# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "databases"

# SQLite database filenames
JOURNAL_DB = DATA_DIR / "journal.db"
FINANCE_DB = DATA_DIR / "finance.db"
TASK_DB = DATA_DIR / "tasks.db"
RECIPE_DB = DATA_DIR / "recipes.db"

__all__ = [
    "PROJECT_ROOT",
    "DATA_DIR",
    "JOURNAL_DB",
    "FINANCE_DB",
    "TASK_DB",
    "RECIPE_DB",
]
