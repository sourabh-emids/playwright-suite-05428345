"""Step definitions for issue_0003: Capabilities Mega-Menu Implementation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.capabilities_menu_page import CapabilitiesMenuPage


@given("User is on page with header visible")
def on_page_with_header(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User activates the Capabilities menu trigger")
def activate_capabilities_menu(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()


@then("Capabilities menu opens predictably; second activation closes it")
def capabilities_menu_opens_predictably(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()
    expect(menu_page.capabilities_menu).to_be_visible()
    menu_page.close_capabilities_menu()
    expect(menu_page.capabilities_menu).not_to_be_visible()


@given("Capabilities menu is open")
def capabilities_menu_open(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()
    expect(menu_page.capabilities_menu).to_be_visible()


@when("User navigates via keyboard (Tab/Arrow)")
def keyboard_navigation(page: Page):
    page.keyboard.press("Tab")


@then("All capability links are keyboard operable")
def capability_links_keyboard_operable(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    links = menu_page.capability_links.all()
    for link in links:
        expect(link).to_be_attached()


@given("Capabilities menu is rendered")
def capabilities_menu_rendered(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Group labels are compared against approved taxonomy")
def compare_group_labels(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()


@then("Labels show AI, Engineering, and Platforms matching approved taxonomy")
def labels_match_taxonomy(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    labels = menu_page.get_group_labels()
    assert "AI" in labels, "AI label not found"
    assert "Engineering" in labels, "Engineering label not found"
    assert "Platforms" in labels, "Platforms label not found"


@when("Labels are checked for uniqueness")
def check_labels_uniqueness(page: Page):
    pass


@then("All labels are unique within the menu")
def labels_are_unique(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    labels = menu_page.get_group_labels()
    assert len(labels) == len(set(labels)), "Duplicate labels found in menu"


@when("User clicks any capability link")
def click_capability_link(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.click_capability_link("Digital Engineering")


@then("All URLs resolve to valid destination pages")
def urls_resolve_valid(page: Page):
    expect(page).to_have_urlContaining("/capabilities/")


@given("Page is at desktop viewport")
def desktop_viewport(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})


@when("Capabilities menu opens")
def capabilities_menu_open_desktop(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()


@then("Menu uses grouped mega-menu layout")
def grouped_mega_menu_layout(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    expect(menu_page.capabilities_menu).to_be_visible()
    labels = menu_page.get_group_labels()
    assert len(labels) >= 3, "Expected grouped layout with 3 groups"


@given("Page is at mobile viewport")
def mobile_viewport(page: Page):
    page.set_viewport_size({"width": 375, "height": 667})


@when("Capabilities menu opens")
def capabilities_menu_open_mobile(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()


@then("Menu uses accessible disclosure pattern")
def mobile_disclosure_pattern(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    expect(menu_page.capabilities_menu).to_be_visible()


@given("Capability menu is open at narrow desktop width")
def narrow_desktop_width(page: Page):
    page.set_viewport_size({"width": 900, "height": 600})


@when("Menu content exceeds container bounds")
def menu_content_exceeds(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    menu_page.open_capabilities_menu()


@then("Menu overflow is handled without breaking layout")
def overflow_handled(page: Page):
    menu_page = CapabilitiesMenuPage(page)
    expect(menu_page.capabilities_menu).to_be_visible()
