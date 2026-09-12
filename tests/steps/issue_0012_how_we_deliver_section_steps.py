"""Step definitions for issue_0012 - How We Deliver section content rendering."""
from pytest_bdd import given, then, when

from pages.issue_0012_how_we_deliver_page import Issue0012HowWeDeliverPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0012HowWeDeliverPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the How We Deliver section")
def view_how_we_deliver_section(page: Issue0012HowWeDeliverPage):
    """View the How We Deliver section."""
    page.view_how_we_deliver_section()


@then("the section heading should be visible")
def section_heading_visible(page: Issue0012HowWeDeliverPage):
    """Verify section heading is visible."""
    page.section_heading_should_be_visible()


@then("the FDCE description should be present")
def fdce_description_present(page: Issue0012HowWeDeliverPage):
    """Verify FDCE description is present."""
    page.fdce_description_should_be_present()


@then("the feature list should be rendered")
def feature_list_rendered(page: Issue0012HowWeDeliverPage):
    """Verify feature list is rendered."""
    page.feature_list_should_be_rendered()
