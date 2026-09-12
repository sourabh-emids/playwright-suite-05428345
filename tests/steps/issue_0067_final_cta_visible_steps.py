"""Step definitions for issue_0067: Final CTA banner visible before footer."""
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


@then("Final CTA banner is visible before footer")
def final_cta_before_footer(page: Page) -> None:
    """Verify Final CTA banner is visible before footer."""
    final_cta = page.locator("text=1 Day · 2 Weeks · 3 Months")
    expect(final_cta).to_be_visible()
    
    footer = page.get_by_role("contentinfo")
    
    cta_box = final_cta.bounding_box()
    footer_box = footer.bounding_box()
    
    if cta_box and footer_box:
        assert cta_box["y"] < footer_box["y"], "Final CTA should be above footer"
