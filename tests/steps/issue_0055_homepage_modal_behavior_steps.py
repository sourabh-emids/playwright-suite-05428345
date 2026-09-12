"""Step definitions for issue_0055 - Homepage modal behavior default state."""
from pytest_bdd import given, then, when

from pages.issue_0055_homepage_modal_behavior_page import Issue0055HomepageModalBehaviorPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0055HomepageModalBehaviorPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("the page loads")
def page_loads(page: Issue0055HomepageModalBehaviorPage):
    """Wait for page to load."""
    page.page_loads()


@then("no modal should be visible by default")
def no_modal_visible(page: Issue0055HomepageModalBehaviorPage):
    """Verify no modal is visible by default."""
    page.no_modal_should_be_visible_by_default()


@then("the main content should be accessible")
def main_content_accessible(page: Issue0055HomepageModalBehaviorPage):
    """Verify main content is accessible."""
    page.main_content_should_be_accessible()
