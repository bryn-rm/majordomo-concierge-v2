"""ADK entrypoint defining the root agent."""

from __future__ import annotations

import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # Fallback simple loader if python-dotenv is unavailable
    def load_dotenv(path=None):
        path = Path(path) if path else Path(".env")
        if not path.exists():
            return False
        for line in path.read_text().splitlines():
            if not line or line.strip().startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())
        return True

from google.adk.agents import Agent, ParallelAgent  # noqa: F401
from google.adk.tools import AgentTool

# Ensure local src package is importable when running from repo root without installation.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Load environment variables from project root or majordomo_agent/.env
ENV_PATHS = [PROJECT_ROOT / ".env", Path(__file__).parent / ".env"]
for env_path in ENV_PATHS:
    if env_path.exists():
        load_dotenv(env_path, override=True)

missing_keys = [key for key in ("GOOGLE_API_KEY", "BRAVE_API_KEY") if not os.getenv(key)]
if missing_keys:
    raise RuntimeError(
        f"Missing required environment variables: {', '.join(missing_keys)}. "
        "Populate them in .env at project root or majordomo_agent/.env."
    )

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

# Instantiate specialist agents
oracle_agent = create_oracle_agent()
scribe_agent = create_scribe_agent()
comptroller_agent = create_comptroller_agent()
archivist_agent = create_archivist_agent()
concierge_agent = create_concierge_agent()
sentinel_agent = create_sentinel_agent()
taskmaster_agent = create_taskmaster_agent(
    delegate_agents=[oracle_agent, scribe_agent, comptroller_agent]
)

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
