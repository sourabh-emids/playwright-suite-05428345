"""Test for issue_0048: Three capability groups AI Engineering Platforms visible."""
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


def test_three_capability_groups_visible(page_ready: Page) -> None:
    """Test three capability groups AI Engineering Platforms are visible."""
    ai_group = page_ready.get_by_role("heading", name="Artificial Intelligence")
    engineering_group = page_ready.get_by_role("heading", name="Engineering")
    platforms_group = page_ready.get_by_role("heading", name="Platforms")
    
    expect(ai_group).to_be_visible()
    expect(engineering_group).to_be_visible()
    expect(platforms_group).to_be_visible()
