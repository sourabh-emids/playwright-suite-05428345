"""Test for eBook Download routes."""
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_no_private_endpoint_exposure(page_ready: Page) -> None:
    """Test resource access does not expose private asset endpoint."""
    page_ready.goto("/insights/")
    links = page_ready.locator('[href*=".pdf"], [href*=".zip"], [href*="download"]').all()
    for link in links:
        href = link.get_attribute("href")
        if href:
            assert not href.startswith("s3://"), "Should not expose S3 bucket URL"
            assert not "private" in href.lower(), "Should not expose private endpoints"
