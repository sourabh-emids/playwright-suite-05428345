"""Step definitions for Issue 0001 - Header visibility and Emids branding."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user navigates to the Emids homepage")
def navigate_to_homepage(page: Page):
    homepage = HomepagePage(page)
    homepage.goto()


@when("The page finishes loading")
def page_finishes_loading(page: Page):
    page.wait_for_load_state("networkidle")


@then("The global header is visible and displays Emids branding")
def header_visible_with_branding(page: Page):
    homepage = HomepagePage(page)
    homepage.header_is_visible()
    homepage.emids_logo_is_visible()


@given("A user is on any page of the Emids site")
def user_on_any_page(page: Page):
    pass  # Already on the page


@when("The user clicks the Emids logo or brand link")
def click_emids_logo(page: Page):
    homepage = HomepagePage(page)
    homepage.click_emids_logo()


@then("The user is navigated to the homepage")
def navigated_to_homepage(page: Page):
    expect(page).to_have_url("https://www.emids.com/")


@given("A user is viewing the Emids homepage with keyboard-only navigation")
def user_with_keyboard_navigation(page: Page):
    pass


@when("The user tabs through the header navigation items")
def tab_through_header(page: Page):
    homepage = HomepagePage(page)
    # Press Tab to focus on first element, then continue
    page.keyboard.press("Tab")


@then("All top-level navigation items are reachable and focusable")
def all_nav_items_focusable(page: Page):
    homepage = HomepagePage(page)
    nav_items = homepage.navigation_items_are_visible()
    assert len(nav_items) == 5


@given("A user is viewing the Emids homepage")
def user_viewing_homepage(page: Page):
    pass


@when("The user clicks the Connect CTA in the header")
def click_connect_cta(page: Page):
    homepage = HomepagePage(page)
    homepage.click_connect_cta()


@then("The user is navigated to the contact experience at /contact/")
def navigated_to_contact(page: Page):
    expect(page).to_have_url("**/contact/")
    contact_page = page.locator("form")
    expect(contact_page).to_be_visible()


@given("A user is viewing the Emids homepage header")
def user_viewing_header(page: Page):
    pass


@when("The user clicks on each navigation item")
def click_each_nav_item(page: Page):
    homepage = HomepagePage(page)
    # Click each navigation item and verify navigation works
    nav_items = ["Solutions", "Capabilities", "Industries", "Insights", "Company"]
    for item in nav_items:
        page.get_by_role("button", name=item).click()
        page.wait_for_timeout(300)
        page.keyboard.press("Escape")
        page.wait_for_timeout(200)


@then("All navigation destinations resolve to valid pages with no 404 errors")
def all_destinations_valid(page: Page):
    # Verify no 404 errors occurred
    errors = page.evaluate("() => window.performance.getEntriesByType('resource').filter(r => r.responseStatus === 404)")
    assert len(errors) == 0, f"404 errors found: {errors}"


@then("Only one primary Connect CTA is visible in the header")
def only_one_connect_cta(page: Page):
    homepage = HomepagePage(page)
    homepage.connect_cta_is_visible()
    # Verify only one Connect link in header
    connect_links = page.locator("header a:has-text('Connect')")
    expect(connect_links).to_have_count(1)
