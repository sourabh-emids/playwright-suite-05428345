"""Test for issue_0001: Header renders on initial page load."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_with_header(page: Page) -> Page:
    """Navigate to homepage and accept cookies."""
    page.goto("/")
    # Accept cookies if banner is visible
    try:
        allow_btn = page.get_by_role("button", name="Allow all")
        if allow_btn.is_visible():
            allow_btn.click()
    except Exception:
        pass
    return page


def test_header_renders_on_initial_load(page_with_header: Page) -> None:
    """Test that header renders on initial page load."""
    header = page_with_header.get_by_role("banner").first
    expect(header).to_be_visible()
