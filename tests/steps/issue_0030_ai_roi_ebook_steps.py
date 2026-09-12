"""Step definitions for issue_0030 - AI ROI eBook card display."""
from pytest_bdd import given, then, when

from pages.issue_0030_ai_roi_ebook_page import Issue0030AiroiEbookPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0030AiroiEbookPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Insights section")
def view_insights_section(page: Issue0030AiroiEbookPage):
    """View the Insights section."""
    page.view_insights_section()


@then("the AI ROI eBook card should be visible")
def card_visible(page: Issue0030AiroiEbookPage):
    """Verify card is visible."""
    page.card_should_be_visible()
