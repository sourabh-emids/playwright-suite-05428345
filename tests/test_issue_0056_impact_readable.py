"""Test for issue_0056: Impact values understandable without animation."""
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


def test_impact_values_readable(page_ready: Page) -> None:
    """Test impact values are understandable without animation."""
    metric_values = [
        page_ready.locator("text=36+ Years").first,
        page_ready.locator("text=115+ Million").first,
        page_ready.locator("text=$48+ Billion").first,
        page_ready.locator("text=450+").first,
    ]
    
    for metric in metric_values:
        text = metric.text_content()
        assert text is not None and text.strip() != "", "Metric should have readable text"
        assert metric.is_visible(), "Metric should be visible"
