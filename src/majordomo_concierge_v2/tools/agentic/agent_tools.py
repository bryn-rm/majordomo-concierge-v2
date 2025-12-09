"""Helpers for wrapping agents as tools."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from google.adk.agents import Agent
    from google.adk.tools import AgentTool


def wrap_agent(agent: "Agent"):
    """Return an AgentTool for a given sub-agent."""
    from google.adk.tools import AgentTool

    return AgentTool(agent)
