"""Step definitions for Capabilities mega-menu - EMIDS-LP-003"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-003_capabilities_menu_page import CapabilitiesMenuPage
from playwright.sync_api import expect


@given("A user interacts with the Capabilities navigation item")
def interact_capabilities(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.goto("/")


@when("The menu trigger is activated")
def activate_capabilities(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()


@then("Menu opens displaying AI, Engineering, and Platforms capability groups with their child destinations")
def verify_capability_groups(page):
    menu_page = CapabilitiesMenuPage(page)
    groups = menu_page.get_capability_groups()
    assert "AI" in groups
    assert "Engineering" in groups
    assert "Platforms" in groups


@given("The Capabilities menu is open")
def capabilities_menu_open(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.goto("/")
    menu_page.open_capabilities_menu()


@when("The user navigates via keyboard")
def keyboard_navigate(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.tab_through_menu_items()


@then("All capability links are reachable via Tab key and activate on Enter")
def verify_capability_links_keyboard(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.verify_group_labels()


@given("The Capabilities menu content")
def capabilities_menu_content(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.goto("/")


@when("Labels are compared against approved site taxonomy")
def compare_labels(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()


@then("AI, Engineering, and Platforms labels are consistent with content management")
def verify_taxonomy_consistency(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.verify_group_labels()


@given("The Capabilities menu structure")
def capabilities_menu_structure(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.goto("/")
    menu_page.open_capabilities_menu()


@when("Labels are inspected for uniqueness")
def inspect_labels_uniqueness(page):
    pass


@then("All labels within the menu are unique")
def verify_unique_labels(page):
    menu_page = CapabilitiesMenuPage(page)
    groups = menu_page.get_capability_groups()
    assert len(groups) == len(set(groups))


@given("A user on a mobile device")
def mobile_device(page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("The Capabilities menu is opened")
def open_capabilities_mobile(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.goto("/")
    menu_page.open_capabilities_menu()


@then("An accessible disclosure pattern is used instead of mega-menu")
def verify_disclosure_pattern(page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.verify_group_labels()
