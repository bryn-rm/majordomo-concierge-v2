"""ADK entrypoint defining the root agent."""

from __future__ import annotations

import os

from dotenv import load_dotenv
from google.adk.agents import Agent, ParallelAgent  # noqa: F401
from google.adk.tools import AgentTool
from google.adk.tools.mcp_tool import MCPToolset, StdioServerParameters  # noqa: F401

from majordomo_concierge_v2.agents import (
    create_archivist_agent,
    create_comptroller_agent,
    create_concierge_agent,
    create_majordomo_agent,
    create_oracle_agent,
    create_sentinel_agent,
    create_scribe_agent,
    create_taskmaster_agent,
)

load_dotenv()

# Instantiate specialist agents
oracle_agent = create_oracle_agent()
scribe_agent = create_scribe_agent()
comptroller_agent = create_comptroller_agent()
archivist_agent = create_archivist_agent()
concierge_agent = create_concierge_agent()
sentinel_agent = create_sentinel_agent()
taskmaster_agent = create_taskmaster_agent()

# Root agent (MUST be named root_agent)
root_agent: Agent = create_majordomo_agent(
    [
        oracle_agent,
        scribe_agent,
        comptroller_agent,
        archivist_agent,
        concierge_agent,
        sentinel_agent,
        taskmaster_agent,
    ]
)
