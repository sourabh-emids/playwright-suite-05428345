"""Step definitions for issue_0022 - Engineering capability content rendering."""
from pytest_bdd import given, then, when

from pages.issue_0022_engineering_capability_page import Issue0022EngineeringCapabilityPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0022EngineeringCapabilityPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Capabilities section")
def view_capabilities_section(page: Issue0022EngineeringCapabilityPage):
    """View the Capabilities section."""
    page.view_capabilities_section()


@then("the Engineering capability section should be visible")
def engineering_capability_visible(page: Issue0022EngineeringCapabilityPage):
    """Verify Engineering capability section is visible."""
    page.engineering_capability_section_should_be_visible()
