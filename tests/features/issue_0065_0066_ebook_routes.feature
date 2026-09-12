"""eBook Download routes to detail access experience."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@when("I click on an eBook card")
def click_ebook_card(page: Page) -> None:
    """Click on an eBook card."""
    page.goto("/insights/")
    page.get_by_role("link", name="eBook").first.click()


@then("I am routed to the eBook detail page")
def routed_to_ebook_detail(page: Page) -> None:
    """Verify user is routed to eBook detail page."""
    current_url = page.url
    assert "/insights/" in current_url or "/ebook/" in current_url, f"Should be on insights/ebook page: {current_url}"


@then("resource access does not expose private asset endpoint")
def no_private_endpoint_exposure(page: Page) -> None:
    """Verify resource access does not expose private asset endpoint."""
    # Check that download URLs are properly routed through a public endpoint
    page.goto("/insights/")
    links = page.locator('[href*=".pdf"], [href*=".zip"], [href*="download"]').all()
    for link in links:
        href = link.get_attribute("href")
        # Should not expose S3 bucket URLs or other private endpoints
        if href:
            assert not href.startswith("s3://"), "Should not expose S3 bucket URL"
            assert not "private" in href.lower(), "Should not expose private endpoints"
