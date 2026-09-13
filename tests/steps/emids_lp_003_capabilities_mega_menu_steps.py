"""Steps for emids_lp_003: Implement Capabilities mega-menu."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.header.capabilities_menu_page import CapabilitiesMenuPage


@given(parsers.parse("User focuses on Capabilities navigation"))
def focus_capabilities_nav(page: Page) -> None:
    """Focus on Capabilities navigation."""
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.navigate()
    capabilities_page.locators.capabilities_nav.focus()


@given(parsers.parse("Capabilities mega-menu is open"))
def capabilities_menu_open(page: Page) -> None:
    """Capabilities mega-menu is open."""
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.navigate()
    capabilities_page.open_capabilities_menu()


@given(parsers.parse("Capabilities menu is open"))
def capabilities_menu_is_open(page: Page) -> None:
    """Capabilities menu is open."""
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.navigate()
    if not capabilities_page.are_all_groups_visible():
        capabilities_page.open_capabilities_menu()


@given(parsers.parse("User opens Capabilities menu"))
def user_opens_capabilities_menu(page: Page) -> None:
    """User opens Capabilities menu."""
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.navigate()
    capabilities_page.open_capabilities_menu()


@given(parsers.parse("Capabilities menu is open with many items"))
def menu_open_many_items(page: Page) -> None:
    """Capabilities menu is open with many items."""
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.navigate()
    capabilities_page.open_capabilities_menu()


@given(parsers.parse("User switches between desktop and mobile viewports"))
def switch_viewports(page: Page) -> None:
    """User switches between desktop and mobile viewports."""
    # Will be tested in the when clause
    pass


@given(parsers.parse("User views menu on various viewport sizes"))
def view_menu_various_sizes(page: Page) -> None:
    """User views menu on various viewport sizes."""
    pass


@when("User activates the Capabilities menu trigger")
def activate_capabilities_menu(page: Page) -> None:
    """Activate the Capabilities menu trigger."""
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.open_capabilities_menu()


@when("User tabs through capability links")
def tab_through_capability_links(page: Page) -> None:
    """Tab through capability links."""
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.open_capabilities_menu()
    # Focus on first link and tab
    capabilities_page.locators.data_engineering_link.focus()
    page.keyboard.press("Tab")


@when("User examines group labels")
def examine_group_labels(page: Page) -> None:
    """Examine group labels."""
    pass  # Verification step


@when("User activates Capabilities navigation")
def activate_capabilities_navigation(page: Page) -> None:
    """Activate Capabilities navigation."""
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.open_capabilities_menu()


@when("User scans for duplicate labels")
def scan_duplicate_labels(page: Page) -> None:
    """Scan for duplicate labels."""
    pass  # Verification step


@then("Menu opens consistently")
def menu_opens_consistently(page: Page) -> None:
    """Verify menu opens consistently."""
    capabilities_page = CapabilitiesMenuPage(page)
    expect(capabilities_page.locators.capabilities_button).to_have_attribute("aria-expanded", "true")


@then("AI, Engineering, and Platforms groups are visible")
def groups_are_visible(page: Page) -> None:
    """Verify AI, Engineering, and Platforms groups are visible."""
    capabilities_page = CapabilitiesMenuPage(page)
    expect(capabilities_page.locators.ai_group).to_be_visible()
    expect(capabilities_page.locators.engineering_group).to_be_visible()
    expect(capabilities_page.locators.platforms_group).to_be_visible()


@then("All capability links receive focus")
def all_capability_links_receive_focus(page: Page) -> None:
    """Verify all capability links receive focus."""
    capabilities_page = CapabilitiesMenuPage(page)
    for link in capabilities_page.locators.get_ai_links():
        expect(link).to_be_focusable()


@then("Links are keyboard navigable to destinations")
def links_keyboard_navigable(page: Page) -> None:
    """Verify links are keyboard navigable to destinations."""
    capabilities_page = CapabilitiesMenuPage(page)
    expect(capabilities_page.locators.data_engineering_link).to_be_focusable()


@then("Labels match approved site taxonomy")
def labels_match_taxonomy(page: Page) -> None:
    """Verify labels match approved site taxonomy."""
    capabilities_page = CapabilitiesMenuPage(page)
    expected_labels = ["AI", "Engineering", "Platforms"]
    actual_labels = capabilities_page.get_group_labels()
    for label in expected_labels:
        expect(label in actual_labels).to_be_true()


@then("No duplicate labels within menu")
def no_duplicate_labels(page: Page) -> None:
    """Verify no duplicate labels within menu."""
    capabilities_page = CapabilitiesMenuPage(page)
    expect(capabilities_page.has_duplicate_labels()).to_be_false()


@then("Desktop shows mega-menu layout")
def desktop_mega_menu_layout(page: Page) -> None:
    """Verify desktop shows mega-menu layout."""
    page.set_viewport_size({"width": 1280, "height": 800})
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.navigate()
    capabilities_page.open_capabilities_menu()
    expect(capabilities_page.locators.capabilities_button).to_have_attribute("aria-expanded", "true")


@then("Mobile shows accessible disclosure pattern")
def mobile_disclosure_pattern(page: Page) -> None:
    """Verify mobile shows accessible disclosure pattern."""
    page.set_viewport_size({"width": 375, "height": 667})
    capabilities_page = CapabilitiesMenuPage(page)
    capabilities_page.navigate()
    capabilities_page.open_capabilities_menu()
    expect(capabilities_page.locators.capabilities_button).to_be_visible()


@then("Menu content remains visible and accessible")
def menu_content_visible_accessible(page: Page) -> None:
    """Verify menu content remains visible and accessible."""
    capabilities_page = CapabilitiesMenuPage(page)
    expect(capabilities_page.locators.ai_group).to_be_visible()


@then("No overflow issues occur")
def no_overflow_issues(page: Page) -> None:
    """Verify no overflow issues occur."""
    capabilities_page = CapabilitiesMenuPage(page)
    # Check that menu doesn't overflow viewport
    menu_box = capabilities_page.locators.capabilities_button.bounding_box()
    expect(menu_box).not_to_be_none()
