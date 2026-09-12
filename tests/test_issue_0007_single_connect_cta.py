"""Test for issue_0007: Only one primary Connect CTA in header."""
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


def test_only_one_connect_cta_in_header(page_ready: Page) -> None:
    """Test only one primary Connect CTA exists in header."""
    header = page_ready.get_by_role("banner").first
    connect_ctas = header.get_by_role("link", name="Connect").all()
    assert len(connect_ctas) == 1, "Should have exactly one primary Connect CTA in header"
