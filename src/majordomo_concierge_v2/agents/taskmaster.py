"""Taskmaster agent factory."""

from google.adk.agents import Agent

from ..agents.base import wrap_functions
from ..prompts import TASKMASTER_PROMPT
from ..tools.local import (
    add_task,
    complete_task,
    upcoming,
    add_habit,
    complete_habit,
    list_habits,
)
from ..orchestration.workflow_builder import build_morning_briefing


def create_taskmaster_agent() -> Agent:
    """Build the productivity agent."""
    tools = wrap_functions(
        [
            add_task,
            complete_task,
            upcoming,
            add_habit,
            complete_habit,
            list_habits,
            build_morning_briefing,
        ]
    )
    return Agent(
        name="taskmaster",
        model="gemini-2.5-flash-lite",
        description="Manages tasks, habits, and daily briefings.",
        instruction=TASKMASTER_PROMPT,
        tools=tools,
    )
