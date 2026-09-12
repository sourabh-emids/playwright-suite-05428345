"""Test for issue_0040: Semantic landmarks main header footer identifiable."""
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


def test_landmarks_identifiable(page_ready: Page) -> None:
    """Test main, header, footer landmarks are identifiable."""
    header = page_ready.get_by_role("banner").first
    main = page_ready.get_by_role("main").first
    footer = page_ready.get_by_role("contentinfo").first
    
    expect(header).to_be_visible()
    expect(main).to_be_visible()
    expect(footer).to_be_visible()
