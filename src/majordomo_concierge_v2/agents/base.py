"""Common helpers for creating ADK agents."""

from __future__ import annotations

from typing import Callable, Iterable

from google.adk.tools import FunctionTool


def wrap_functions(funcs: Iterable[Callable[..., object]]):
    """Wrap callables with FunctionTool for ADK."""
    return [FunctionTool(func) for func in funcs]
