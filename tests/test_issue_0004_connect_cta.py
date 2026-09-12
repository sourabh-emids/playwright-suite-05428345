"""Test for issue_0004: Connect CTA routes to contact experience."""
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


def test_header_connect_cta_routes_to_contact(page_ready: Page) -> None:
    """Test that header Connect CTA routes to contact page."""
    page_ready.get_by_role("link", name="Connect").first.click()
    expect(page_ready).to_have_url("https://www.emids.com/contact/")
