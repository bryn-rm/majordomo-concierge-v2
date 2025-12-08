"""Concierge agent factory."""

from google.adk.agents import Agent

from ..agents.base import wrap_functions
from ..prompts import CONCIERGE_PROMPT
from ..tools.local import add_recipe, find_recipe, add_item, remove_item, list_items


def create_concierge_agent() -> Agent:
    """Build the lifestyle agent."""
    tools = wrap_functions([add_recipe, find_recipe, add_item, remove_item, list_items])
    return Agent(
        name="concierge",
        model="gemini-2.0-flash",
        description="Provides recipes, recommendations, and shopping support.",
        instruction=CONCIERGE_PROMPT,
        tools=tools,
    )
