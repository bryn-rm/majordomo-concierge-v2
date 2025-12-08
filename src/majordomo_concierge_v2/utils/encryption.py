"""Lightweight reversible encoding (placeholder for real encryption)."""

from __future__ import annotations

import base64


def encode(text: str) -> str:
    """Base64 encode text (not secure; placeholder for real crypto)."""
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def decode(encoded: str) -> str:
    """Decode text previously encoded with `encode`."""
    return base64.b64decode(encoded.encode("utf-8")).decode("utf-8")
