"""General text utilities."""

import re
from typing import Iterable


def normalize_text(text: str) -> str:
    """Lowercase and collapse whitespace."""
    return re.sub(r"\s+", " ", text.strip().lower())


def summarize_list(items: Iterable[str], bullet: str = "- ") -> str:
    """Convert an iterable into a simple bullet list string."""
    return "\n".join(f"{bullet}{item}" for item in items)
