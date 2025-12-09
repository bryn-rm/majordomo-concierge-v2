"""Lightweight safe Python evaluator for calculations."""

from __future__ import annotations

import ast
import operator
from typing import Any, Dict

# Whitelist of safe operators
_OPS: Dict[type, Any] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


def _eval(node: ast.AST) -> Any:
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.operand))
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
    raise ValueError("Unsupported expression")


def evaluate_expression(expression: str) -> str:
    """Safely evaluate a simple Python arithmetic expression."""
    try:
        parsed = ast.parse(expression, mode="eval")
        result = _eval(parsed.body)
        return str(result)
    except Exception as exc:
        return f"Error evaluating expression: {exc}"
