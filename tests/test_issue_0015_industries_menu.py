"""Test for issue_0015: Industries menu contains all five audiences."""
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


def test_industries_menu_has_five_audiences(page_ready: Page) -> None:
    """Test Industries menu contains all five audiences."""
    page_ready.get_by_role("button", name="Industries").first.click()
    
    audiences = ["Payer", "Provider", "Health Tech", "Life Sciences", "Consumer"]
    
    for audience in audiences:
        link = page_ready.get_by_role("link", name=audience)
        expect(link).to_be_visible()
