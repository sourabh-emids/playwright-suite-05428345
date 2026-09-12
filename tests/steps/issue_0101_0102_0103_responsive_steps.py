"""Step definitions for responsive design requirements."""
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
    assert not has_horizontal_scroll


@then("typography readable at mobile width")
def typography_readable_mobile(page: Page) -> None:
    """Verify typography readable at mobile width."""
    page.set_viewport_size({"width": 320, "height": 568})
    
    h1 = page.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
