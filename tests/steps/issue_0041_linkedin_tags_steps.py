"""Step definitions for issue_0041 - LinkedIn marketing tags conditional loading."""
from pytest_bdd import given, then

from pages.issue_0041_linkedin_tags_page import Issue0041LinkedInTagsPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0041LinkedInTagsPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@then("LinkedIn tags should not be active")
def linkedin_not_active(page: Issue0041LinkedInTagsPage):
    """Verify LinkedIn tags are not active."""
    page.linkedin_tags_should_not_be_active()
