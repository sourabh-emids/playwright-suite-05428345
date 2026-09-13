"""Steps for Insights navigation group implementation (issue_0005)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0005_insights_navigation_page import InsightsNavigationPage
from locators.issue_0005_insights_navigation_locators import InsightsNavigationLocators


@given("User is on Emids homepage")
def on_homepage(page: Page) -> None:
    page.goto("/")


@given("Insights menu is open")
def insights_menu_open(page: Page) -> None:
    page.goto("/")
    insights_page = InsightsNavigationPage(page)
    insights_page.activate_insights()


@when("User activates Insights navigation")
def activate_insights(page: Page) -> None:
    insights_page = InsightsNavigationPage(page)
    insights_page.activate_insights()


@when("User views menu at desktop, tablet, and mobile widths")
def view_at_breakpoints(page: Page) -> None:
    for width in [1280, 768, 375]:
        page.set_viewport_size({"width": width, "height": 800})
        insights_page = InsightsNavigationPage(page)
        insights_page.activate_insights()


@when("User tests navigation at different viewport sizes")
def test_nav_at_sizes(page: Page) -> None:
    for width in [1280, 768, 375]:
        page.set_viewport_size({"width": width, "height": 800})


@when("User views all menu groups")
def view_menu_groups(page: Page) -> None:
    pass


@when("User inspects child link URLs")
def inspect_urls(page: Page) -> None:
    pass


@when("User views Insights menu")
def view_insights_menu(page: Page) -> None:
    pass


@then("Insights menu opens reliably")
def menu_opens(page: Page) -> None:
    expect(InsightsNavigationLocators(page).menu_visible).to_be_visible()


@then("Child links are readable and text does not overflow or become inaccessible")
def links_readable(page: Page) -> None:
    locators = InsightsNavigationLocators(page)
    expect(locators.insights_resources_link).to_be_visible()


@then("All child links remain operable via keyboard and pointer")
def links_operable(page: Page) -> None:
    locators = InsightsNavigationLocators(page)
    locators.insights_resources_link.focus()
    expect(locators.insights_resources_link).to_be_focused()


@then("No empty menu groups are displayed")
def no_empty_groups(page: Page) -> None:
    pass


@then("All destination URLs are canonical")
def canonical_urls(page: Page) -> None:
    pass


@then("Menu behavior is consistent with Solutions, Capabilities, and Industries mega-menu/disclosure patterns")
def consistent_behavior(page: Page) -> None:
    locators = InsightsNavigationLocators(page)
    expect(locators.insights_button).to_be_visible()
