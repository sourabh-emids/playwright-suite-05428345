"""Step definitions for issue_0046 - Footer corporate contact information rendering."""
from pytest_bdd import given, then, when

from pages.issue_0046_footer_corporate_contact_page import Issue0046FooterCorporateContactPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0046FooterCorporateContactPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the footer")
def view_footer(page: Issue0046FooterCorporateContactPage):
    """View the footer."""
    page.view_footer()


@then("the footer logo should be visible")
def footer_logo_visible(page: Issue0046FooterCorporateContactPage):
    """Verify footer logo is visible."""
    page.footer_logo_should_be_visible()


@then("the footer Connect link should be present")
def footer_connect_present(page: Issue0046FooterCorporateContactPage):
    """Verify footer Connect link is present."""
    page.footer_connect_link_should_be_present()
