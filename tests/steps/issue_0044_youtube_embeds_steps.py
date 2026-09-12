"""Step definitions for issue_0044 - YouTube embeds conditional loading."""
from pytest_bdd import given, then, when

from pages.issue_0044_youtube_embeds_page import Issue0044YouTubeEmbedsPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0044YouTubeEmbedsPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view a page with YouTube content")
def view_youtube_content(page: Issue0044YouTubeEmbedsPage):
    """View a page with YouTube content."""
    pass


@then("YouTube should not load before consent")
def youtube_not_loaded(page: Issue0044YouTubeEmbedsPage):
    """Verify YouTube does not load before consent."""
    page.youtube_should_not_load_before_consent()
