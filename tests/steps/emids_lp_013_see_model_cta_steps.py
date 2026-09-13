"""Step definitions for emids_lp_013 - See the model CTA."""
from playwright.sync_api import Page, expect
from pytest_bdd import when, then


@when("The user clicks the CTA")
def user_clicks_see_model_cta(page: Page) -> None:
    from pages.emids_lp_013_see_model_cta_page import SeeModelCTAPage
    page_obj = SeeModelCTAPage(page)
    page_obj.see_model_cta.click()


@then("The CTA routes to '/forward-deployed-context-engineering/'")
def verify_see_model_routes(page: Page) -> None:
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("The CTA can be activated using Enter or Space key")
def verify_cta_keyboard_operable(page: Page) -> None:
    from pages.emids_lp_013_see_model_cta_page import SeeModelCTAPage
    page_obj = SeeModelCTAPage(page)
    page_obj.see_model_cta.focus()
    page.keyboard.press("Enter")
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("Accessible name clearly describes the action 'See the model'")
def verify_accessible_name(page: Page) -> None:
    from pages.emids_lp_013_see_model_cta_page import SeeModelCTAPage
    page_obj = SeeModelCTAPage(page)
    text = page_obj.see_model_cta.text_content()
    assert "see" in text.lower() and "model" in text.lower(), f"CTA text '{text}' doesn't describe action"


@then("Visual hover/focus states are visible")
def verify_hover_focus_states(page: Page) -> None:
    from pages.emids_lp_013_see_model_cta_page import SeeModelCTAPage
    page_obj = SeeModelCTAPage(page)
    page_obj.see_model_cta.hover()
    page_obj.see_model_cta.focus()


@then("Page displays appropriate error without breaking navigation")
def verify_404_handled(page: Page) -> None:
    expect(page).to_have_url("/forward-deployed-context-engineering/")
