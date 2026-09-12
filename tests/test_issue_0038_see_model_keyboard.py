"""Test for issue_0038: See the model CTA keyboard operable."""
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


def test_see_model_cta_keyboard_operable(page_ready: Page) -> None:
    """Test See the model CTA is keyboard operable."""
    see_model_cta = page_ready.get_by_role("link", name="See the model")
    see_model_cta.focus()
    expect(see_model_cta).to_be_focused()
    
    href = see_model_cta.get_attribute("href")
    assert href is not None, "See the model CTA should have href"
