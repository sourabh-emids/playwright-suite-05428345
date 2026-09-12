"""Header visible on narrow viewport."""
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


@then("the header is visible at narrow viewport")
def header_visible_narrow_viewport(page: Page) -> None:
    """Verify header is visible at 320px width."""
    page.set_viewport_size({"width": 320, "height": 568})
    header = page.get_by_role("banner").first
    expect(header).to_be_visible()
