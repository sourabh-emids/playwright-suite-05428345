"""Test for issue_0039: Exactly one H1 on page with logical heading hierarchy."""
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


def test_exactly_one_h1(page_ready: Page) -> None:
    """Test exactly one H1 on the page."""
    h1_elements = page_ready.get_by_role("heading", level=1).all()
    assert len(h1_elements) == 1, f"Should have exactly one H1, found {len(h1_elements)}"


def test_heading_hierarchy_logical(page_ready: Page) -> None:
    """Test heading hierarchy is logical."""
    h2_elements = page_ready.get_by_role("heading", level=2).all()
    h3_elements = page_ready.get_by_role("heading", level=3).all()
    
    if len(h3_elements) > 0:
        assert len(h2_elements) >= 1, "H3 elements should have H2 parents"
