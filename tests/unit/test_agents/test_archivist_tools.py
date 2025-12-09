"""Unit checks for archivist document tools."""

from majordomo_concierge_v2.tools.local.document_tools import store_document, search_documents


def test_document_store_and_search():
    store_document("doc1", "The quick brown fox jumps over the lazy dog", tags="animals")
    results = search_documents("brown fox")
    assert "doc1" in results
