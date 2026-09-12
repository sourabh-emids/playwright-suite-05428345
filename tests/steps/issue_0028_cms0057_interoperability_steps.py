"""Step definitions for issue_0028 - CMS-0057 interoperability resource card display."""
from pytest_bdd import given, then, when

from pages.issue_0028_cms0057_interoperability_page import Issue0028CMS0057InteroperabilityPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0028CMS0057InteroperabilityPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Insights section")
def view_insights_section(page: Issue0028CMS0057InteroperabilityPage):
    """View the Insights section."""
    page.view_insights_section()


@then("the CMS-0057 eBook card should be visible")
def card_visible(page: Issue0028CMS0057InteroperabilityPage):
    """Verify card is visible."""
    page.card_should_be_visible()


@then("the card should have the eBook type indicator")
def card_has_ebook_indicator(page: Issue0028CMS0057InteroperabilityPage):
    """Verify card has eBook type indicator."""
    page.card_should_have_ebook_indicator()
