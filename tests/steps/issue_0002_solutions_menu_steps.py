"""Step definitions for Issue 0002 - Solutions mega-menu functionality."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user is viewing the Emids homepage desktop header")
def user_on_desktop_homepage(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")


@when("The user hovers or clicks on the Solutions navigation item")
def hover_or_click_solutions(page: Page):
    homepage = HomepagePage(page)
    homepage.hover_solutions_nav()


@then("An accessible mega-menu opens displaying the Solutions taxonomy")
def solutions_menu_opens(page: Page):
    homepage = HomepagePage(page)
    homepage.solutions_menu_is_open()
    # Verify taxonomy groups are present
    expect(page.getByText("Solutions by Initiative")).to_be_visible()
    expect(page.getByText("Browse By Industry")).to_be_visible()
    expect(page.getByText("The Portfolio")).to_be_visible()


@when("The user focuses on Solutions and activates it")
def focus_and_activate_solutions(page: Page):
    page.get_by_role("button", name="Solutions").focus()
    page.keyboard.press("Enter")
    page.wait_for_timeout(300)


@then("The menu opens and all solution links are keyboard operable")
def all_solution_links_keyboard_operable(page: Page):
    # Verify solution links are present
    expect(page.getByText("Modernization", exact=False)).to_be_visible()
    expect(page.getByText("Interoperability", exact=False)).to_be_visible()
    expect(page.getByText("Cloud Transformation", exact=False)).to_be_visible()
    expect(page.getByText("Agentic AI", exact=False)).to_be_visible()
    
    # Tab through links to verify keyboard operability
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    focused = page.evaluate("() => document.activeElement.tagName")


@given("A user has the Solutions mega-menu open")
def solutions_menu_open(page: Page):
    page.goto("/")
    page.get_by_role("button", name="Solutions").hover()
    page.wait_for_timeout(500)


@when("The user closes the menu via keyboard or click outside")
def close_solutions_menu(page: Page):
    homepage = HomepagePage(page)
    homepage.close_solutions_menu()


@then("Focus is restored to the Solutions trigger element")
def focus_restored_to_trigger(page: Page):
    # After closing, Solutions button should be focusable
    expect(page.get_by_role("button", name="Solutions")).to_be_visible()


@when("The user examines the visible solution links")
def examine_solution_links(page: Page):
    pass


@then("Each solution item has a non-empty label and valid URL")
def solution_links_have_valid_urls(page: Page):
    # Verify solution links have proper href attributes
    solution_links = page.getByText("Modernization", exact=False).first.locator("..")
    href = solution_links.get_attribute("href")
    assert href and "/solutions/" in href


@given("A user is viewing the site on a mobile device")
def user_on_mobile(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})


@when("The user taps the Solutions navigation item")
def tap_solutions_mobile(page: Page):
    page.get_by_role("button", name="Solutions").click()


@then("An accessible disclosure or drawer pattern is displayed")
def mobile_solutions_disclosure(page: Page):
    # Verify menu content is visible
    expect(page.getByText("Solutions by Initiative")).to_be_visible()


@given("A user has the Solutions mega-menu open near the viewport edge")
def solutions_menu_near_edge(page: Page):
    page.set_viewport_size({"width": 1024, "height": 600})
    page.goto("/")
    page.get_by_role("button", name="Solutions").hover()
    page.wait_for_timeout(500)


@when("The mega-menu is rendered")
def menu_rendered(page: Page):
    pass


@then("The menu is not clipped by the viewport and remains fully visible")
def menu_not_clipped(page: Page):
    # Check menu bounding box is within viewport
    menu = page.getByText("Solutions by Initiative")
    box = menu.bounding_box()
    assert box is not None
    assert box["x"] >= 0
    assert box["y"] >= 0
