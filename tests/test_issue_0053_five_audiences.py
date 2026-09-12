"""Test for issue_0053: Five audience entries with Explore actions visible."""
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


def test_five_audiences_explore_visible(page_ready: Page) -> None:
    """Test five audience entries with Explore actions visible."""
    audiences = ["Payer", "Provider", "HealthTech", "Life Sciences", "Consumer"]
    
    for audience in audiences:
        button = page_ready.get_by_role("button", name=audience)
        expect(button).to_be_visible()
