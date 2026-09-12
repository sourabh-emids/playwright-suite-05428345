"""Test for issue_0033: Hero media dimensions reserved to avoid layout shift."""
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


def test_hero_media_reserved_dimensions(page_ready: Page) -> None:
    """Test Hero media has reserved dimensions to avoid layout shift."""
    hero_section = page_ready.locator("section, div").filter(has=page_ready.get_by_role("heading", level=1)).first
    
    images = hero_section.locator("img").all()
    for img in images:
        width = img.get_attribute("width")
        height = img.get_attribute("height")
        style = img.get_attribute("style") or ""
        
        has_explicit_dimensions = width is not None or height is not None or "width" in style or "height" in style
        assert has_explicit_dimensions, "Hero images should have explicit width or height attributes"
