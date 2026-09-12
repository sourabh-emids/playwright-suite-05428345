"""Test for issue_0025: Content reflows without horizontal scrolling at 320px."""
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_content_reflows_at_320px(page_ready: Page) -> None:
    """Test content reflows without horizontal scrolling at 320px."""
    page_ready.set_viewport_size({"width": 320, "height": 568})
    
    has_horizontal_scroll = page_ready.evaluate("""
        () => {
            return document.documentElement.scrollWidth > document.documentElement.clientWidth;
        }
    """)
    assert not has_horizontal_scroll, "Content should reflow without horizontal scrolling at 320px"
