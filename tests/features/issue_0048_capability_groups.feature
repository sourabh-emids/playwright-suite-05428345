"""Three capability groups AI Engineering Platforms visible."""
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


@then("three capability groups AI Engineering Platforms are visible")
def three_capability_groups_visible(page: Page) -> None:
    """Verify three capability groups are visible."""
    ai_group = page.get_by_role("heading", name="Artificial Intelligence")
    engineering_group = page.get_by_role("heading", name="Engineering")
    platforms_group = page.get_by_role("heading", name="Platforms")
    
    expect(ai_group).to_be_visible()
    expect(engineering_group).to_be_visible()
    expect(platforms_group).to_be_visible()
