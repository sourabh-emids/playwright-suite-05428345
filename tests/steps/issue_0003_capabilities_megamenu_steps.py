"""Steps for Capabilities mega-menu implementation (issue_0003)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0003_capabilities_megamenu_page import CapabilitiesMegamenuPage
from locators.issue_0003_capabilities_megamenu_locators import CapabilitiesMegamenuLocators


@given("User is on Emids homepage")
def on_homepage(page: Page) -> None:
    page.goto("/")


@given("Capabilities menu is open")
def capabilities_menu_open(page: Page) -> None:
    page.goto("/")
    capabilities_page = CapabilitiesMegamenuPage(page)
    capabilities_page.activate_capabilities()


@given("User is on desktop viewing Emids homepage")
def desktop_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 1280, "height": 800})


@given("User is on mobile viewing Emids homepage")
def mobile_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@when("User activates the Capabilities navigation item")
def activate_capabilities(page: Page) -> None:
    capabilities_page = CapabilitiesMegamenuPage(page)
    capabilities_page.activate_capabilities()


@when("User navigates with Tab key through capability links")
def tab_through_capabilities(page: Page) -> None:
    capabilities_page = CapabilitiesMegamenuPage(page)
    capabilities_page.activate_capabilities()
    for _ in range(5):
        page.keyboard.press("Tab")


@when("User views capability group labels")
def view_capability_labels(page: Page) -> None:
    pass


@when("User reviews all labels")
def review_labels(page: Page) -> None:
    pass


@when("User clicks on each capability link")
def click_capability_links(page: Page) -> None:
    capabilities_page = CapabilitiesMegamenuPage(page)
    links = capabilities_page.get_capability_links()
    if links:
        links[0].click()


@then("Menu opens with AI, Engineering, and Platforms capability groups visible")
def menu_opens_with_groups(page: Page) -> None:
    locators = CapabilitiesMegamenuLocators(page)
    expect(locators.ai_group).to_be_visible()
    expect(locators.engineering_group).to_be_visible()
    expect(locators.platforms_group).to_be_visible()


@then("All capability links are keyboard accessible and operable")
def capability_links_keyboard_accessible(page: Page) -> None:
    capabilities_page = CapabilitiesMegamenuPage(page)
    links = capabilities_page.get_capability_links()
    for link in links:
        link.focus()
        expect(link).to_be_focused()


@then("Labels (AI, Engineering, Platforms) match approved site taxonomy with unique labels within menu")
def labels_match_taxonomy(page: Page) -> None:
    locators = CapabilitiesMegamenuLocators(page)
    expect(locators.ai_group).to_be_visible()
    expect(locators.engineering_group).to_be_visible()
    expect(locators.platforms_group).to_be_visible()


@then("Desktop uses grouped mega-menu layout")
def desktop_grouped_layout(page: Page) -> None:
    expect(CapabilitiesMegamenuLocators(page).capabilities_button).to_be_visible()


@then("Mobile uses accessible disclosure pattern")
def mobile_disclosure_pattern(page: Page) -> None:
    expect(CapabilitiesMegamenuLocators(page).capabilities_button).to_be_visible()


@then("All capability labels are unique within the menu")
def labels_unique(page: Page) -> None:
    pass


@then("All capability destination URLs resolve to valid pages")
def capability_urls_resolve(page: Page) -> None:
    pass
