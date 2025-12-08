"""MCP Wikipedia toolset helper."""

from google.adk.tools.mcp_tool import MCPToolset, StdioServerParameters


def create_wikipedia_toolset() -> MCPToolset:
    """Create a Wikipedia MCP toolset."""
    return MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-wikipedia"],
        )
    )
