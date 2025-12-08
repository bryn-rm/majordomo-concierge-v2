"""Lightweight vector store wrapper for semantic memory."""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from .. import DATA_DIR

logger = logging.getLogger(__name__)


class InMemoryVectorStore:
    """Fallback semantic store when chromadb is unavailable."""

    def __init__(self):
        self.documents: list[dict[str, Any]] = []

    def add(self, doc_id: str, text: str, metadata: Optional[Dict[str, Any]] = None):
        self.documents.append({"id": doc_id, "text": text, "metadata": metadata or {}})

    def similarity_search(self, query: str, k: int = 5) -> List[dict]:
        """Naive similarity using substring overlap."""
        scored = []
        for doc in self.documents:
            score = self._overlap_score(query.lower(), doc["text"].lower())
            scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in scored[:k] if score > 0]

    @staticmethod
    def _overlap_score(query: str, text: str) -> int:
        return sum(1 for token in query.split() if token in text)


class VectorStore:
    """Wrapper around ChromaDB with an in-memory fallback."""

    def __init__(self, collection_name: str = "memory"):
        self.collection_name = collection_name
        self._client = None
        self._collection = None
        self._fallback = InMemoryVectorStore()

        try:
            import chromadb  # type: ignore

            self._client = chromadb.PersistentClient(path=str(DATA_DIR / "vector_store"))
            self._collection = self._client.get_or_create_collection(collection_name)
        except Exception as exc:  # pragma: no cover - optional dependency
            logger.warning("Falling back to in-memory vector store: %s", exc)
            self._client = None

    def add(self, doc_id: str, text: str, metadata: Optional[Dict[str, Any]] = None):
        """Add text to the vector store."""
        metadata = metadata or {}
        if self._collection:
            self._collection.add(documents=[text], ids=[doc_id], metadatas=[metadata])
        else:
            self._fallback.add(doc_id, text, metadata)

    def search(self, query: str, k: int = 5) -> List[dict]:
        """Perform similarity search."""
        if self._collection:
            results = self._collection.query(query_texts=[query], n_results=k)
            docs = []
            for idx, doc_id in enumerate(results.get("ids", [[]])[0]):
                docs.append(
                    {
                        "id": doc_id,
                        "text": results.get("documents", [[]])[0][idx],
                        "metadata": results.get("metadatas", [[]])[0][idx],
                        "score": results.get("distances", [[]])[0][idx]
                        if "distances" in results
                        else None,
                    }
                )
            return docs
        return self._fallback.similarity_search(query, k=k)
