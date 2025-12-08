"""Majordomo orchestrator factory."""

from typing import Iterable

from google.adk.agents import Agent
from google.adk.tools import AgentTool

from ..prompts import MAJORDOMO_PROMPT


def create_majordomo_agent(sub_agents: Iterable[Agent]) -> Agent:
    """Create the root Majordomo agent with wrapped sub-agents."""
    tools = [AgentTool(agent) for agent in sub_agents]
    return Agent(
        name="majordomo",
        model="gemini-2.5-flash",
        description="Root orchestrator that delegates to specialists.",
        instruction=MAJORDOMO_PROMPT,
        tools=tools,
    )
