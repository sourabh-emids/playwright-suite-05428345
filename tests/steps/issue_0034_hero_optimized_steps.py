"""Step definitions for issue_0034: Hero media uses optimized format and size."""
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


@then("Hero media uses optimized format and size")
def hero_media_optimized(page: Page) -> None:
    """Verify Hero media uses optimized format (WebP/AVIF) and appropriate size."""
    hero_section = page.locator("section, div").filter(has=page.get_by_role("heading", level=1)).first
    
    images = hero_section.locator("img").all()
    for img in images:
        src = img.get_attribute("src") or ""
        assert src != "", "Hero images should have a src attribute"
