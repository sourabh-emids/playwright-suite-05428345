"""Step definitions for issue_0029: Hero media has alternative handling."""
from pytest_bdd import given, then
from playwright.sync_api import Page


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("Hero media has alternative text handling")
def hero_media_has_alt_handling(page: Page) -> None:
    """Verify Hero media has alternative text handling."""
    hero_section = page.locator("section, div").filter(has=page.get_by_role("heading", level=1)).first
    
    images = hero_section.locator("img").all()
    for img in images:
        alt = img.get_attribute("alt")
        assert alt is not None, "Hero images should have alt text"
    
    videos = hero_section.locator("video").all()
    for video in videos:
        aria_label = video.get_attribute("aria-label")
        track = video.locator("track").count()
        assert aria_label is not None or track > 0, "Videos should have caption track or aria-label"
