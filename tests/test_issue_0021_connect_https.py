"""Test for issue_0021: Connect CTA routes to HTTPS contact page."""
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


def test_connect_cta_routes_to_https(page_ready: Page) -> None:
    """Test Connect CTA routes to HTTPS contact page."""
    page_ready.get_by_role("link", name="Connect").first.click()
    expect(page_ready).to_have_url("https://www.emids.com/contact/")
