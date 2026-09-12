"""Step definitions for issue_0042 - ZoomInfo WebSights conditional integration."""
from pytest_bdd import given, then

from pages.issue_0042_zoominfo_websights_page import Issue0042ZoomInfoWebSightsPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0042ZoomInfoWebSightsPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@then("ZoomInfo WebSights should not be active")
def zoominfo_not_active(page: Issue0042ZoomInfoWebSightsPage):
    """Verify ZoomInfo WebSights is not active."""
    page.zoominfo_should_not_be_active()
