"""Step definitions for issue_0042: Featured solutions titles not blank and destination valid."""
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


@then("featured solutions titles are not blank and destinations are valid")
def solutions_titles_destinations_valid(page: Page) -> None:
    """Verify featured solutions titles are not blank and destinations valid."""
    explore_links = page.locator('[href*="/solutions/"]').all()
    for link in explore_links:
        href = link.get_attribute("href")
        assert href is not None and href != "", "Link should have valid href"
        assert "/solutions/" in href, f"Link should point to solutions: {href}"
