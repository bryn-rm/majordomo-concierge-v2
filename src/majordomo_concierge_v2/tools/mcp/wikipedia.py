"""MCP Wikipedia toolset helper with safety checks."""

import shutil

from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
from mcp import StdioServerParameters


def create_wikipedia_toolset() -> MCPToolset:
    """Create a Wikipedia MCP toolset."""
    if not shutil.which("npx"):
        raise RuntimeError("npx is required for Wikipedia MCP. Install Node.js/npx to enable this tool.")
    server = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-wikipedia"],
    )
    return MCPToolset(connection_params=StdioConnectionParams(server_params=server, timeout=10.0))
