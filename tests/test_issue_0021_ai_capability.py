"""Test for issue_0021 - AI capability content rendering and links."""
import pytest

from pages.issue_0021_ai_capability_page import Issue0021AICapabilityPage


@pytest.fixture
def ai_capability_page(page) -> Issue0021AICapabilityPage:
    """Create page object for issue_0021 tests."""
    return Issue0021AICapabilityPage(page)
