"""Test for timing labels."""
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


def test_timing_order(page_ready: Page) -> None:
    """Test 1 Day 2 Weeks 3 Months message renders in order."""
    final_cta_section = page_ready.locator("text=1 Day · 2 Weeks · 3 Months")
    expect(final_cta_section).to_be_visible()


def test_timing_labels_screen_reader(page_ready: Page) -> None:
    """Test timing labels are screen reader accessible."""
    final_cta_section = page_ready.locator("text=1 Day · 2 Weeks · 3 Months")
    
    accessible_name = final_cta_section.get_attribute("aria-label") or final_cta_section.text_content()
    assert accessible_name is not None and accessible_name.strip() != "", "Should have accessible content"
