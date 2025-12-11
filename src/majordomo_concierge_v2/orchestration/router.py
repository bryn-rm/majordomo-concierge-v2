"""Intent router that points to the right specialist agent."""

from __future__ import annotations

import re


def route_intent(message: str) -> str:
    """Heuristic routing: research→oracle, memory→scribe, finance→comptroller, docs→archivist, lifestyle→concierge, smart-home→sentinel, tasks→taskmaster."""
    text = message.lower()
    if any(word in text for word in ["spend", "expense", "budget", "bill"]):
        return "comptroller"
    if any(word in text for word in ["journal", "remember", "note", "memory"]):
        return "scribe"
    if any(word in text for word in ["task", "todo", "habit", "briefing"]):
        return "taskmaster"
    if any(word in text for word in ["recipe", "dinner", "meal", "restaurant"]):
        return "concierge"
    if any(word in text for word in ["document", "file", "drive", "knowledge"]):
        return "archivist"
    if any(word in text for word in ["light", "thermostat", "smart", "home"]):
        return "sentinel"
    if re.search(r"news|latest|search|who|what|when|where|why|how", text):
        return "oracle"
    return "majordomo"
