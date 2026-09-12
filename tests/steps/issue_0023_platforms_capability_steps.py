"""Step definitions for issue_0023 - Platforms capability taxonomy consistency."""
from pytest_bdd import given, then, when

from pages.issue_0023_platforms_capability_page import Issue0023PlatformsCapabilityPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0023PlatformsCapabilityPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Capabilities section")
def view_capabilities_section(page: Issue0023PlatformsCapabilityPage):
    """View the Capabilities section."""
    page.view_capabilities_section()


@then("the Platforms capability section should be visible")
def platforms_capability_visible(page: Issue0023PlatformsCapabilityPage):
    """Verify Platforms capability section is visible."""
    page.platforms_capability_section_should_be_visible()


@then("the Platforms section should have consistent naming")
def platforms_consistent_naming(page: Issue0023PlatformsCapabilityPage):
    """Verify Platforms section has consistent naming."""
    page.platforms_section_should_have_consistent_naming()
