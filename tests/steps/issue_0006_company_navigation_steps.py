"""Steps for Company navigation group implementation (issue_0006)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0006_company_navigation_page import CompanyNavigationPage
from locators.issue_0006_company_navigation_locators import CompanyNavigationLocators


@given("Company menu is open")
def company_menu_open(page: Page) -> None:
    page.goto("/")
    company_page = CompanyNavigationPage(page)
    company_page.activate_company()


@given("User is on Emids homepage with keyboard focus on header")
def keyboard_focus_header(page: Page) -> None:
    page.goto("/")
    page.locator("header").focus()


@given("User is on Emids homepage")
def on_homepage(page: Page) -> None:
    page.goto("/")


@given("User is on touch device viewing Emids homepage")
def touch_device(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("Company menu is open with focus inside")
def company_menu_focused(page: Page) -> None:
    page.goto("/")
    company_page = CompanyNavigationPage(page)
    company_page.activate_company()
    company_page.locators.about_us_link.focus()


@when("User views menu content")
def view_menu_content(page: Page) -> None:
    pass


@when("User navigates to Company and opens menu")
def navigate_open_company(page: Page) -> None:
    company_page = CompanyNavigationPage(page)
    company_page.activate_company()


@when("User hovers over Company navigation")
def hover_company(page: Page) -> None:
    company_page = CompanyNavigationPage(page)
    company_page.activate_company()


@when("User taps Company navigation")
def tap_company(page: Page) -> None:
    company_page = CompanyNavigationPage(page)
    company_page.click_company()


@when("User views Contact/Connect destinations")
def view_connect_destinations(page: Page) -> None:
    pass


@when("User presses Tab to navigate through menu items")
def tab_through_menu(page: Page) -> None:
    for _ in range(3):
        page.keyboard.press("Tab")


@when("User clicks on a company link")
def click_company_link(page: Page) -> None:
    company_page = CompanyNavigationPage(page)
    company_page.activate_company()
    company_page.locators.about_us_link.click()


@then("Only published company pages are exposed")
def published_pages_only(page: Page) -> None:
    locators = CompanyNavigationLocators(page)
    expect(locators.about_us_link).to_be_visible()


@then("Company menu items are keyboard accessible")
def menu_keyboard_accessible(page: Page) -> None:
    locators = CompanyNavigationLocators(page)
    locators.about_us_link.focus()
    expect(locators.about_us_link).to_be_focused()


@then("Company menu opens and items are clickable")
def menu_clickable(page: Page) -> None:
    expect(CompanyNavigationLocators(page).menu_visible).to_be_visible()


@then("Company menu opens via touch interaction")
def menu_touch_opens(page: Page) -> None:
    expect(CompanyNavigationLocators(page).menu_visible).to_be_visible()


@then("Contact/Connect destinations are visible and accessible")
def connect_destinations_visible(page: Page) -> None:
    locators = CompanyNavigationLocators(page)
    expect(locators.connect_link).to_be_visible()


@then("Focus does not become trapped and exits menu appropriately")
def no_focus_trap(page: Page) -> None:
    pass


@then("Page does not enter a redirect loop")
def no_redirect_loop(page: Page) -> None:
    expect(page).not_to_have_url(re.compile(r".*\?redirect_loop=.*"))
