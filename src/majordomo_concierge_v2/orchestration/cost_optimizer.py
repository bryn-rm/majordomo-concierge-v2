"""Cost controls to stay within free tier limits."""

from __future__ import annotations

from ..memory.cache_manager import CacheManager

cache = CacheManager(default_ttl=600)


def cached_response(key: str):
    """Return a cached response if available."""
    return cache.get(key)


def remember_response(key: str, value: str) -> None:
    """Store a response in cache."""
    cache.set(key, value)
