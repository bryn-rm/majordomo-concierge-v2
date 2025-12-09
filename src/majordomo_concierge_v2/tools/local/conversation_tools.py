"""Conversation logging helpers for Scribe."""

from __future__ import annotations

from ...memory.conversation_history import ConversationHistory

history = ConversationHistory()


def log_turn(role: str, content: str) -> str:
    """Persist a conversation turn."""
    history.log(role, content)
    return "Logged conversation turn."


def recent_history(limit: int = 10) -> str:
    """Return the latest conversation turns."""
    rows = history.recent(limit)
    if not rows:
        return "No conversation history yet."
    return "\n".join(f"- {role}: {text}" for role, text in rows)
