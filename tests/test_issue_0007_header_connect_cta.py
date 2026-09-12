"""Test for issue_0007 - Header Connect CTA visibility and routing."""
import pytest

from pages.issue_0007_connect_cta_page import Issue0007ConnectCTAPage


@pytest.fixture
def connect_cta_page(page) -> Issue0007ConnectCTAPage:
    """Create page object for issue_0007 tests."""
    return Issue0007ConnectCTAPage(page)
