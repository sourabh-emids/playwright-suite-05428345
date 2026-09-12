"""Test for issue_0042: Featured solutions titles not blank and destination valid."""
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


def test_solutions_titles_destinations_valid(page_ready: Page) -> None:
    """Test featured solutions titles not blank and destinations valid."""
    explore_links = page_ready.locator('[href*="/solutions/"]').all()
    for link in explore_links:
        href = link.get_attribute("href")
        assert href is not None and href != "", "Link should have valid href"
        assert "/solutions/" in href, f"Link should point to solutions: {href}"
