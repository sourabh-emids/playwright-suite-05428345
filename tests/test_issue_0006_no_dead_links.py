"""Test for issue_0006: No dead links in navigation items."""
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_no_dead_links_in_navigation(page_ready: Page) -> None:
    """Test all navigation links have valid href attributes."""
    nav = page_ready.get_by_role("navigation", name="Main Navigation")
    links = nav.get_by_role("link").all()
    
    for link in links:
        href = link.get_attribute("href")
        assert href is not None, "Navigation link should have href attribute"
        assert href != "", "Navigation link href should not be empty"
        assert href != "#", "Navigation link should not be a dead link"
