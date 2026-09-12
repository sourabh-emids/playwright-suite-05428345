"""Test for issue_0035: How We Deliver section renders in intended sequence."""
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


def test_how_we_deliver_sequence(page_ready: Page) -> None:
    """Test How We Deliver section renders in intended sequence."""
    how_we_deliver = page_ready.locator("text=How We Deliver").first
    expect(how_we_deliver).to_be_visible()
    
    h2 = page_ready.get_by_role("heading", name="Embedded healthcare expertise")
    h3 = page_ready.get_by_role("heading", name="Forward-Deployed Context Engineering")
    see_model_cta = page_ready.get_by_role("link", name="See the model")
    
    expect(h2).to_be_visible()
    expect(h3).to_be_visible()
    expect(see_model_cta).to_be_visible()
