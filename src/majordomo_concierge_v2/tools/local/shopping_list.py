"""Simple shopping list manager stored on disk."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from ... import DATA_DIR

LIST_PATH = DATA_DIR / "shopping_list.json"


def _load() -> List[str]:
    if LIST_PATH.exists():
        try:
            return json.loads(LIST_PATH.read_text())
        except Exception:
            return []
    return []


def _save(items: List[str]) -> None:
    LIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    LIST_PATH.write_text(json.dumps(items, indent=2))


def add_item(item: str) -> str:
    """Add an item to the shopping list."""
    items = _load()
    items.append(item)
    _save(items)
    return f"Added '{item}' to shopping list."


def remove_item(item: str) -> str:
    """Remove an item from the shopping list if present."""
    items = _load()
    if item in items:
        items.remove(item)
        _save(items)
        return f"Removed '{item}'."
    return f"Item '{item}' not found."


def list_items() -> str:
    """Return current shopping list."""
    items = _load()
    if not items:
        return "Shopping list is empty."
    return "\n".join(f"- {item}" for item in items)
