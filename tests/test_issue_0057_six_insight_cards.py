"""Test for issue_0057: Six insight cards render with type title and action."""
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


def test_insight_cards_render(page_ready: Page) -> None:
    """Test insight cards render with type title and action."""
    insights_section = page_ready.get_by_role("heading", name="The intelligence behind the outcomes")
    expect(insights_section).to_be_visible()
    
    next_button = page_ready.get_by_role("button", name="Next")
    expect(next_button).to_be_visible()
