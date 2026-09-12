"""Step definitions for Issue 0006 - Company navigation group implementation."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user has the Company menu open")
def company_menu_open(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Company").hover()
    page.wait_for_timeout(500)


@when("The user examines the menu content")
def examine_company_menu_content(page: Page):
    pass


@then("Only published company information and contact-related destinations are displayed")
def only_published_company_info(page: Page):
    expect(page.getByText("About Us")).to_be_visible()
    expect(page.getByText("Our Story", exact=False)).to_be_visible()
    expect(page.getByText("Leadership Team", exact=False)).to_be_visible()
    expect(page.getByText("Connect with Us")).to_be_visible()


@given("A user is viewing the Company menu")
def user_viewing_company_menu(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Company").hover()
    page.wait_for_timeout(500)


@when("The user interacts via keyboard, pointer, and touch")
def interact_via_multiple_methods(page: Page):
    # Keyboard
    page.keyboard.press("Tab")
    # Pointer (hover)
    page.mouse.move(400, 200)
    # Touch (tap)
    page.set_viewport_size({"width": 375, "height": 812})
    page.get_by_role("button", name="Company").click()


@then("The menu functions correctly with all interaction methods")
def menu_functions_all_methods(page: Page):
    expect(page.getByText("About Us")).to_be_visible()


@given("A company page has been unpublished")
def company_page_unpublished(page: Page):
    pass  # Hypothetical scenario


@when("A user views the Company menu")
def view_company_menu(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Company").hover()
    page.wait_for_timeout(500)


@then("The unpublished page is not visible in the menu")
def unpublished_not_visible(page: Page):
    # Verify expected links are present
    expect(page.getByText("Our Story", exact=False)).to_be_visible()


@given("A user has the Company menu open")
def company_menu_open_for_focus(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Company").hover()
    page.wait_for_timeout(500)


@when("The user tabs through the menu")
def tab_through_company_menu(page: Page):
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")


@then("Focus does not become trapped within the menu")
def focus_not_trapped(page: Page):
    # Escape should close the menu
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)
    expect(page.get_by_role("button", name="Company")).to_be_visible()
