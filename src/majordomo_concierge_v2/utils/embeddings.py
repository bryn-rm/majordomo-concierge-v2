"""Simple embedding helper."""

from __future__ import annotations

import hashlib
from typing import List


def hash_embedding(text: str, dimensions: int = 12) -> List[float]:
    """Generate a deterministic pseudo-embedding using hashing."""
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    chunk_size = len(digest) // dimensions
    return [
        int.from_bytes(digest[i * chunk_size : (i + 1) * chunk_size], "big")
        / 2**64
        for i in range(dimensions)
    ]
