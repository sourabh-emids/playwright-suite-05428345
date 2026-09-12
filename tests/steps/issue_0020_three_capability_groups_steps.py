"""Step definitions for issue_0020 - Three capability groups visibility and content."""
from pytest_bdd import given, then, when

from pages.issue_0020_three_capability_groups_page import Issue0020ThreeCapabilityGroupsPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0020ThreeCapabilityGroupsPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Capabilities section")
def view_capabilities_section(page: Issue0020ThreeCapabilityGroupsPage):
    """View the Capabilities section."""
    page.view_capabilities_section()


@then('the section heading should be "Capabilities that deliver on ambitious goals"')
def section_heading_correct(page: Issue0020ThreeCapabilityGroupsPage):
    """Verify section heading is correct."""
    page.section_heading_should_be_correct()


@then("the AI capability group should be visible")
def ai_capability_visible(page: Issue0020ThreeCapabilityGroupsPage):
    """Verify AI capability group is visible."""
    page.ai_capability_should_be_visible()


@then("the Engineering capability group should be visible")
def engineering_capability_visible(page: Issue0020ThreeCapabilityGroupsPage):
    """Verify Engineering capability group is visible."""
    page.engineering_capability_should_be_visible()


@then("the Platforms capability group should be visible")
def platforms_capability_visible(page: Issue0020ThreeCapabilityGroupsPage):
    """Verify Platforms capability group is visible."""
    page.platforms_capability_should_be_visible()
