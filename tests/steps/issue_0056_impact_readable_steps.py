"""Step definitions for issue_0056: Impact values understandable without animation."""
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


@then("impact values are understandable without animation")
def impact_values_readable(page: Page) -> None:
    """Verify impact values are understandable without animation."""
    metric_values = [
        page.locator("text=36+ Years").first,
        page.locator("text=115+ Million").first,
        page.locator("text=$48+ Billion").first,
        page.locator("text=450+").first,
    ]
    
    for metric in metric_values:
        text = metric.text_content()
        assert text is not None and text.strip() != "", "Metric should have readable text"
        assert metric.is_visible(), "Metric should be visible"
