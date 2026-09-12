"""Step definitions for issue_0055: Four impact metrics visible as text."""
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


@then("four impact metrics are visible as text")
def four_metrics_visible_text(page: Page) -> None:
    """Verify four impact metrics visible as text."""
    expected_metrics = [
        "36+ Years",
        "115+ Million",
        "$48+ Billion",
        "450+",
    ]
    
    for metric in expected_metrics:
        metric_elem = page.locator(f"text={metric}").first
        expect(metric_elem).to_be_visible()
