"""Step definitions for issue_0043 - Wistia embeds conditional loading."""
from pytest_bdd import given, then, when

from pages.issue_0043_wistia_embeds_page import Issue0043WistiaEmbedsPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0043WistiaEmbedsPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view a page with video content")
def view_video_content(page: Issue0043WistiaEmbedsPage):
    """View a page with video content."""
    pass


@then("Wistia should not load before consent")
def wistia_not_loaded(page: Issue0043WistiaEmbedsPage):
    """Verify Wistia does not load before consent."""
    page.wistia_should_not_load_before_consent()
