"""Comptroller agent factory."""

from google.adk.agents import Agent

from ..agents.base import wrap_functions
from ..prompts import COMPTROLLER_PROMPT
from ..tools.local import (
    log_expense,
    budget_status,
    categorize_expense,
    monthly_summary,
    evaluate_expression,
)


def create_comptroller_agent() -> Agent:
    """Build the finance agent."""
    tools = wrap_functions(
        [
            log_expense,
            budget_status,
            categorize_expense,
            monthly_summary,
            evaluate_expression,
        ]
    )
    return Agent(
        name="comptroller",
        model="gemini-2.5-flash",
        description="Tracks expenses, budgets, and spending alerts.",
        instruction=COMPTROLLER_PROMPT,
        tools=tools,
    )
