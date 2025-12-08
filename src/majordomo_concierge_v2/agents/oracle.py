"""Oracle agent factory."""

from google.adk.agents import Agent

from ..prompts import ORACLE_PROMPT
from ..tools.mcp import create_brave_search_toolset, create_wikipedia_toolset


def create_oracle_agent() -> Agent:
    """Build the information retrieval agent."""
    brave = create_brave_search_toolset()
    wikipedia = create_wikipedia_toolset()
    return Agent(
        name="oracle",
        model="gemini-2.0-flash",
        description="Information retrieval via web search and Wikipedia.",
        instruction=ORACLE_PROMPT,
        tools=[brave, wikipedia],
    )
