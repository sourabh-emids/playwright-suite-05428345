"""Step definitions for issue_0045 - Footer legal navigation links."""
from pytest_bdd import given, then, when

from pages.issue_0045_footer_legal_links_page import Issue0045FooterLegalLinksPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0045FooterLegalLinksPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the footer")
def view_footer(page: Issue0045FooterLegalLinksPage):
    """View the footer."""
    page.view_footer()


@then("the Code of Conduct link should be present")
def code_of_conduct_present(page: Issue0045FooterLegalLinksPage):
    """Verify Code of Conduct link is present."""
    page.code_of_conduct_link_present()


@then("the Privacy Policy link should be present")
def privacy_policy_present(page: Issue0045FooterLegalLinksPage):
    """Verify Privacy Policy link is present."""
    page.privacy_policy_link_present()


@then("the Transparency in Coverage link should be present")
def transparency_present(page: Issue0045FooterLegalLinksPage):
    """Verify Transparency in Coverage link is present."""
    page.transparency_in_coverage_link_present()


@then("the Cookie Policy link should be present")
def cookie_policy_present(page: Issue0045FooterLegalLinksPage):
    """Verify Cookie Policy link is present."""
    page.cookie_policy_link_present()


@then("the Accessibility Statement link should be present")
def accessibility_statement_present(page: Issue0045FooterLegalLinksPage):
    """Verify Accessibility Statement link is present."""
    page.accessibility_statement_link_present()
