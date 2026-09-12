"""Step definitions for issue_0018 - Partner logo rail rendering and accessibility."""
from pytest_bdd import given, then, when

from pages.issue_0018_partner_logo_rail_page import Issue0018PartnerLogoRailPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0018PartnerLogoRailPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Partnerships section")
def view_partnerships_section(page: Issue0018PartnerLogoRailPage):
    """View the Partnerships section."""
    page.view_partnerships_section()


@then("partner logos should be visible")
def partner_logos_visible(page: Issue0018PartnerLogoRailPage):
    """Verify partner logos are visible."""
    page.partner_logos_should_be_visible()


@then("logos should have alt text for accessibility")
def logos_have_alt_text(page: Issue0018PartnerLogoRailPage):
    """Verify logos have alt text."""
    page.logos_should_have_alt_text()
