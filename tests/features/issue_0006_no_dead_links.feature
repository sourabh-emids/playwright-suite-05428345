"""No dead links in navigation items."""
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


@then("all navigation links have valid href attributes")
def nav_links_have_valid_href(page: Page) -> None:
    """Verify all navigation links have valid href attributes."""
    nav = page.get_by_role("navigation", name="Main Navigation")
    links = nav.get_by_role("link").all()
    
    for link in links:
        href = link.get_attribute("href")
        assert href is not None, "Navigation link should have href attribute"
        assert href != "", "Navigation link href should not be empty"
        assert href != "#", "Navigation link should not be a dead link"
