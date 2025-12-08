"""Date parsing and formatting helpers."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Optional

WEEKDAYS = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}


def parse_human_date(value: str, *, today: Optional[date] = None) -> date:
    """Parse simple natural language dates like 'last Wednesday' or 'yesterday'."""
    today = today or date.today()
    normalized = value.strip().lower()

    if normalized in {"today", "tonight"}:
        return today
    if normalized in {"yesterday", "last day"}:
        return today - timedelta(days=1)
    if normalized == "tomorrow":
        return today + timedelta(days=1)

    if normalized.startswith("last "):
        weekday_name = normalized.replace("last ", "").strip()
        if weekday_name in WEEKDAYS:
            target_weekday = WEEKDAYS[weekday_name]
            delta = (today.weekday() - target_weekday) % 7 or 7
            return today - timedelta(days=delta)

    # Try ISO format first
    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    # Try common date formats
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue

    raise ValueError(f"Unable to parse date from '{value}'.")


def days_remaining_in_month(today: Optional[date] = None) -> int:
    """Return number of days left in the current month including today."""
    today = today or date.today()
    next_month = today.replace(day=28) + timedelta(days=4)
    last_day = next_month - timedelta(days=next_month.day)
    return (last_day - today).days + 1


def format_date(value: date) -> str:
    """Format a date as YYYY-MM-DD string."""
    return value.isoformat()
