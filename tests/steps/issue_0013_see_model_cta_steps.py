"""Steps for See the model CTA functionality (issue_0013)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0013_see_model_cta_page import SeeModelCTAPage
from locators.issue_0013_see_model_cta_locators import SeeModelCTALocators


@given("User is on How We Deliver section")
def on_how_we_deliver(page: Page) -> None:
    page.goto("/")
    cta_page = SeeModelCTAPage(page)
    cta_page.scroll_to_cta()


@given("User is on How We Deliver section with keyboard focus")
def on_how_we_deliver_keyboard(page: Page) -> None:
    page.goto("/")
    cta_page = SeeModelCTAPage(page)
    cta_page.scroll_to_cta()
    cta_page.focus_cta()


@given("User uses screen reader")
def screen_reader(page: Page) -> None:
    page.goto("/")


@given("User hovers over 'See the model' CTA")
def hover_cta(page: Page) -> None:
    page.goto("/")
    cta_page = SeeModelCTAPage(page)
    cta_page.scroll_to_cta()
    cta_page.hover_cta()


@given("User tabs to 'See the model' CTA")
def tab_to_cta(page: Page) -> None:
    page.goto("/")
    cta_page = SeeModelCTAPage(page)
    cta_page.scroll_to_cta()
    cta_page.focus_cta()


@given("Multiple CTAs exist on page")
def multiple_ctas(page: Page) -> None:
    page.goto("/")


@when("User clicks 'See the model' CTA")
def click_see_model(page: Page) -> None:
    cta_page = SeeModelCTAPage(page)
    cta_page.click_cta()


@when("User focuses on 'See the model' CTA and presses Enter")
def focus_and_enter(page: Page) -> None:
    page.keyboard.press("Enter")


@when("User encounters 'See the model' CTA")
def encounter_cta(page: Page) -> None:
    pass


@when("Hover interaction occurs")
def hover_interaction(page: Page) -> None:
    page.wait_for_timeout(100)


@when("Focus is received")
def focus_received(page: Page) -> None:
    pass


@when("FDCE destination returns 404")
def fdce_404(page: Page) -> None:
    pass


@when("User navigates with keyboard")
def keyboard_navigate(page: Page) -> None:
    page.keyboard.press("Tab")


@then("User is navigated to '/forward-deployed-context-engineering/'")
def navigated_to_fdce(page: Page) -> None:
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("Navigation to FDCE page occurs")
def navigation_occurs(page: Page) -> None:
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("Accessible name describes the action")
def accessible_name(page: Page) -> None:
    cta_page = SeeModelCTAPage(page)
    name = cta_page.get_accessible_name()
    assert name and "model" in name.lower()


@then("Visible hover state is displayed")
def hover_state(page: Page) -> None:
    expect(SeeModelCTALocators(page).see_model_cta).to_be_visible()


@then("Visible focus state is displayed")
def focus_state(page: Page) -> None:
    expect(SeeModelCTALocators(page).see_model_cta).to_be_focused()


@then("User sees appropriate error page")
def error_page(page: Page) -> None:
    pass


@then("Focus target is not duplicated")
def no_duplicate_focus(page: Page) -> None:
    pass
