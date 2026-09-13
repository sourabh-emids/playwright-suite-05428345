"""Step definitions for issue_0005: Insights navigation group"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0005_insights_navigation_group_page import Issue0005InsightsMenuPage


@given("A user focuses on the Insights navigation item")
def user_focuses_insights(page: Page):
    page_object = Issue0005InsightsMenuPage(page)
    page_object.navigate_to_homepage()
    page_object.open_insights_menu()


@given("The Insights menu is open")
def insights_menu_is_open(page: Page):
    page_object = Issue0005InsightsMenuPage(page)
    page_object.open_insights_menu()


@given("The Insights navigation group is rendered")
def insights_nav_group_rendered(page: Page):
    page_object = Issue0005InsightsMenuPage(page)
    page_object.open_insights_menu()


@when("The user activates the trigger")
def user_activates_trigger(page: Page):
    page_object = Issue0005InsightsMenuPage(page)
    page_object.open_insights_menu()


@when("The user tests at desktop, tablet, and mobile widths")
def user_tests_at_breakpoints(page: Page):
    page_object = Issue0005InsightsMenuPage(page)
    # Test at desktop
    page_object.resize_to_viewport(1280, 720)
    page_object.open_insights_menu()
    # Test at tablet
    page_object.resize_to_viewport(768, 1024)
    page_object.open_insights_menu()
    # Test at mobile
    page_object.resize_to_viewport(375, 812)
    page_object.open_insights_menu()


@when("Automated testing checks menu content")
def automated_checks_menu_content(page: Page):
    """Menu content check happens in assertions."""
    pass


@then("The Insights menu opens displaying thought leadership, resources, news, and related destinations")
def insights_menu_displays_content(page: Page):
    page_object = Issue0005InsightsMenuPage(page)
    page_object.verify_insights_menu_content()


@then("Child links remain readable and operable across all supported breakpoints")
def child_links_operable_at_breakpoints(page: Page):
    page_object = Issue0005InsightsMenuPage(page)
    expect(page_object.locators.get_all_insights_links().first).to_be_visible()


@then("All menu groups contain at least one navigation item")
def no_empty_menu_groups(page: Page):
    page_object = Issue0005InsightsMenuPage(page)
    assert not page_object.check_empty_groups(), "Found empty menu groups"
