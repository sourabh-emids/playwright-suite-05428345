"""Test for issue_0045: Partner logos render with accessible names."""
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


def test_partner_logos_accessible(page_ready: Page) -> None:
    """Test partner logos render with accessible names."""
    logos = page_ready.locator("img[alt*='Partner'], img[alt*='Logo']").all()
    
    assert len(logos) > 0, "Should have partner logos"
    
    for logo in logos:
        alt = logo.get_attribute("alt")
        assert alt is not None and alt.strip() != "", f"Logo should have accessible alt text: {alt}"
