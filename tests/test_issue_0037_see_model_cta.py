"""Test for issue_0037: See the model CTA routes to FDCE detail page."""
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


def test_see_model_cta_routes_to_fdce(page_ready: Page) -> None:
    """Test See the model CTA routes to FDCE detail page."""
    page_ready.get_by_role("link", name="See the model").click()
    expect(page_ready).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")
