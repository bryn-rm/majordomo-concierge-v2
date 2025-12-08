"""Journal CRUD operations exposed as ADK tools."""

from __future__ import annotations

from datetime import date
from typing import List, Optional

from ...memory.journal_store import JournalStore
from ...utils.date_utils import parse_human_date

store = JournalStore()


def remember(content: str, tags: Optional[List[str]] = None, entry_type: str = "note") -> str:
    """Persist a note to the journal."""
    entry_id = store.add_entry(content=content, tags=tags, entry_type=entry_type)
    return f"Stored journal entry {entry_id}."


def recall_by_date(date_phrase: str) -> str:
    """Return journal entries for a given natural-language date."""
    target_date = parse_human_date(date_phrase)
    entries = store.entries_on(target_date)
    if not entries:
        return f"No entries recorded for {target_date.isoformat()}."
    formatted = "\n".join(f"- {etype}: {text}" for _, text, etype in entries)
    return f"Entries for {target_date.isoformat()}:\n{formatted}"


def set_preference(key: str, value: str) -> str:
    """Save a user preference in the journal database."""
    store.set_preference(key, value)
    return f"Preference '{key}' saved."


def get_preference(key: str) -> str:
    """Return a stored preference or a helpful fallback."""
    value = store.get_preference(key)
    return value if value else "No preference found."
