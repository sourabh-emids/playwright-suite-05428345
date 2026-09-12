"""Step definitions for issue_0001 - Header visibility and global navigation."""
from pytest_bdd import given, parsers, then

from pages.issue_0001_header_page import Issue0001HeaderPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0001HeaderPage):
    """Navigate to the homepage."""
    page.goto()


@then("the header banner should be visible")
def header_banner_visible(page: Issue0001HeaderPage):
    """Verify header banner is visible."""
    page.header_banner_should_be_visible()


@then("the main navigation should be present")
def main_navigation_present(page: Issue0001HeaderPage):
    """Verify main navigation is present."""
    page.main_navigation_should_be_present()


@then("the logo link should navigate to homepage")
def logo_link_navigates_to_homepage(page: Issue0001HeaderPage):
    """Verify logo link navigates to homepage."""
    page.logo_link_should_navigate_to_homepage()


@then(parsers.parse('the navigation should include "{item}"'))
def navigation_includes_item(page: Issue0001HeaderPage, item: str):
    """Verify navigation includes specific item."""
    page.navigation_should_include_item(item)


@then("the Connect CTA should be visible in the header")
def connect_cta_visible_in_header(page: Issue0001HeaderPage):
    """Verify Connect CTA is visible in header."""
    page.connect_cta_should_be_visible_in_header()
