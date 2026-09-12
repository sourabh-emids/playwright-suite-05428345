"""Step definitions for issue_0018: No empty menu groups in Insights."""
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
    
    group_headers = [
        page.locator("text=Insights and Resources"),
        page.locator("text=News & Events"),
    ]
    
    for header in group_headers:
        expect(header).to_be_visible()
    
    # Verify each group has links
    insights_hub = page.get_by_role("link", name="Insights Hub")
    case_studies = page.get_by_role("link", name="Case Studies")
    ebooks = page.get_by_role("link", name="eBooks & Guides")
    webinars = page.get_by_role("link", name="Webinars")
    news = page.get_by_role("link", name="News")
    
    expect(insights_hub).to_be_visible()
    expect(case_studies).to_be_visible()
    expect(ebooks).to_be_visible()
    expect(webinars).to_be_visible()
    expect(news).to_be_visible()
