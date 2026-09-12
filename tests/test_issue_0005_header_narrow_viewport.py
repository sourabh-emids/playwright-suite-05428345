"""Test for issue_0005: Header visible on narrow viewport."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_header_visible_at_narrow_viewport(page_ready: Page) -> None:
    """Test header is visible at 320px width."""
    page_ready.set_viewport_size({"width": 320, "height": 568})
    header = page_ready.get_by_role("banner").first
    expect(header).to_be_visible()
