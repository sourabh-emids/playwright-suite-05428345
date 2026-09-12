"""Test for issue_0084: Footer legal links have valid HTTPS destinations."""
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


def test_footer_legal_https(page_ready: Page) -> None:
    """Test footer legal links have valid HTTPS destinations."""
    footer = page_ready.get_by_role("contentinfo")
    legal_links = ["Privacy Policy", "Terms of Use", "Accessibility Statement"]
    
    for link_text in legal_links:
        link = footer.get_by_role("link", name=link_text)
        if link.is_visible():
            href = link.get_attribute("href")
            assert href is not None, f"{link_text} should have href"
            assert href.startswith("https://"), f"{link_text} should use HTTPS"
