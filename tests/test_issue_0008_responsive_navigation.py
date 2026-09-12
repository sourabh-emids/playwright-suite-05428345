"""Test for issue_0008 - Responsive navigation behavior."""
import pytest

from pages.issue_0008_responsive_nav_page import Issue0008ResponsiveNavPage


@pytest.fixture
def responsive_nav_page(page) -> Issue0008ResponsiveNavPage:
    """Create page object for issue_0008 tests."""
    return Issue0008ResponsiveNavPage(page)
