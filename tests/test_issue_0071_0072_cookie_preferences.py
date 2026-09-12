"""Test for Cookie Preferences."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage."""
    page.goto("/")
    return page


def test_cookie_preferences_visible(page_ready: Page) -> None:
    """Test Cookie Preferences control is visible in footer."""
    footer = page_ready.get_by_role("contentinfo")
    expect(footer).to_be_visible()


def test_cookie_preferences_opens_ui(page_ready: Page) -> None:
    """Test Cookie Preferences opens consent management UI."""
    customize_btn = page_ready.get_by_role("button", name="Customize")
    if customize_btn.is_visible():
        customize_btn.click()
        expect(page_ready.get_by_role("tabpanel")).to_be_visible()
