"""Test for issue_0002: Emids logo navigates to homepage."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_on_contact(page: Page) -> Page:
    """Navigate to contact page."""
    page.goto("/contact/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_emids_logo_navigates_to_homepage(page_on_contact: Page) -> None:
    """Test that clicking Emids logo navigates to homepage."""
    page_on_contact.get_by_role("link", name="Emids logo").click()
    expect(page_on_contact).to_have_url("https://www.emids.com/")
