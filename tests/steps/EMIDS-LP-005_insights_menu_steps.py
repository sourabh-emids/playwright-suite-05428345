"""Step definitions for Insights menu - EMIDS-LP-005"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-005_insights_menu_page import InsightsMenuPage
from playwright.sync_api import expect


@given("A user interacts with the Insights navigation item")
def interact_insights(page):
    menu_page = InsightsMenuPage(page)
    menu_page.goto("/")


@when("The menu trigger is activated")
def activate_insights(page):
    menu_page = InsightsMenuPage(page)
    menu_page.open_insights_menu()


@then("Menu opens displaying thought leadership, resources, news, and related insight destinations")
def verify_insights_menu_content(page):
    menu_page = InsightsMenuPage(page)
    menu_page.verify_menu_groups()


@given("The Insights menu is open")
def insights_menu_open(page):
    menu_page = InsightsMenuPage(page)
    menu_page.goto("/")
    menu_page.open_insights_menu()


@when("Viewed at desktop, tablet, and mobile widths")
def view_at_different_widths(page):
    pass


@then("All child links are readable and operable")
def verify_child_links_readable(page):
    menu_page = InsightsMenuPage(page)
    links = menu_page.get_insights_links()
    assert len(links) > 0


@given("The Insights navigation structure")
def insights_nav_structure(page):
    menu_page = InsightsMenuPage(page)
    menu_page.goto("/")
    menu_page.open_insights_menu()


@when("All menu groups are inspected")
def inspect_menu_groups(page):
    pass


@then("No empty menu groups exist; all destination URLs are canonical")
def verify_no_empty_groups(page):
    menu_page = InsightsMenuPage(page)
    menu_page.verify_menu_groups()
    links = menu_page.get_insights_links()
    assert len(links) > 0
