"""Test for insight cards display."""
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


def test_payer_blog_card_with_read_more(page_ready: Page) -> None:
    """Test Payer data readiness blog card displays with Read More."""
    page_ready.goto("/insights/")
    read_more = page_ready.get_by_role("link", name="Read More")
    expect(read_more).to_be_visible()
