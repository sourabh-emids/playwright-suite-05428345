"""Test for issue_0004 - Industries mega-menu content."""
import pytest

from pages.issue_0004_industries_page import Issue0004IndustriesMenuPage


@pytest.fixture
def industries_menu_page(page) -> Issue0004IndustriesMenuPage:
    """Create page object for issue_0004 tests."""
    return Issue0004IndustriesMenuPage(page)
