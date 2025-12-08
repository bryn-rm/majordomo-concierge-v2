"""Expose date parsing as a tool-friendly function."""

from __future__ import annotations

from datetime import date

from ...utils.date_utils import parse_human_date


def parse_date(phrase: str) -> str:
    """Parse a human-friendly date phrase and return ISO string."""
    parsed: date = parse_human_date(phrase)
    return parsed.isoformat()
