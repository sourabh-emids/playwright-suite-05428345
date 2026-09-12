"""Featured solutions reachable on keyboard and touch."""
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


@then("featured solutions are keyboard reachable")
def solutions_keyboard_reachable(page: Page) -> None:
    """Verify featured solutions are keyboard reachable."""
    solution_link = page.get_by_role("link", name="Explore solution: Modernization as a Service").first
    solution_link.focus()
    expect(solution_link).to_be_focused()
