"""Step definitions for issue_0027: Hero H1 present and readable on initial load."""
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


@then("Hero H1 is present and readable on initial load")
def hero_h1_present_readable(page: Page) -> None:
    """Verify Hero H1 is present and readable on initial load."""
    h1 = page.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
    
    text = h1.text_content()
    assert text is not None and text.strip() != "", "H1 should have text content"
