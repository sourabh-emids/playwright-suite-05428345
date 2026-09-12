"""Test for issue_0026: Interactive controls are semantic buttons links."""
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


def test_controls_are_semantic(page_ready: Page) -> None:
    """Test interactive controls are semantic buttons or links."""
    nav = page_ready.get_by_role("navigation", name="Main Navigation")
    
    buttons = nav.get_by_role("button").all()
    for button in buttons:
        tag = button.evaluate("el => el.tagName")
        assert tag == "BUTTON", f"Button element should be a semantic <button>, got <{tag}>"
    
    links = nav.get_by_role("link").all()
    for link in links:
        tag = link.evaluate("el => el.tagName")
        assert tag == "A", f"Link element should be a semantic <a>, got <{tag}>"
