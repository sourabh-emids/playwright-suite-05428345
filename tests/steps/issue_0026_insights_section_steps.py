"""Step definitions for issue_0026 - Insights section six content cards rendering."""
from pytest_bdd import given, then, when

from pages.issue_0026_insights_section_page import Issue0026InsightsSectionPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0026InsightsSectionPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Insights section")
def view_insights_section(page: Issue0026InsightsSectionPage):
    """View the Insights section."""
    page.view_insights_section()


@then('the section heading should be "The intelligence behind the outcomes"')
def section_heading_correct(page: Issue0026InsightsSectionPage):
    """Verify section heading is correct."""
    page.section_heading_should_be_correct()


@then("six content cards should be visible")
def six_content_cards_visible(page: Issue0026InsightsSectionPage):
    """Verify six content cards are visible."""
    page.six_content_cards_should_be_visible()
