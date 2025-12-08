"""Semantic memory search helpers."""

from __future__ import annotations

from typing import Dict, Optional

from ...memory.vector_store import VectorStore

vector_store = VectorStore()


def index_memory(memory_id: str, content: str, metadata: Optional[Dict[str, str]] = None) -> str:
    """Add text to the vector store."""
    vector_store.add(memory_id, content, metadata)
    return f"Indexed memory '{memory_id}'."


def search_memory(query: str, limit: int = 5) -> str:
    """Search semantic memory and return a formatted string."""
    results = vector_store.search(query, k=limit)
    if not results:
        return "No similar memories found."
    lines = []
    for item in results:
        lines.append(f"- {item.get('id')}: {item.get('text')}")
    return "\n".join(lines)
