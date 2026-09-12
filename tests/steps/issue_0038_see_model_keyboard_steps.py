"""Step definitions for issue_0038: See the model CTA keyboard operable."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("See the model CTA is keyboard operable")
def see_model_cta_keyboard_operable(page: Page) -> None:
    """Verify See the model CTA is keyboard operable."""
    see_model_cta = page.get_by_role("link", name="See the model")
    see_model_cta.focus()
    expect(see_model_cta).to_be_focused()
    
    href = see_model_cta.get_attribute("href")
    assert href is not None, "See the model CTA should have href"
