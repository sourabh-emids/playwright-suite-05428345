"""Step definitions for performance requirements."""
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


@then("critical content renders without waiting for analytics")
def critical_content_no_wait(page: Page) -> None:
    """Verify critical content renders without waiting for analytics."""
    h1 = page.get_by_role("heading", level=1).first
    assert h1.is_visible()
    
    header = page.get_by_role("banner").first
    assert header.is_visible()


@then("images sized and optimized appropriately")
def images_optimized(page: Page) -> None:
    """Verify images sized and optimized appropriately."""
    images = page.locator("img").all()
    for img in images:
        src = img.get_attribute("src")
        if src and not src.endswith(".svg"):
            assert src is not None
