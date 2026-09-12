"""Test for issue_0043: All Solutions CTA routes to solutions portfolio."""
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


def test_all_solutions_cta_routes_to_solutions(page_ready: Page) -> None:
    """Test All solutions CTA routes to solutions portfolio page."""
    page_ready.get_by_role("link", name="All solutions").click()
    expect(page_ready).to_have_url("https://www.emids.com/solutions/")
