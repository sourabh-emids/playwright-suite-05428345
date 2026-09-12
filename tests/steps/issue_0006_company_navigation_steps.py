"""Step definitions for issue_0006 - Company navigation group."""
from pytest_bdd import given, parsers, then, when

from pages.issue_0006_company_page import Issue0006CompanyMenuPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0006CompanyMenuPage):
    """Navigate to the homepage."""
    page.click_company_navigation()


@when("I click the Company navigation item")
def click_company_navigation(page: Issue0006CompanyMenuPage):
    """Click the Company navigation item."""
    page.click_company_navigation()


@then("the Company mega-menu should appear")
def mega_menu_appears(page: Issue0006CompanyMenuPage):
    """Verify mega-menu appears."""
    page.mega_menu_should_appear()


@then(parsers.parse('the menu should display "{section}" section'))
def menu_displays_section(page: Issue0006CompanyMenuPage, section: str):
    """Verify a section is displayed in the menu."""
    page.menu_should_display_section(section)
