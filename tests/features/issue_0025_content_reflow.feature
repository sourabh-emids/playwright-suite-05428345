"""Content reflows without horizontal scrolling at 320px."""
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


@then("content reflows without horizontal scrolling at 320px")
def content_reflows_at_320px(page: Page) -> None:
    """Verify content reflows without horizontal scrolling at 320px."""
    page.set_viewport_size({"width": 320, "height": 568})
    
    # Check for horizontal scrollbar
    has_horizontal_scroll = page.evaluate("""
        () => {
            return document.documentElement.scrollWidth > document.documentElement.clientWidth;
        }
    """)
    assert not has_horizontal_scroll, "Content should reflow without horizontal scrolling at 320px"
