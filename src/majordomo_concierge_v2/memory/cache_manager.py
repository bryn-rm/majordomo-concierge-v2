"""Simple in-memory response cache with TTL support."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class CacheEntry:
    value: Any
    expires_at: float


class CacheManager:
    """Lightweight cache for tool responses to control API spend."""

    def __init__(self, default_ttl: int = 300):
        self.default_ttl = default_ttl
        self._entries: Dict[str, CacheEntry] = {}

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a cached value if not expired."""
        entry = self._entries.get(key)
        if not entry:
            return None
        if entry.expires_at < time.time():
            self._entries.pop(key, None)
            return None
        return entry.value

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Store a value with optional TTL override."""
        expires_in = ttl if ttl is not None else self.default_ttl
        self._entries[key] = CacheEntry(value=value, expires_at=time.time() + expires_in)

    def clear(self) -> None:
        """Empty the cache."""
        self._entries.clear()
