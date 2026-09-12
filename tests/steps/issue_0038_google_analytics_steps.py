"""Step definitions for issue_0038 - Google Analytics post-consent measurement."""
from pytest_bdd import given, then, when

from pages.issue_0038_google_analytics_page import Issue0038GoogleAnalyticsPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0038GoogleAnalyticsPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I give analytics consent")
def give_analytics_consent(page: Issue0038GoogleAnalyticsPage):
    """Give analytics consent."""
    page.give_analytics_consent()


@then("GA should be initialized")
def ga_initialized(page: Issue0038GoogleAnalyticsPage):
    """Verify GA is initialized."""
    page.ga_should_be_initialized()
