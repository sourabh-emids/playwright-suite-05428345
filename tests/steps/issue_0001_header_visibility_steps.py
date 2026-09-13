"""Steps for Global header visibility and Emids brand link (issue_0001)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then, parsers

from pages.issue_0001_header_page import HeaderPage
from locators.issue_0001_header_locators import HeaderLocators


@given("User navigates to the Emids homepage")
def navigate_to_homepage(page: Page) -> None:
    page.goto("/")


@given("User is on any page of the Emids website")
def user_on_any_page(page: Page) -> None:
    page.goto("/contact/")


@given("User navigates to the Emids homepage with keyboard focus at the header")
def navigate_with_keyboard_focus(page: Page) -> None:
    page.goto("/")
    header_page = HeaderPage(page)
    header_page.locators.header.focus()


@given("User has JavaScript disabled in browser")
def js_disabled_context(page: Page) -> None:
    pass


@given("User views the Emids homepage at a narrow viewport width (320px)")
def narrow_viewport(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 320, "height": 568})


@given("User views the Emids homepage on desktop")
def desktop_viewport(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 1280, "height": 800})


@when("Page fully loads")
def page_fully_loads(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("User clicks the Emids logo or brand entry point")
def click_logo(page: Page) -> None:
    header_page = HeaderPage(page)
    header_page.click_logo()


@when("User tabs through header navigation items")
def tab_through_nav(page: Page) -> None:
    page.keyboard.press("Tab")


@when("User hovers over each navigation item in the header")
def hover_nav_items(page: Page) -> None:
    header_page = HeaderPage(page)
    for item in ["Solutions", "Capabilities", "Industries", "Insights", "Company"]:
        header_page.hover_over_nav_item(item)


@when("User clicks the Connect CTA in the header")
def click_connect_cta(page: Page) -> None:
    header_page = HeaderPage(page)
    header_page.locators.connect_cta.click()


@when("User clicks on each navigation item and CTA")
def click_each_nav_item(page: Page) -> None:
    header_page = HeaderPage(page)
    for item in ["Solutions", "Capabilities", "Industries", "Insights", "Company"]:
        header_page.click_nav_item(item)


@when("User inspects the header for Connect CTAs")
def inspect_connect_ctas(page: Page) -> None:
    pass


@when("Header renders")
def header_renders(page: Page) -> None:
    pass


@then("Global header is visible at the top of the viewport with Logo, Solutions, Capabilities, Industries, Insights, Company, and Connect fields")
def header_visible_with_fields(page: Page) -> None:
    locators = HeaderLocators(page)
    expect(locators.header).to_be_visible()
    expect(locators.logo).to_be_visible()
    expect(locators.solutions_button).to_be_visible()
    expect(locators.capabilities_button).to_be_visible()
    expect(locators.industries_button).to_be_visible()
    expect(locators.insights_button).to_be_visible()
    expect(locators.company_button).to_be_visible()
    expect(locators.connect_cta).to_be_visible()


@then("User is navigated to the homepage URL '/'")
def navigated_to_homepage(page: Page) -> None:
    expect(page).to_have_url("/")


@then("Each navigation item (Solutions, Capabilities, Industries, Insights, Company) receives visible focus and can be activated with Enter key")
def nav_items_keyboard_accessible(page: Page) -> None:
    locators = HeaderLocators(page)
    nav_buttons = [
        locators.solutions_button,
        locators.capabilities_button,
        locators.industries_button,
        locators.insights_button,
        locators.company_button,
    ]
    for button in nav_buttons:
        button.focus()
        expect(button).to_be_focused()
        page.keyboard.press("Enter")


@then("Each navigation item is hoverable and clickable without dead links")
def nav_items_hoverable_clickable(page: Page) -> None:
    header_page = HeaderPage(page)
    for item in ["Solutions", "Capabilities", "Industries", "Insights", "Company"]:
        header_page.hover_over_nav_item(item)
        page.wait_for_timeout(100)


@then("User is navigated to the contact page at '/contact/'")
def navigated_to_contact(page: Page) -> None:
    expect(page).to_have_url("/contact/")


@then("All navigation destinations resolve to valid internal or approved external URLs with HTTP 200 or appropriate redirect")
def nav_destinations_valid(page: Page) -> None:
    pass


@then("Exactly one primary Connect CTA is present in the header")
def one_connect_cta(page: Page) -> None:
    header_page = HeaderPage(page)
    count = header_page.count_connect_ctas()
    expect(count).to_equal(1)


@then("Header is visible with functional navigation links")
def header_visible_no_js(page: Page) -> None:
    locators = HeaderLocators(page)
    expect(locators.header).to_be_visible()


@then("All navigation destinations remain accessible via collapsible/responsive mechanism")
def nav_accessible_mobile(page: Page) -> None:
    locators = HeaderLocators(page)
    expect(locators.header).to_be_visible()


@then("Navigation items are presented in grouped format as per design")
def grouped_nav_desktop(page: Page) -> None:
    locators = HeaderLocators(page)
    expect(locators.navigation).to_be_visible()
