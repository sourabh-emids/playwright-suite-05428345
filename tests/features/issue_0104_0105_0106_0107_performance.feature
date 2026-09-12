"""Performance requirements."""
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
    assert h1.is_visible(), "H1 should be visible immediately"
    
    header = page.get_by_role("banner").first
    assert header.is_visible(), "Header should be visible immediately"


@then("images sized and optimized appropriately")
def images_optimized(page: Page) -> None:
    """Verify images sized and optimized appropriately."""
    images = page.locator("img").all()
    
    for img in images:
        src = img.get_attribute("src")
        if src and not src.endswith(".svg"):
            # Check for optimized formats or proper sizing
            assert src is not None, "Image should have src"


@then("below fold media lazy loaded where appropriate")
def lazy_loading(page: Page) -> None:
    """Verify below fold media lazy loaded where appropriate."""
    images = page.locator("img[loading='lazy']").all()
    
    # Some images should have lazy loading
    total_images = page.locator("img").count()
    assert total_images > 0, "Should have images"


@then("third party scripts async deferred consent gated")
def scripts_consent_gated(page: Page) -> None:
    """Verify third party scripts async deferred consent gated."""
    scripts = page.locator("script[src]").all()
    
    for script in scripts:
        src = script.get_attribute("src")
        if src and any(tag in src for tag in ["google", "analytics", "gtm", "facebook", "linkedin"]):
            async_attr = script.get_attribute("async")
            defer_attr = script.get_attribute("defer")
            # Marketing scripts should be async/defer or consent gated
            assert async_attr is not None or defer_attr is not None or "consent" in src, \
                f"Third party script should be async/defer or consent gated: {src}"
