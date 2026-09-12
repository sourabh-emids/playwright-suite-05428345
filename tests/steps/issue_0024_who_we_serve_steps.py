"""Step definitions for issue_0024 - Five audience entries rendering and Explore actions."""
from pytest_bdd import given, parsers, then, when

from pages.issue_0024_who_we_serve_page import Issue0024WhoWeServePage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0024WhoWeServePage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Who We Serve section")
def view_who_we_serve_section(page: Issue0024WhoWeServePage):
    """View the Who We Serve section."""
    page.view_who_we_serve_section()


@then("five audience entries should be visible")
def five_audience_entries_visible(page: Issue0024WhoWeServePage):
    """Verify five audience entries are visible."""
    page.five_audience_entries_should_be_visible()


@then(parsers.parse("the audience should include {audience}"))
def audience_includes(page: Issue0024WhoWeServePage, audience: str):
    """Verify specific audience is included."""
    page.audience_should_include(audience)


@then("each audience should have an Explore action")
def each_audience_has_explore(page: Issue0024WhoWeServePage):
    """Verify each audience has an Explore action."""
    page.each_audience_should_have_explore_action()
