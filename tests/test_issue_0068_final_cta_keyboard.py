"""Test for issue_0068: Final CTA primary action keyboard operable."""
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


def test_final_cta_keyboard_operable(page_ready: Page) -> None:
    """Test Final CTA primary action is keyboard operable."""
    final_cta_connect = page_ready.get_by_role("link", name="Connect").last
    final_cta_connect.focus()
    expect(final_cta_connect).to_be_focused()
