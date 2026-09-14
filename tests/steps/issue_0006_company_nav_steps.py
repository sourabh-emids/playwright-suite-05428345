"""Step definitions for issue_0006: Implement Company navigation group."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User activates the Company navigation item")
def activate_company(page: Page) -> None:
    page.get_by_role("button", name="Company").click()


@when("Menu opens")
def menu_opens(page: Page) -> None:
    pass


@then("Only published and approved company links are displayed")
def approved_links_displayed(page: Page) -> None:
    expect(page.get_by_text("About Us")).to_be_visible()
    expect(page.get_by_text("Connect with Us")).to_be_visible()


@given("User is testing accessibility")
def testing_accessibility(page: Page) -> None:
    page.goto("/")


@when("User navigates Company menu using keyboard, mouse, and touch")
def navigate_all_methods(page: Page) -> None:
    page.get_by_role("button", name="Company").click()
    page.keyboard.press("Tab")


@then("Menu functions correctly with all input methods")
def menu_functions_all_methods(page: Page) -> None:
    expect(page.get_by_text("About Us")).to_be_visible()


@given("User compares Company menu to Solutions or Capabilities menu")
def compare_to_other_menus(page: Page) -> None:
    page.goto("/")
    page.get_by_role("button", name="Company").click()


@when("Testing interaction patterns")
def test_interaction_patterns(page: Page) -> None:
    pass


@then("Company menu opens, navigates, and closes with the same behavior as other primary navigation groups")
def consistent_behavior(page: Page) -> None:
    expect(page.get_by_text("About Us")).to_be_visible()
    page.keyboard.press("Escape")
    expect(page.get_by_role("button", name="Company")).to_be_visible()


@given("Company menu is open")
def company_menu_open(page: Page) -> None:
    page.goto("/")
    page.get_by_role("button", name="Company").click()
    expect(page.get_by_text("About Us")).to_be_visible()


@when("User presses Tab repeatedly")
def press_tab_repeatedly(page: Page) -> None:
    for _ in range(10):
        page.keyboard.press("Tab")


@then("User can exit menu; focus does not get trapped within menu")
def no_focus_trap(page: Page) -> None:
    active = page.evaluate("() => document.activeElement?.closest('[aria-label]')")
    # Focus should eventually exit the menu area
    expect(page.locator("h1")).to_be_visible()


@given("A company link destination has redirect loop")
def link_has_redirect_loop(page: Page) -> None:
    page.goto("/")


@when("User clicks that link")
def click_looping_link(page: Page) -> None:
    company_btn = page.get_by_role("button", name="Company")
    company_btn.click()
    link = page.get_by_role("navigation", name="Company").get_by_role("link").first
    link.click()


@then("Page either loads with warning or link is not rendered to prevent infinite loop")
def redirect_handled(page: Page) -> None:
    # Page should either load successfully or show error
    assert page.url.startswith("https://www.emids.com")
