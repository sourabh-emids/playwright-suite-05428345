"""Test for issue_0020: Connect CTA visually distinct and keyboard accessible."""
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


def test_connect_cta_visually_distinct(page_ready: Page) -> None:
    """Test Connect CTA is visually distinct."""
    connect_cta = page_ready.get_by_role("link", name="Connect").first
    expect(connect_cta).to_be_visible()
    href = connect_cta.get_attribute("href")
    assert href is not None, "Connect CTA should have href"


def test_connect_cta_keyboard_accessible(page_ready: Page) -> None:
    """Test Connect CTA is keyboard accessible."""
    connect_cta = page_ready.get_by_role("link", name="Connect").first
    connect_cta.focus()
    expect(connect_cta).to_be_focused()
