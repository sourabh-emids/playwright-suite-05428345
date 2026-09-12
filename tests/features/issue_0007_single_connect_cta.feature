"""Only one primary Connect CTA in header."""
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


@then("there is only one primary Connect CTA in the header")
def only_one_connect_cta(page: Page) -> None:
    """Verify only one primary Connect CTA exists in header."""
    header = page.get_by_role("banner").first
    connect_ctas = header.get_by_role("link", name="Connect").all()
    assert len(connect_ctas) == 1, "Should have exactly one primary Connect CTA in header"
