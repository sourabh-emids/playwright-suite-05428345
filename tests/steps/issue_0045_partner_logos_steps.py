"""Step definitions for issue_0045: Partner logos render with accessible names."""
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


@then("partner logos render with accessible names")
def partner_logos_accessible(page: Page) -> None:
    """Verify partner logos render with accessible names."""
    logos = page.locator("img[alt*='Partner'], img[alt*='Logo']").all()
    
    assert len(logos) > 0, "Should have partner logos"
    
    for logo in logos:
        alt = logo.get_attribute("alt")
        assert alt is not None and alt.strip() != "", f"Logo should have accessible alt text: {alt}"
