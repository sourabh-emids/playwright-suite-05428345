"""Step definitions for issue_0004 - Industries mega-menu content."""
from pytest_bdd import given, then, when

from pages.issue_0004_industries_page import Issue0004IndustriesMenuPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0004IndustriesMenuPage):
    """Navigate to the homepage."""
    page.click_industries_navigation()


@when("I click the Industries navigation item")
def click_industries_navigation(page: Issue0004IndustriesMenuPage):
    """Click the Industries navigation item."""
    page.click_industries_navigation()


@then("the Industries mega-menu should appear")
def mega_menu_appears(page: Issue0004IndustriesMenuPage):
    """Verify mega-menu appears."""
    page.mega_menu_should_appear()


@then("the menu should display Consumer industry option")
def menu_displays_consumer_industry(page: Issue0004IndustriesMenuPage):
    """Verify Consumer industry option is displayed."""
    page.menu_should_display_consumer_industry()


@then("the industry description should be visible")
def industry_description_visible(page: Issue0004IndustriesMenuPage):
    """Verify industry description is visible."""
    page.industry_description_should_be_visible()
