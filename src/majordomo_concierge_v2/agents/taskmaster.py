"""Taskmaster agent factory."""

from typing import Iterable, Optional

from google.adk.agents import Agent
from google.adk.tools import AgentTool

from ..agents.base import wrap_functions
from ..prompts import TASKMASTER_PROMPT
from ..tools.local import (
    add_task,
    complete_task,
    upcoming,
    list_tasks,
    add_habit,
    complete_habit,
    list_habits,
)
from ..orchestration.workflow_builder import build_morning_briefing


def create_taskmaster_agent(
    *,
    delegate_agents: Optional[Iterable[Agent]] = None,
) -> Agent:
    """Build the productivity agent with optional delegation tools."""
    tools = wrap_functions(
        [
            add_task,
            complete_task,
            upcoming,
            list_tasks,
            add_habit,
            complete_habit,
            list_habits,
            build_morning_briefing,
        ]
    )

    if delegate_agents:
        tools.extend(AgentTool(agent) for agent in delegate_agents)

    return Agent(
        name="taskmaster",
        model="gemini-2.5-flash-lite",
        description="Manages tasks, habits, and daily briefings. Delegates to oracle/scribe/comptroller when needed.",
        instruction=TASKMASTER_PROMPT,
        tools=tools,
    )
