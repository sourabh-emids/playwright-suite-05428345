"""Step definitions for issue_0032 - Payer data readiness blog card display."""
from pytest_bdd import given, then, when

from pages.issue_0032_payer_data_readiness_blog_page import Issue0032PayerDataReadinessBlogPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0032PayerDataReadinessBlogPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Insights section")
def view_insights_section(page: Issue0032PayerDataReadinessBlogPage):
    """View the Insights section."""
    page.view_insights_section()


@then("the Payer data readiness blog card should be visible")
def card_visible(page: Issue0032PayerDataReadinessBlogPage):
    """Verify card is visible."""
    page.card_should_be_visible()
