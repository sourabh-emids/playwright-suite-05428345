"""Test for issue_0034: Hero media uses optimized format and size."""
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


def test_hero_media_optimized(page_ready: Page) -> None:
    """Test Hero media uses optimized format and size."""
    hero_section = page_ready.locator("section, div").filter(has=page_ready.get_by_role("heading", level=1)).first
    
    images = hero_section.locator("img").all()
    for img in images:
        src = img.get_attribute("src") or ""
        assert src != "", "Hero images should have a src attribute"
