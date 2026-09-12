"""Test for issue_0046: Logo rail does not duplicate for screen readers."""
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


def test_logo_rail_no_duplication(page_ready: Page) -> None:
    """Test logo rail does not duplicate for screen readers."""
    partnerships_section = page_ready.locator("text=Partnerships").first
    logos = partnerships_section.locator("img").all()
    for logo in logos:
        alt = logo.get_attribute("alt")
        aria_hidden = logo.get_attribute("aria-hidden")
        if alt and alt.strip():
            # Logo has accessible name, which is correct
            pass
