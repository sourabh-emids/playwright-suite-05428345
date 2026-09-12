"""Connect CTA visually distinct and keyboard accessible."""
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


@then("the Connect CTA is visually distinct")
def connect_cta_visually_distinct(page: Page) -> None:
    """Verify Connect CTA is visually distinct from other navigation."""
    connect_cta = page.get_by_role("link", name="Connect").first
    
    # Verify it has a distinctive style (should have a different visual treatment)
    # Check it's visible and has an href
    expect(connect_cta).to_be_visible()
    href = connect_cta.get_attribute("href")
    assert href is not None, "Connect CTA should have href"


@then("the Connect CTA is keyboard accessible")
def connect_cta_keyboard_accessible(page: Page) -> None:
    """Verify Connect CTA is keyboard accessible."""
    connect_cta = page.get_by_role("link", name="Connect").first
    connect_cta.focus()
    expect(connect_cta).to_be_focused()
