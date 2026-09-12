"""1 Day 2 Weeks 3 Months message renders in order."""
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


@then("1 Day 2 Weeks 3 Months message renders in order")
def timing_order(page: Page) -> None:
    """Verify 1 Day 2 Weeks 3 Months message renders in order."""
    final_cta_section = page.locator("text=1 Day · 2 Weeks · 3 Months")
    expect(final_cta_section).to_be_visible()


@then("timing labels are screen reader accessible")
def timing_labels_screen_reader(page: Page) -> None:
    """Verify timing labels are screen reader accessible."""
    final_cta_section = page.locator("text=1 Day · 2 Weeks · 3 Months")
    
    # Verify section has accessible name or role
    accessible_name = final_cta_section.get_attribute("aria-label") or final_cta_section.text_content()
    assert accessible_name is not None and accessible_name.strip() != "", "Should have accessible content"
