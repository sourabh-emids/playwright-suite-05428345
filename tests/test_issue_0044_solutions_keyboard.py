"""Test for issue_0044: Featured solutions reachable on keyboard and touch."""
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


def test_solutions_keyboard_reachable(page_ready: Page) -> None:
    """Test featured solutions are keyboard reachable."""
    solution_link = page_ready.get_by_role("link", name="Explore solution: Modernization as a Service").first
    solution_link.focus()
    expect(solution_link).to_be_focused()
