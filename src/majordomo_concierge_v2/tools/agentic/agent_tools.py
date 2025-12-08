"""Helpers for wrapping agents as tools."""

from google.adk.agents import Agent
from google.adk.tools import AgentTool


def wrap_agent(agent: Agent) -> AgentTool:
    """Return an AgentTool for a given sub-agent."""
    return AgentTool(agent)
