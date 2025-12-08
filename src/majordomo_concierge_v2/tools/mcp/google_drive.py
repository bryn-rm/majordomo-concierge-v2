"""Placeholder for Google Drive MCP integration."""

from __future__ import annotations

from typing import Optional

try:
    from google.adk.tools.mcp_tool import MCPToolset, StdioServerParameters
except Exception:  # pragma: no cover - optional dependency
    MCPToolset = None  # type: ignore
    StdioServerParameters = None  # type: ignore


def create_drive_toolset() -> Optional["MCPToolset"]:
    """Return a Drive toolset when the MCP server is available."""
    if not MCPToolset or not StdioServerParameters:
        return None
    return MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-google-drive"],
        )
    )
