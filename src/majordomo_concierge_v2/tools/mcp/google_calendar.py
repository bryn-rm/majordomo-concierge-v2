"""Google Calendar MCP integration with OAuth env passthrough."""

from __future__ import annotations

import os
import shutil
from typing import Optional

try:
    from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
    from mcp import StdioServerParameters
except Exception:  # pragma: no cover - optional dependency
    MCPToolset = None  # type: ignore
    StdioServerParameters = None  # type: ignore
    StdioConnectionParams = None  # type: ignore


REQUIRED_ENV = ["GOOGLE_CALENDAR_CLIENT_ID", "GOOGLE_CALENDAR_CLIENT_SECRET", "GOOGLE_CALENDAR_REFRESH_TOKEN"]


def _missing_env() -> list[str]:
    return [key for key in REQUIRED_ENV if not os.getenv(key)]


def create_calendar_toolset() -> Optional["MCPToolset"]:
    """Return a configured MCP toolset if dependencies and OAuth env are available."""
    if not MCPToolset or not StdioServerParameters or not StdioConnectionParams:
        return None
    if not shutil.which("npx"):
        raise RuntimeError("npx is required for Google Calendar MCP. Install Node.js/npx to enable this tool.")
    missing = _missing_env()
    if missing:
        raise RuntimeError(f"Missing Google OAuth env vars for Calendar MCP: {', '.join(missing)}")

    server = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-google-calendar"],
        env={
            "GOOGLE_CALENDAR_CLIENT_ID": os.getenv("GOOGLE_CALENDAR_CLIENT_ID", ""),
            "GOOGLE_CALENDAR_CLIENT_SECRET": os.getenv("GOOGLE_CALENDAR_CLIENT_SECRET", ""),
            "GOOGLE_CALENDAR_REFRESH_TOKEN": os.getenv("GOOGLE_CALENDAR_REFRESH_TOKEN", ""),
        },
    )
    return MCPToolset(connection_params=StdioConnectionParams(server_params=server, timeout=10.0))
