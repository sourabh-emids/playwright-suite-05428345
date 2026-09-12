"""Test for issue_0055: Four impact metrics visible as text."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_four_metrics_visible_text(page_ready: Page) -> None:
    """Test four impact metrics visible as text."""
    expected_metrics = [
        "36+ Years",
        "115+ Million",
        "$48+ Billion",
        "450+",
    ]
    
    for metric in expected_metrics:
        metric_elem = page_ready.locator(f"text={metric}").first
        expect(metric_elem).to_be_visible()
