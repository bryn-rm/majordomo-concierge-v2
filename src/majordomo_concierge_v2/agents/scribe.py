"""Scribe agent factory."""

from google.adk.agents import Agent

from ..prompts import SCRIBE_PROMPT
from ..agents.base import wrap_functions
from ..tools.local import (
    remember,
    recall_by_date,
    set_preference,
    get_preference,
    parse_date,
    log_turn,
    recent_history,
)


def create_scribe_agent() -> Agent:
    """Build the memory and calendar agent."""
    tools = wrap_functions(
        [
            remember,
            recall_by_date,
            set_preference,
            get_preference,
            parse_date,
            log_turn,
            recent_history,
        ]
    )
    return Agent(
        name="scribe",
        model="gemini-2.5-flash",
        description="Stores and recalls memories, preferences, calendar, and conversation history.",
        instruction=SCRIBE_PROMPT,
        tools=tools,
    )
