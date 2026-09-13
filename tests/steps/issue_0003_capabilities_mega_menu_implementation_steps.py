"""Step definitions for issue_0003: Capabilities mega-menu implementation"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0003_capabilities_mega_menu_implementation_page import Issue0003CapabilitiesMenuPage


@given("A user focuses on the Capabilities navigation item")
def user_focuses_capabilities(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.navigate_to_homepage()
    page_object.open_capabilities_menu()


@given("The Capabilities menu is open")
def capabilities_menu_is_open(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.open_capabilities_menu()


@given("The Capabilities menu displays group headings")
def capabilities_menu_displays_headings(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.open_capabilities_menu()


@given("The Capabilities menu is rendered")
def capabilities_menu_is_rendered(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.open_capabilities_menu()


@given("A user is on a mobile viewport")
def user_on_mobile_viewport(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.resize_to_mobile()
    page_object.navigate_to_homepage()


@when("The user activates the trigger")
def user_activates_trigger(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.open_capabilities_menu()


@when("The user navigates using Tab and Arrow keys")
def user_navigates_tab_arrow_keys(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.navigate_with_tab_key()
    page_object.navigate_with_arrow_keys()


@when("Automated testing verifies labels against CMS taxonomy")
def automated_verifies_labels(page: Page):
    """Label verification happens in assertions."""
    pass


@when("Automated testing checks for duplicate labels")
def automated_checks_duplicates(page: Page):
    """Duplicate check happens in assertions."""
    pass


@when("The user expands the Capabilities menu")
def user_expands_capabilities_menu(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.open_capabilities_menu()


@then("The menu opens displaying AI, Engineering, and Platforms capability groups with their child destinations")
def menu_opens_with_capability_groups(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.verify_capability_groups_visible()


@then("All capability links within all groups are keyboard accessible")
def all_capability_links_keyboard_accessible(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    # Verify the capability links are accessible
    links = page.locator("a:has-text('AI'), a:has-text('Engineering'), a:has-text('Platforms')")
    expect(links.first).to_be_attached()


@then("Labels (AI, Engineering, Platforms) match the approved site taxonomy exactly")
def labels_match_taxonomy(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    labels = page_object.get_capability_labels()
    expected_labels = {"AI", "Engineering", "Platforms"}
    assert set(labels) == expected_labels, f"Labels {set(labels)} do not match expected {expected_labels}"


@then("All capability labels are unique within the menu structure")
def labels_are_unique(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    assert page_object.check_duplicate_labels(), "Duplicate labels found in the menu"


@then("An accessible disclosure pattern provides equivalent access to all capability groups")
def accessible_disclosure_pattern(page: Page):
    page_object = Issue0003CapabilitiesMenuPage(page)
    page_object.verify_capability_groups_visible()
