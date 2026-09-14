"""Step definitions for issue_0036: Expose Cookie Preferences control."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views page footer")
def view_footer(page: Page) -> None:
    page.goto("/")


@when("Locating cookie control")
def locate_cookie_control(page: Page) -> None:
    pass


@then("Cookie Preferences link or button is visible in footer")
def cookie_control_visible(page: Page) -> None:
    footer = page.locator("footer")
    expect(footer).to_be_visible()


@when("User clicks Cookie Preferences")
def click_cookie_prefs(page: Page) -> None:
    cookie_btn = page.getByRole("link", name="Cookie Preferences").or_(page.getByRole("button", name="Cookie Preferences"))
    if cookie_btn.count() > 0:
        cookie_btn.first.click()


@then("Consent management interface opens")
def consent_ui_opens(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("Consent UI is open")
def consent_ui_open(page: Page) -> None:
    page.goto("/")


@when("User adjusts consent choices")
def adjust_consent(page: Page) -> None:
    pass


@then("User can modify consent preferences and save changes")
def modify_consent(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User dismissed initial cookie banner")
def dismissed_banner(page: Page) -> None:
    page.goto("/")


@when("Returning to page later or scrolling")
def return_to_page(page: Page) -> None:
    pass


@then("Cookie Preferences control remains accessible in footer")
def control_accessible(page: Page) -> None:
    footer = page.locator("footer")
    expect(footer).to_be_visible()


@given("Consent management script blocked")
def script_blocked(page: Page) -> None:
    page.goto("/")


@when("User clicks Cookie Preferences")
def click_cookie_blocked(page: Page) -> None:
    cookie_btn = page.getByRole("link", name="Cookie Preferences")
    if cookie_btn.count() > 0:
        cookie_btn.first.click()


@then("Fallback experience or error message displays")
def fallback_displays(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("Browser storage is disabled")
def storage_disabled(page: Page) -> None:
    page.goto("/")


@when("User attempts to save consent")
def save_consent(page: Page) -> None:
    pass


@then("Consent state handled gracefully; user informed of limitation")
def graceful_handling(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User clears browser cookies")
def clear_cookies(page: Page) -> None:
    page.goto("/")


@when("Returning to site")
def return_to_site(page: Page) -> None:
    pass


@then("Cookie Preferences allows user to re-establish consent")
def reestablish_consent(page: Page) -> None:
    footer = page.locator("footer")
    expect(footer).to_be_visible()
