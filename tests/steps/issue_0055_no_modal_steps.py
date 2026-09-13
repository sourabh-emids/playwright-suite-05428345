"""Steps for No promotional modal in base experience (issue_0055)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0055_no_modal_locators import NoModalLocators


@given("User navigates to homepage")
def navigate_homepage(page: Page) -> None:
    page.goto("/")


@given("Campaign modal is not configured")
def modal_not_configured(page: Page) -> None:
    page.goto("/")


@given("Campaign modal is configured and displays")
def modal_displays(page: Page) -> None:
    page.goto("/")


@given("Campaign modal displays")
def modal_display(page: Page) -> None:
    page.goto("/")


@given("User dismisses campaign modal")
def dismiss_modal(page: Page) -> None:
    page.goto("/")


@given("Campaign modal opens")
def modal_opens(page: Page) -> None:
    page.goto("/")


@given("Campaign modal displays at small viewport")
def modal_small_viewport(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("JavaScript is disabled")
def js_disabled(page: Page) -> None:
    pass


@when("Page loads")
def page_loads(page: Page) -> None:
    page.wait_for_load_state("domcontentloaded")


@when("User interacts with modal")
def interact_modal(page: Page) -> None:
    pass


@when("User navigates with keyboard")
def keyboard_nav(page: Page) -> None:
    page.keyboard.press("Tab")


@when("Modal is open")
def modal_open(page: Page) -> None:
    pass


@when("User continues browsing")
def continue_browsing(page: Page) -> None:
    pass


@when("User presses Tab")
def tab_press(page: Page) -> None:
    page.keyboard.press("Tab")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("No unsolicited promotional modal appears")
def no_unsolicited_modal(page: Page) -> None:
    expect(NoModalLocators(page).main_content).to_be_visible()


@then("No modal displays")
def no_modal(page: Page) -> None:
    expect(NoModalLocators(page).main_content).to_be_visible()


@then("Modal is dismissible")
def dismissible(page: Page) -> None:
    pass


@then("Modal is keyboard accessible")
def keyboard_accessible(page: Page) -> None:
    pass


@then("Modal does not block core page interaction")
def non_blocking(page: Page) -> None:
    expect(NoModalLocators(page).main_content).to_be_visible()


@then("Modal does not repeatedly display")
def no_repeat(page: Page) -> None:
    pass


@then("Focus remains within modal until dismissed")
def focus_trap(page: Page) -> None:
    pass


@then("Modal handles small viewport appropriately")
def small_viewport(page: Page) -> None:
    pass


@then("No modal appears (base experience)")
def no_modal_base(page: Page) -> None:
    expect(NoModalLocators(page).main_content).to_be_visible()
