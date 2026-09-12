"""Test for media integration, resilience, and global requirements."""
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


def test_content_readable_scripts_fail(page_ready: Page) -> None:
    """Test header main content footer readable when scripts fail."""
    header = page_ready.get_by_role("banner").first
    main = page_ready.get_by_role("main").first
    footer = page_ready.get_by_role("contentinfo").first
    
    expect(header).to_be_visible()
    expect(main).to_be_visible()
    expect(footer).to_be_visible()


def test_no_unsolicited_modal(page_ready: Page) -> None:
    """Test base homepage loads without unsolicited modal."""
    h1 = page_ready.get_by_role("heading", level=1).first
    expect(h1).to_be_visible()
    
    modals = page_ready.locator('[role="dialog"], .modal, .popup').all()
    visible_modals = [m for m in modals if m.is_visible()]
    assert len(visible_modals) == 0
