"""Document and knowledge helpers for the Archivist agent."""

from __future__ import annotations

from typing import Optional

from ...memory.vector_store import VectorStore
from ...utils.text_processing import normalize_text

vector_store = VectorStore(collection_name="documents")


def store_document(doc_id: str, content: str, tags: Optional[str] = None) -> str:
    """Index a document for later retrieval."""
    metadata = {"tags": tags or "", "id": doc_id}
    vector_store.add(doc_id, content, metadata)
    return f"Stored document '{doc_id}' with tags '{tags or ''}'."


def search_documents(query: str, limit: int = 5) -> str:
    """Search indexed documents by semantic similarity."""
    results = vector_store.search(normalize_text(query), k=limit)
    if not results:
        return "No documents matched."
    lines = []
    for item in results:
        lines.append(f"- {item.get('id')}: {item.get('text')[:160]}...")
    return "\n".join(lines)
