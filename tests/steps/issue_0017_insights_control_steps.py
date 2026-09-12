"""Step definitions for issue_0017: Insights control opens with child links readable."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@when("I click the Insights button")
def click_insights_button(page: Page) -> None:
    """Click the Insights button."""
    page.get_by_role("button", name="Insights").first.click()


@then("the Insights menu opens with child links readable")
def insights_menu_opens(page: Page) -> None:
    """Verify Insights menu opens and child links are readable."""
    insights_header = page.locator("text=Insights and Resources").first
    expect(insights_header).to_be_visible()
    
    child_links = [
        "Insights Hub",
        "Case Studies",
        "eBooks & Guides",
        "Webinars",
    ]
    
    for link_text in child_links:
        link = page.get_by_role("link", name=link_text)
        expect(link).to_be_visible()
