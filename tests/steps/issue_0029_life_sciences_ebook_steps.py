"""Step definitions for issue_0029 - Life Sciences transformation eBook card display."""
from pytest_bdd import given, then, when

from pages.issue_0029_life_sciences_ebook_page import Issue0029LifeSciencesEbookPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0029LifeSciencesEbookPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Insights section")
def view_insights_section(page: Issue0029LifeSciencesEbookPage):
    """View the Insights section."""
    page.view_insights_section()


@then("the Life Sciences eBook card should be visible")
def card_visible(page: Issue0029LifeSciencesEbookPage):
    """Verify card is visible."""
    page.card_should_be_visible()
