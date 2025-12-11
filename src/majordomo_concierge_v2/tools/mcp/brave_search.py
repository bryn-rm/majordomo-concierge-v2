"""MCP Brave Search toolset helper with safety checks."""

from __future__ import annotations

import os
import shutil

from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
from mcp import StdioServerParameters


def create_brave_search_toolset() -> MCPToolset:
    """Create a Brave Search MCP toolset or raise a clear error."""
    if not shutil.which("npx"):
        raise RuntimeError("npx is required for Brave MCP. Install Node.js/npx to enable web search.")
    api_key = os.getenv("BRAVE_API_KEY", "")
    if not api_key:
        raise RuntimeError("BRAVE_API_KEY is not set. Add it to your environment to enable Brave search.")
    server = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-brave-search"],
        env={"BRAVE_API_KEY": api_key},
    )
    return MCPToolset(connection_params=StdioConnectionParams(server_params=server, timeout=10.0))
