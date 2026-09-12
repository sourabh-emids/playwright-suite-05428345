"""Test for issue_0052 - Responsive layout across common viewports."""
import pytest

from pages.issue_0052_responsive_layout_page import Issue0052ResponsiveLayoutPage


@pytest.fixture
def responsive_layout_page(page) -> Issue0052ResponsiveLayoutPage:
    """Create page object for issue_0052 tests."""
    return Issue0052ResponsiveLayoutPage(page)
