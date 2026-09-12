"""Test for issue_0027: Hero H1 present and readable on initial load."""
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


def test_hero_h1_present_readable(page_ready: Page) -> None:
    """Test Hero H1 is present and readable on initial load."""
    h1 = page_ready.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
    
    text = h1.text_content()
    assert text is not None and text.strip() != "", "H1 should have text content"
