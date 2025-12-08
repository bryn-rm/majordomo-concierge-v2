"""Chart generation utilities (text-only fallback)."""

from __future__ import annotations

from typing import Dict

try:
    import matplotlib.pyplot as plt  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    plt = None


def spending_bar_chart(data: Dict[str, float], output_path: str) -> str:
    """Render a simple bar chart if matplotlib is available."""
    if not plt:
        return "matplotlib not installed; skipping chart generation."
    labels = list(data.keys())
    values = list(data.values())
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title("Monthly spend by category")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return f"Chart saved to {output_path}"
