"""Step definitions for emids_lp_003 - Capabilities mega-menu."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@when("The user activates the Capabilities navigation control")
def activate_capabilities_control(page: Page) -> None:
    from pages.emids_lp_003_capabilities_page import CapabilitiesMenuPage
    cap_page = CapabilitiesMenuPage(page)
    cap_page.click_capabilities_button()


@then("The menu opens and displays AI, Engineering, and Platforms capability groups with child destinations")
def verify_capabilities_menu_opens(page: Page) -> None:
    from pages.emids_lp_003_capabilities_page import CapabilitiesMenuPage
    cap_page = CapabilitiesMenuPage(page)
    expect(cap_page.capabilities_menu).to_be_visible()
    expect(cap_page.ai_group).to_be_visible()
    expect(cap_page.engineering_group).to_be_visible()
    expect(cap_page.platforms_group).to_be_visible()


@then("All capability links including AI, Engineering, Platforms, and child links are operable via keyboard")
def verify_capability_links_keyboard_operable(page: Page) -> None:
    from pages.emids_lp_003_capabilities_page import CapabilitiesMenuPage
    cap_page = CapabilitiesMenuPage(page)
    links = cap_page.capability_links
    for link in links:
        link.focus()
        expect(link).to_be_focused()


@then("Labels for AI, Engineering, and Platforms match content-managed terminology exactly")
def verify_labels_match_taxonomy(page: Page) -> None:
    from pages.emids_lp_003_capabilities_page import CapabilitiesMenuPage
    cap_page = CapabilitiesMenuPage(page)
    expect(cap_page.ai_label).to_have_text("AI")
    expect(cap_page.engineering_label).to_have_text("Engineering")
    expect(cap_page.platforms_label).to_have_text("Platforms")


@then("All capability labels are unique within the menu")
def verify_unique_labels(page: Page) -> None:
    from pages.emids_lp_003_capabilities_page import CapabilitiesMenuPage
    cap_page = CapabilitiesMenuPage(page)
    labels = cap_page.all_capability_labels
    label_texts = [label.text_content() for label in labels]
    assert len(label_texts) == len(set(label_texts)), "Duplicate labels found"


@then("All capability destination URLs resolve successfully without 404 errors")
def verify_capability_urls_resolve(page: Page) -> None:
    from pages.emids_lp_003_capabilities_page import CapabilitiesMenuPage
    cap_page = CapabilitiesMenuPage(page)
    links = cap_page.capability_links
    for link in links:
        href = link.get_attribute("href")
        if href and not href.startswith("#"):
            response = page.request.get(href)
            assert response.status < 400, f"404 for {href}"


@then("Menu content scrolls or repositions without clipping critical content")
def verify_menu_overflow_handled(page: Page) -> None:
    from pages.emids_lp_003_capabilities_page import CapabilitiesMenuPage
    cap_page = CapabilitiesMenuPage(page)
    page.set_viewport_size({"width": 1024, "height": 600})
    cap_page.click_capabilities_button()
    expect(cap_page.capabilities_menu).to_be_visible()
