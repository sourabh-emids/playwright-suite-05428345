"""Test for issue_0029: Hero media has alternative handling."""
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


def test_hero_media_has_alt_handling(page_ready: Page) -> None:
    """Test Hero media has alternative text handling."""
    hero_section = page_ready.locator("section, div").filter(has=page_ready.get_by_role("heading", level=1)).first
    
    images = hero_section.locator("img").all()
    for img in images:
        alt = img.get_attribute("alt")
        assert alt is not None, "Hero images should have alt text"
    
    videos = hero_section.locator("video").all()
    for video in videos:
        aria_label = video.get_attribute("aria-label")
        track = video.locator("track").count()
        assert aria_label is not None or track > 0, "Videos should have caption track or aria-label"
