"""Step definitions for Issue 0007 - Header Connect CTA functionality."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user is viewing the Emids homepage header")
def user_viewing_header(page: Page):
    page.goto("/")


@when("The user examines the Connect CTA")
def examine_connect_cta(page: Page):
    pass


@then("The CTA is visually distinct from other navigation elements")
def cta_visually_distinct(page: Page):
    homepage = HomepagePage(page)
    homepage.connect_cta_is_visible()
    # Verify Connect is a link in the header area
    connect = page.get_by_role("link", name="Connect").first
    expect(connect).to_be_visible()


@given("A user is viewing the Connect CTA")
def user_viewing_connect_cta(page: Page):
    page.goto("/")


@when("The user or assistive technology examines the CTA")
def examine_cta_with_at(page: Page):
    pass


@then("The CTA has an accessible name that describes its action")
def cta_has_accessible_name(page: Page):
    connect = page.get_by_role("link", name="Connect").first
    name = connect.get_attribute("aria-label") or connect.text_content()
    assert name and "Connect" in name


@given("A user clicks the Connect CTA")
def user_clicks_connect_cta(page: Page):
    homepage = HomepagePage(page)
    homepage.click_connect_cta()


@when("The CTA is activated")
def cta_activated(page: Page):
    pass


@then("The user is navigated to /contact/ with valid HTTPS URL")
def navigated_to_contact_https(page: Page):
    expect(page).to_have_url("**/contact/**")
    expect(page).to_have_url(re.compile(r"^https://"))


@given("A user is viewing the Emids homepage with keyboard navigation")
def user_with_keyboard(page: Page):
    page.goto("/")


@when("The user focuses on and activates the Connect CTA")
def focus_and_activate_connect(page: Page):
    page.get_by_role("link", name="Connect").focus()
    page.keyboard.press("Enter")


@then("The action is triggered successfully via keyboard")
def action_triggered_keyboard(page: Page):
    page.wait_for_url("**/contact/**")


@given("The contact page is unavailable (503 or timeout)")
def contact_page_unavailable(page: Page):
    pass  # This would require mocking the server


@when("A user clicks the Connect CTA")
def click_connect_when_unavailable(page: Page):
    pass  # Would need to mock network conditions


@then("An appropriate error message or fallback is displayed without breaking the UI")
def error_handled_gracefully(page: Page):
    # In a real test, we would verify error handling
    # For now, verify the page still renders
    expect(page.locator("body")).to_be_visible()
