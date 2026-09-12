"""Responsive design requirements."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("no horizontal scrolling at 320px viewport width")
def no_horizontal_scroll_320(page: Page) -> None:
    """Verify no horizontal scrolling at 320px viewport width."""
    page.set_viewport_size({"width": 320, "height": 568})
    
    has_horizontal_scroll = page.evaluate("""
        () => document.documentElement.scrollWidth > document.documentElement.clientWidth
    """)
    assert not has_horizontal_scroll, "Should not have horizontal scroll at 320px"


@then("typography readable at mobile width")
def typography_readable_mobile(page: Page) -> None:
    """Verify typography readable at mobile width."""
    page.set_viewport_size({"width": 320, "height": 568})
    
    h1 = page.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
    
    h1_font_size = h1.evaluate("el => window.getComputedStyle(el).fontSize")
    font_size_value = int(h1_font_size.replace("px", ""))
    assert font_size_value >= 16, "Font size should be readable at mobile width"


@then("images preserve aspect ratio during resize")
def images_aspect_ratio(page: Page) -> None:
    """Verify images preserve aspect ratio during resize."""
    images = page.locator("img").all()
    
    for img in images:
        natural_width = img.evaluate("el => el.naturalWidth")
        natural_height = img.evaluate("el => el.naturalHeight")
        width = img.get_attribute("width")
        height = img.get_attribute("height")
        
        if natural_width and natural_height and width and height:
            # Aspect ratio should be preserved
            ratio = natural_width / natural_height
            displayed_ratio = int(width) / int(height)
            assert abs(ratio - displayed_ratio) < 0.1, "Image aspect ratio should be preserved"
