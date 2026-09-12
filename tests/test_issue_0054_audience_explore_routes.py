"""Test for issue_0054: Audience Explore routes to canonical segment page."""
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


def test_audience_explore_routes_to_segment(page_ready: Page) -> None:
    """Test Audience Explore routes to canonical segment page."""
    page_ready.locator("text=Explore").first.click()
    current_url = page_ready.url
    assert "/segments/" in current_url, f"Should be on segment page, got: {current_url}"
