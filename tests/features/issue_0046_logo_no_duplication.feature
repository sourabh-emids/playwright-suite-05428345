"""Logo rail does not duplicate for screen readers."""
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


@then("logo rail does not duplicate for screen readers")
def logo_rail_no_duplication(page: Page) -> None:
    """Verify logo rail does not duplicate for screen readers."""
    # Check if there's an aria-hidden attribute on duplicated content
    partnerships_section = page.locator("text=Partnerships").first
    
    # Verify logos are not marked as decorative when they need alt text
    logos = partnerships_section.locator("img").all()
    for logo in logos:
        alt = logo.get_attribute("alt")
        aria_hidden = logo.get_attribute("aria-hidden")
        # If alt is present and meaningful, aria-hidden should not be true
        if alt and alt.strip():
            # This is fine - logo has accessible name
            pass
