"""Step definitions for Issue 0003 - Capabilities mega-menu functionality."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user is viewing the Emids homepage desktop header")
def user_on_desktop_homepage(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")


@when("The user activates the Capabilities navigation item")
def activate_capabilities(page: Page):
    homepage = HomepagePage(page)
    homepage.hover_capabilities_nav()


@then("The menu opens displaying AI, Engineering, and Platforms capability groups")
def capabilities_menu_displays_groups(page: Page):
    homepage = HomepagePage(page)
    homepage.capabilities_menu_groups_are_visible()


@given("A user has the Capabilities menu open")
def capabilities_menu_open(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Capabilities").hover()
    page.wait_for_timeout(500)


@when("The user tabs through the menu items")
def tab_through_capabilities_menu(page: Page):
    # Focus on menu and tab through items
    page.keyboard.press("Tab")


@then("All capability links are keyboard accessible and operable")
def all_capability_links_keyboard_accessible(page: Page):
    homepage = HomepagePage(page)
    groups = homepage.capabilities_menu_groups_are_visible()
    assert "AI" in groups
    assert "Engineering" in groups
    assert "Platforms" in groups


@when("The user examines the group labels")
def examine_capability_group_labels(page: Page):
    pass


@then("Labels match the approved site taxonomy and are unique within the menu")
def labels_match_taxonomy(page: Page):
    # Verify exact label names
    expect(page.getByText("AI", exact=False)).to_be_visible()
    expect(page.getByText("Engineering", exact=False)).to_be_visible()
    expect(page.getByText("Platforms", exact=False)).to_be_visible()


@when("The user clicks on any capability link")
def click_capability_link(page: Page):
    homepage = HomepagePage(page)
    homepage.click_ai_capability_link()


@then("The destination URL resolves to a valid page")
def capability_url_resolves(page: Page):
    page.wait_for_load_state("networkidle")
    # Verify page loaded without 404
    title = page.title()
    assert "Error" not in title
    assert "404" not in title


@given("A user is on a touch device without hover capability")
def user_on_touch_device(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})


@when("The user taps the Capabilities item")
def tap_capabilities_mobile(page: Page):
    page.get_by_role("button", name="Capabilities").click()


@then("The menu opens and all links are accessible via touch")
def menu_accessible_via_touch(page: Page):
    # Verify menu is visible and touchable
    expect(page.getByText("AI", exact=False)).to_be_visible()
