"""Test for responsive design requirements."""
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


def test_no_horizontal_scroll_320(page_ready: Page) -> None:
    """Test no horizontal scrolling at 320px viewport width."""
    page_ready.set_viewport_size({"width": 320, "height": 568})
    
    has_horizontal_scroll = page_ready.evaluate("""
        () => document.documentElement.scrollWidth > document.documentElement.clientWidth
    """)
    assert not has_horizontal_scroll


def test_typography_readable_mobile(page_ready: Page) -> None:
    """Test typography readable at mobile width."""
    page_ready.set_viewport_size({"width": 320, "height": 568})
    
    h1 = page_ready.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
