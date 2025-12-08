"""Basic calculator utilities."""

from __future__ import annotations

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> float:
    """Add two numbers."""
    return float(a) + float(b)


def subtract(a: Number, b: Number) -> float:
    """Subtract b from a."""
    return float(a) - float(b)
