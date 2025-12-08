"""MCP Brave Search toolset helper."""

from __future__ import annotations

import os

from google.adk.tools.mcp_tool import MCPToolset, StdioServerParameters


def create_brave_search_toolset() -> MCPToolset:
    """Create a Brave Search MCP toolset."""
    return MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-brave-search"],
            env={"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY", "")},
        ),
    )
