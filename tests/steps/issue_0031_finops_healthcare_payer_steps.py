"""Step definitions for issue_0031 - FinOps healthcare payer resource card display."""
from pytest_bdd import given, then, when

from pages.issue_0031_finops_healthcare_payer_page import Issue0031FinopsHealthcarePayerPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0031FinopsHealthcarePayerPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Insights section")
def view_insights_section(page: Issue0031FinopsHealthcarePayerPage):
    """View the Insights section."""
    page.view_insights_section()


@then("the FinOps resource card should be visible")
def card_visible(page: Issue0031FinopsHealthcarePayerPage):
    """Verify card is visible."""
    page.card_should_be_visible()


@then("the card should have a Read More action")
def card_has_read_more_action(page: Issue0031FinopsHealthcarePayerPage):
    """Verify card has a Read More action."""
    page.card_should_have_read_more_action()
