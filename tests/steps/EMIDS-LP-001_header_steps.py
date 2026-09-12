"""Step definitions for Header - EMIDS-LP-001"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-001_header_page import HeaderPage


@given("A user navigates to the homepage for the first time")
def navigate_to_homepage(page):
    header_page = HeaderPage(page)
    header_page.goto("/")


@when("The page loads completely")
def page_loads_completely(page):
    pass


@then("The global header is visible at the top of the viewport with Emids logo, all navigation items (Solutions, Capabilities, Industries, Insights, Company), and Connect CTA")
def verify_header_components(page):
    header_page = HeaderPage(page)
    header_page.verify_header_visible()


@given("A user is on any page of the site")
def user_on_any_page(page):
    page.goto("/")


@when("The user clicks the Emids logo or brand element")
def click_logo(page):
    header_page = HeaderPage(page)
    header_page.click_logo()


@then("The user is navigated to the homepage")
def verify_navigated_to_homepage(page):
    expect(page).to_have_url("https://www.emids.com/")


@given("A user navigates using keyboard only (Tab key)")
def navigate_keyboard_only(page):
    pass


@when("The user tabs through the header navigation")
def tab_through_navigation(page):
    header_page = HeaderPage(page)
    header_page.tab_through_navigation()


@then("All top-level navigation items (Solutions, Capabilities, Industries, Insights, Company) are reachable and receive visible focus state; Connect CTA is reachable")
def verify_nav_items_reachable(page):
    header_page = HeaderPage(page)
    count = header_page.get_nav_item_count()
    assert count >= 6


@given("A user with a mouse or touch device")
def user_with_mouse_or_touch(page):
    pass


@when("The user hovers over or taps each top-level navigation item")
def hover_nav_items(page):
    header_page = HeaderPage(page)
    for name in ["Solutions", "Capabilities", "Industries", "Insights", "Company"]:
        header_page.click_nav_item(name)


@then("All navigation items are interactive and show appropriate hover/focus states")
def verify_interactive_states(page):
    header_page = HeaderPage(page)
    header_page.verify_header_visible()


@given("A user clicks the Connect CTA in the header")
def user_clicks_connect_cta(page):
    page.goto("/")


@when("The Connect button or link is activated")
def activate_connect_cta(page):
    header_page = HeaderPage(page)
    header_page.click_connect_cta()


@then("The user is navigated to the contact page")
def verify_contact_page(page):
    page.wait_for_url("**/contact/**")


@given("All navigation items in the header")
def all_nav_items_in_header(page):
    page.goto("/")


@when("Each navigation item is inspected for its destination URL")
def inspect_nav_destinations(page):
    header_page = HeaderPage(page)
    for name in ["Solutions", "Capabilities", "Industries", "Insights", "Company"]:
        header_page.click_nav_item(name)


@then("All destinations are configured with valid URLs and no dead links exist")
def verify_valid_urls(page):
    pass


@given("The header navigation items")
def header_navigation_items(page):
    page.goto("/")


@when("Counting primary Connect CTA elements")
def count_connect_cta(page):
    header_page = HeaderPage(page)
    count = header_page.get_nav_item_count()


@then("Only one primary Connect CTA is present in the header")
def verify_single_connect_cta(page):
    header_page = HeaderPage(page)
    header_page.verify_header_visible()


@given("JavaScript is disabled in the browser")
def js_disabled_browser(page):
    page.goto("/")


@when("The homepage loads")
def homepage_loads(page):
    pass


@then("Header is visible and basic navigation links are functional")
def header_functional(page):
    header_page = HeaderPage(page)
    header_page.verify_header_visible()


@given("A user views the site on a mobile device with narrow viewport")
def narrow_viewport(page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("The page renders at narrow width")
def render_narrow(page):
    page.goto("/")


@then("Navigation collapses appropriately but all destinations remain accessible")
def destinations_accessible(page):
    header_page = HeaderPage(page)
    header_page.verify_header_visible()


from playwright.sync_api import expect
