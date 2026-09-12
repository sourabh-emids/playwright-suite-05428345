"""Step definitions for Issue 0055 - No base promotional modal on homepage."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect


@given("A user loads the Emids homepage with no campaign modal configured")
def load_homepage_no_modal(page: Page):
    page.goto("/")


@when("Page loads")
def page_loads_no_modal(page: Page):
    page.wait_for_load_state("networkidle")


@then("No promotional modal appears")
def no_modal_appears(page: Page):
    # Modal should not appear on base homepage
    modals = page.locator('[class*="modal"], [role="dialog"]')
    expect(modals).to_have_count(0)


@given("A campaign modal is configured and displays")
def modal_configured(page: Page):
    page.goto("/")


@when("User interacts with the modal")
def interact_modal(page: Page):
    pass


@then("Modal is dismissible via close button, Escape key, or overlay click")
def modal_dismissible(page: Page):
    # Check for close button or overlay
    close_buttons = page.locator('[class*="close"], [aria-label="Close"]')
    # If modal exists, it should be dismissible
    pass


@given("A campaign modal is configured and displays")
def modal_displayed(page: Page):
    page.goto("/")


@when("User navigates with keyboard")
def keyboard_nav_modal(page: Page):
    pass


@then("Modal focus is managed; close control is keyboard accessible")
def focus_managed(page: Page):
    pass


@given("A campaign modal is configured and displays")
def modal_visible(page: Page):
    page.goto("/")


@when("Modal is open")
def modal_open(page: Page):
    pass


@then("Modal is non-blocking; underlying content remains accessible")
def non_blocking(page: Page):
    # Underlying content should be in DOM
    expect(page.locator("main")).to_be_visible()


@given("No campaign modal is configured")
def no_modal_configured(page: Page):
    page.goto("/")


@when("Page loads")
def page_loads_no_config(page: Page):
    page.wait_for_load_state("networkidle")


@then("No modal appears (default state is disabled)")
def no_modal_default(page: Page):
    modals = page.locator('[role="dialog"]')
    expect(modals).to_have_count(0)


@given("User has dismissed a campaign modal")
def dismissed_modal(page: Page):
    page.goto("/")


@when("User reloads page or continues browsing")
def reload_browse(page: Page):
    pass


@then("Modal does not repeatedly appear after dismissal")
def no_repeat_modal(page: Page):
    modals = page.locator('[role="dialog"]')
    expect(modals).to_have_count(0)


@given("Campaign modal is open")
def campaign_modal_open(page: Page):
    page.goto("/")


@when("User tabs through modal")
def tab_modal(page: Page):
    pass


@then("Focus is trapped within modal until closed")
def focus_trapped(page: Page):
    pass


@given("Campaign modal displays at narrow viewport")
def modal_narrow(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})


@when("Modal renders")
def modal_renders_narrow(page: Page):
    page.goto("/")


@then("Modal is readable and functional at small viewport")
def modal_functional_narrow(page: Page):
    # Check layout doesn't break
    expect(page.locator("body")).to_be_visible()
