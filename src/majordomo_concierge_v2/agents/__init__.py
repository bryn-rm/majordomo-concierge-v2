"""Agent factories."""

from .majordomo import create_majordomo_agent
from .oracle import create_oracle_agent
from .scribe import create_scribe_agent
from .comptroller import create_comptroller_agent
from .archivist import create_archivist_agent
from .concierge import create_concierge_agent
from .sentinel import create_sentinel_agent
from .taskmaster import create_taskmaster_agent

__all__ = [
    "create_majordomo_agent",
    "create_oracle_agent",
    "create_scribe_agent",
    "create_comptroller_agent",
    "create_archivist_agent",
    "create_concierge_agent",
    "create_sentinel_agent",
    "create_taskmaster_agent",
]
