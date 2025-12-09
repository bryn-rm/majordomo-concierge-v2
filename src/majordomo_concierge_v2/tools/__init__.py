"""Tool package exports."""

from .local import (
    remember,
    recall_by_date,
    set_preference,
    get_preference,
    index_memory,
    search_memory,
    log_expense,
    budget_status,
    categorize_expense,
    add_task,
    complete_task,
    upcoming,
    add_habit,
    complete_habit,
    list_habits,
    add_recipe,
    find_recipe,
    add_item,
    remove_item,
    list_items,
    add,
    subtract,
    parse_date,
)
from .agentic import wrap_agent

# MCP integrations are optional at import-time to allow local unit tests to run
# without google-adk installed. In production, google-adk must be installed.
try:  # pragma: no cover - guarded for environments without ADK
    from .mcp import (
        create_brave_search_toolset,
        create_wikipedia_toolset,
        create_calendar_toolset,
        create_drive_toolset,
    )
except Exception:  # pragma: no cover
    create_brave_search_toolset = None  # type: ignore
    create_wikipedia_toolset = None  # type: ignore
    create_calendar_toolset = None  # type: ignore
    create_drive_toolset = None  # type: ignore

__all__ = [
    "create_brave_search_toolset",
    "create_wikipedia_toolset",
    "create_calendar_toolset",
    "create_drive_toolset",
    "remember",
    "recall_by_date",
    "set_preference",
    "get_preference",
    "index_memory",
    "search_memory",
    "log_expense",
    "budget_status",
    "categorize_expense",
    "add_task",
    "complete_task",
    "upcoming",
    "add_habit",
    "complete_habit",
    "list_habits",
    "add_recipe",
    "find_recipe",
    "add_item",
    "remove_item",
    "list_items",
    "add",
    "subtract",
    "parse_date",
    "wrap_agent",
]
