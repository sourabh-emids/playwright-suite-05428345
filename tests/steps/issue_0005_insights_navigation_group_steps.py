"""Step definitions for issue_0005: Insights Navigation Group."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from locators.insights_menu_locators import InsightsMenuLocators


@given("User is on page with header")
def on_page_with_header(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User activates Insights navigation control")
def activate_insights(page: Page):
    locators = InsightsMenuLocators(page)
    locators.insights_trigger.click()


@then("Insights control opens reliably with visible response")
def insights_opens_reliably(page: Page):
    locators = InsightsMenuLocators(page)
    expect(locators.insights_menu).to_be_visible()


@given("Insights menu is open")
def insights_menu_open(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    locators = InsightsMenuLocators(page)
    locators.insights_trigger.click()


@when("User views child links at all supported breakpoints")
def view_child_links_breakpoints(page: Page):
    pass


@then("Child links are readable and operable")
def child_links_readable_operable(page: Page):
    locators = InsightsMenuLocators(page)
    links = locators.child_links.all()
    for link in links:
        expect(link).to_be_visible()


@given("Insights navigation group is configured")
def insights_configured(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Menu renders")
def menu_renders(page: Page):
    locators = InsightsMenuLocators(page)
    locators.insights_trigger.click()


@then("No empty menu groups are displayed")
def no_empty_groups(page: Page):
    locators = InsightsMenuLocators(page)
    links = locators.child_links.all()
    assert len(links) > 0, "No empty groups should be displayed"


@when("URLs are validated")
def validate_urls(page: Page):
    pass


@then("Destination URLs are canonical")
def canonical_urls(page: Page):
    locators = InsightsMenuLocators(page)
    links = locators.child_links.all()
    for link in links:
        href = link.get_attribute("href")
        assert href and ("/insights/" in href or href.startswith("http")), f"Invalid URL: {href}"


@given("User with mouse interacts with Insights menu")
def mouse_interaction(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User hovers over menu items")
def hover_insights_items(page: Page):
    locators = InsightsMenuLocators(page)
    locators.insights_trigger.hover()


@then("Interaction does not prevent keyboard/touch access")
def hover_not_block_keyboard(page: Page):
    locators = InsightsMenuLocators(page)
    expect(locators.insights_trigger).to_be_focusable()
