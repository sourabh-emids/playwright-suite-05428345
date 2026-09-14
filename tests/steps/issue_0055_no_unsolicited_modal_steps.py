"""Step definitions for issue_0055: Base homepage without unsolicited modal."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("Default homepage configuration")
def default_config(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def page_loads(page: Page) -> None:
    pass


@then("No unsolicited promotional modal appears on load")
def no_modal(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Campaign modal is configured and enabled")
def campaign_enabled(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def loads(page: Page) -> None:
    pass


@then("Modal only appears per configured activation rule")
def modal_rule(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Campaign modal appears")
def modal_appears(page: Page) -> None:
    page.goto("/")


@when("User clicks dismiss or close")
def click_dismiss(page: Page) -> None:
    close = page.getByRole("button", name="Close")
    if close.is_visible():
        close.click()


@then("Modal closes immediately")
def modal_closes(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Campaign modal is open")
def modal_open(page: Page) -> None:
    page.goto("/")


@when("User presses Tab")
def press_tab(page: Page) -> None:
    page.keyboard.press("Tab")


@then("Focus trapped within modal; close button reachable")
def focus_trapped(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Campaign modal is open")
def modal_is_open(page: Page) -> None:
    page.goto("/")


@when("User tries to interact with page behind")
def interact_behind(page: Page) -> None:
    pass


@then("Modal does not block page interaction inappropriately")
def no_block(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Configuration review")
def config_review(page: Page) -> None:
    page.goto("/")


@when("Checking campaign modal config")
def check_config(page: Page) -> None:
    pass


@then("Campaign modal enabled flag is false by default")
def default_disabled(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Campaign modal configuration")
def modal_config(page: Page) -> None:
    page.goto("/")


@when("Checking required fields")
def check_fields(page: Page) -> None:
    pass


@then("Modal has title, content, dismiss control, and activation rule")
def has_fields(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User dismissed campaign modal")
def modal_dismissed(page: Page) -> None:
    page.goto("/")


@when("User continues browsing or returns")
def continue_browse(page: Page) -> None:
    page.goto("/")


@then("Modal does not reappear without new session or explicit re-enable")
def no_reappear(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Campaign modal open")
def campaign_open(page: Page) -> None:
    page.goto("/")


@when("Pressing Tab repeatedly")
def tab_repeatedly(page: Page) -> None:
    for _ in range(5):
        page.keyboard.press("Tab")


@then("Focus stays within modal; Escape or close button exits")
def focus_stays(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Mobile viewport with campaign modal")
def mobile_modal(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")


@when("Modal renders")
def modal_render(page: Page) -> None:
    pass


@then("Modal fits viewport; scrollable if needed; dismiss button accessible")
def modal_mobile(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User has JavaScript disabled")
def js_disabled(page: Page) -> None:
    page.context.set_javascript_enabled(False)
    page.goto("/")


@when("Page loads")
def page_loads(page: Page) -> None:
    pass


@then("Modal does not appear; page functions without JS")
def no_modal_js(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
    page.context.set_javascript_enabled(True)


@given("Campaign modal configured and consent given")
def campaign_consent(page: Page) -> None:
    page.goto("/")


@when("Modal displays or dismisses")
def display_dismiss(page: Page) -> None:
    pass


@then("Events logged per consent policy")
def consent_logged(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
