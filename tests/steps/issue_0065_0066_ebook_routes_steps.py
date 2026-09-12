"""Step definitions for eBook Download routes."""
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


@then("resource access does not expose private asset endpoint")
def no_private_endpoint_exposure(page: Page) -> None:
    """Verify resource access does not expose private asset endpoint."""
    page.goto("/insights/")
    links = page.locator('[href*=".pdf"], [href*=".zip"], [href*="download"]').all()
    for link in links:
        href = link.get_attribute("href")
        if href:
            assert not href.startswith("s3://"), "Should not expose S3 bucket URL"
            assert not "private" in href.lower(), "Should not expose private endpoints"
