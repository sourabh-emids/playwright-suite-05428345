"""Step definitions for issue_0041: Six featured solutions present with correct numbering."""
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


@then("six featured solutions are present with correct numbering")
def six_solutions_numbered(page: Page) -> None:
    """Verify six featured solutions present with correct numbering."""
    expected_numbers = ["01", "02", "03", "04", "05", "06"]
    
    for number in expected_numbers:
        number_elem = page.locator(f"text={number}").first
        expect(number_elem).to_be_visible()
