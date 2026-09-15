"""Steps for issue_0002: Main navigation menu items work correctly."""
from pytest_bdd import given, when, then

from pages.issue_0002_navigation_menu_page import NavigationMenuPage


@given("The homepage is loaded and main menu is visible")
def homepage_loaded_menu_visible(page, navigation_menu_page):
    navigation_menu_page.navigate_to_homepage()


@when("The user clicks on each main navigation menu item")
def click_each_menu_item(page, navigation_menu_page):
    navigation_menu_page.click_solutions_menu()
    navigation_menu_page.navigate_to_homepage()

    navigation_menu_page.click_capabilities_menu()
    navigation_menu_page.navigate_to_homepage()

    navigation_menu_page.click_industries_menu()
    navigation_menu_page.navigate_to_homepage()

    navigation_menu_page.click_insights_menu()
    navigation_menu_page.navigate_to_homepage()

    navigation_menu_page.click_company_menu()
    navigation_menu_page.navigate_to_homepage()

    navigation_menu_page.click_connect_menu()


@then("Each menu item navigates to the correct corresponding page")
def verify_navigation_results(page, navigation_menu_page):
    pass
