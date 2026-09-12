"""Step definitions for issue_0027 - Medicare Advantage eBook card display."""
from pytest_bdd import given, then, when

from pages.issue_0027_medicare_advantage_ebook_page import Issue0027MedicareAdvantageEbookPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0027MedicareAdvantageEbookPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Insights section")
def view_insights_section(page: Issue0027MedicareAdvantageEbookPage):
    """View the Insights section."""
    page.view_insights_section()


@then("the Medicare Advantage eBook card should be visible")
def card_visible(page: Issue0027MedicareAdvantageEbookPage):
    """Verify card is visible."""
    page.card_should_be_visible()


@then("the card should have the eBook type indicator")
def card_has_ebook_indicator(page: Issue0027MedicareAdvantageEbookPage):
    """Verify card has eBook type indicator."""
    page.card_should_have_ebook_indicator()


@then("the card should have a download action")
def card_has_download_action(page: Issue0027MedicareAdvantageEbookPage):
    """Verify card has a download action."""
    page.card_should_have_download_action()
