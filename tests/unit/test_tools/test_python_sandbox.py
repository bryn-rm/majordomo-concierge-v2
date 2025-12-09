"""Tests for the safe Python evaluator."""

from majordomo_concierge_v2.tools.local.python_sandbox import evaluate_expression


def test_evaluate_expression_simple_math():
    assert evaluate_expression("2 + 3 * 4") == "14"


def test_evaluate_expression_rejects_bad_input():
    assert "Unsupported" in evaluate_expression("__import__('os').system('ls')")
