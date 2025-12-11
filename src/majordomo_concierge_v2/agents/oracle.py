"""Oracle agent factory."""

from google.adk.agents import Agent

from ..prompts import ORACLE_PROMPT
from ..tools.mcp import create_brave_search_toolset, create_wikipedia_toolset


def create_oracle_agent() -> Agent:
    """Build the information retrieval agent."""
    tools = []
    try:
        tools.append(create_brave_search_toolset())
    except Exception as exc:
        tools.append(None)
        print(f"[oracle] Brave MCP unavailable: {exc}")
    try:
        tools.append(create_wikipedia_toolset())
    except Exception as exc:
        tools.append(None)
        print(f"[oracle] Wikipedia MCP unavailable: {exc}")
    tools = [t for t in tools if t is not None]
    return Agent(
        name="oracle",
        model="gemini-2.0-flash",
        description="Information retrieval via web search and Wikipedia.",
        instruction=ORACLE_PROMPT,
        tools=tools,
    )
