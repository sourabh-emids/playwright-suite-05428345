"""Test for issue_0067: Final CTA banner visible before footer."""
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


def test_final_cta_before_footer(page_ready: Page) -> None:
    """Test Final CTA banner is visible before footer."""
    final_cta = page_ready.locator("text=1 Day · 2 Weeks · 3 Months")
    expect(final_cta).to_be_visible()
    
    footer = page_ready.get_by_role("contentinfo")
    
    cta_box = final_cta.bounding_box()
    footer_box = footer.bounding_box()
    
    if cta_box and footer_box:
        assert cta_box["y"] < footer_box["y"], "Final CTA should be above footer"
