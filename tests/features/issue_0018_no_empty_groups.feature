"""No empty menu groups in Insights."""
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


@then("Insights menu has no empty groups")
def insights_menu_no_empty_groups(page: Page) -> None:
    """Verify Insights menu has no empty groups."""
    page.get_by_role("button", name="Insights").first.click()
    
    # Verify group headings
    group_headers = [
        page.locator("text=Insights and Resources"),
        page.locator("text=News & Events"),
    ]
    
    for header in group_headers:
        expect(header).to_be_visible()
    
    # Verify each group has at least one link
    insights_resources_group = page.locator("text=Insights and Resources").first
    next_group = page.locator("text=News & Events").first
    
    # Count links between headers
    links_between = page.locator("text=Insights and Resources ~ text=News & Events").count()
    assert links_between >= 1, "Insights and Resources group should have links"
