"""Step definitions for issue_0033: Hero media dimensions reserved to avoid layout shift."""
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


@then("Hero media has reserved dimensions")
def hero_media_reserved_dimensions(page: Page) -> None:
    """Verify Hero media has reserved dimensions to avoid layout shift."""
    hero_section = page.locator("section, div").filter(has=page.get_by_role("heading", level=1)).first
    
    images = hero_section.locator("img").all()
    for img in images:
        width = img.get_attribute("width")
        height = img.get_attribute("height")
        style = img.get_attribute("style") or ""
        
        has_explicit_dimensions = width is not None or height is not None or "width" in style or "height" in style
        assert has_explicit_dimensions, "Hero images should have explicit width or height attributes"
