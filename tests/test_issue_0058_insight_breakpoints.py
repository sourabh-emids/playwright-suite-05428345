"""Test for issue_0058: Insight cards accessible at all breakpoints."""
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


def test_insight_cards_all_breakpoints(page_ready: Page) -> None:
    """Test insight cards accessible at all breakpoints."""
    page_ready.set_viewport_size({"width": 1280, "height": 720})
    insights_heading = page_ready.get_by_role("heading", name="The intelligence behind the outcomes")
    expect(insights_heading).to_be_visible()
    
    page_ready.set_viewport_size({"width": 768, "height": 1024})
    expect(insights_heading).to_be_visible()
    
    page_ready.set_viewport_size({"width": 375, "height": 667})
    expect(insights_heading).to_be_visible()
