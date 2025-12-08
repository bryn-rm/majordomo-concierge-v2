"""Archivist agent factory."""

from google.adk.agents import Agent

from ..agents.base import wrap_functions
from ..prompts import ARCHIVIST_PROMPT
from ..tools.local import index_memory, search_memory


def create_archivist_agent() -> Agent:
    """Build the document/knowledge agent."""
    tools = wrap_functions([index_memory, search_memory])
    return Agent(
        name="archivist",
        model="gemini-2.0-flash",
        description="Organizes documents and answers knowledge-base questions.",
        instruction=ARCHIVIST_PROMPT,
        tools=tools,
    )
