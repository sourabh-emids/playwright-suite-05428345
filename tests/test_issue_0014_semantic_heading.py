"""Test for issue_0014 - Semantic heading hierarchy and landmarks."""
import pytest

from pages.issue_0014_semantic_page import Issue0014SemanticPage


@pytest.fixture
def semantic_page(page) -> Issue0014SemanticPage:
    """Create page object for issue_0014 tests."""
    return Issue0014SemanticPage(page)
