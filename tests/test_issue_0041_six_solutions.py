"""Test for issue_0041: Six featured solutions present with correct numbering."""
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


def test_six_solutions_numbered(page_ready: Page) -> None:
    """Test six featured solutions present with correct numbering."""
    expected_numbers = ["01", "02", "03", "04", "05", "06"]
    
    for number in expected_numbers:
        number_elem = page_ready.locator(f"text={number}").first
        expect(number_elem).to_be_visible()
