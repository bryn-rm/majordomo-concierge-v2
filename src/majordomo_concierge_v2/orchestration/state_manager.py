"""Shared state coordinator for multi-agent workflows."""

from __future__ import annotations

from typing import Any, Dict


class StateManager:
    """Mutable state shared across agent calls."""

    def __init__(self):
        self.state: Dict[str, Any] = {}

    def get(self, key: str, default=None):
        return self.state.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.state[key] = value

    def to_dict(self) -> Dict[str, Any]:
        return dict(self.state)
