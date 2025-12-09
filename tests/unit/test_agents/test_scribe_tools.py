"""Unit checks for scribe helpers."""

from majordomo_concierge_v2.tools.local.conversation_tools import log_turn, recent_history


def test_conversation_logging_roundtrip():
    log_turn("user", "hello world")
    history = recent_history(1)
    assert "hello world" in history
