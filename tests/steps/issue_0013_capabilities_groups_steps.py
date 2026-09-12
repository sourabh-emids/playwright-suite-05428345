"""Step definitions for issue_0013: Capabilities menu AI Engineering Platforms groups present."""
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


@then("the Capabilities menu has AI Engineering Platforms groups")
def capabilities_menu_has_three_groups(page: Page) -> None:
    """Verify Capabilities menu has AI, Engineering, and Platforms groups."""
    page.get_by_role("button", name="Capabilities").first.click()
    
    ai_group = page.locator("text=AI").first
    engineering_group = page.locator("text=Engineering").first
    platforms_group = page.locator("text=Platforms").first
    
    expect(ai_group).to_be_visible()
    expect(engineering_group).to_be_visible()
    expect(platforms_group).to_be_visible()
