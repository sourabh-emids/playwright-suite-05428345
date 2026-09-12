"""Step definitions for issue_0021 - AI capability content rendering and links."""
from pytest_bdd import given, then, when

from pages.issue_0021_ai_capability_page import Issue0021AICapabilityPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0021AICapabilityPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the Capabilities section")
def view_capabilities_section(page: Issue0021AICapabilityPage):
    """View the Capabilities section."""
    page.view_capabilities_section()


@then("the AI capability section should be visible")
def ai_capability_visible(page: Issue0021AICapabilityPage):
    """Verify AI capability section is visible."""
    page.ai_capability_section_should_be_visible()


@then("AI capability links should be present")
def ai_capability_links_present(page: Issue0021AICapabilityPage):
    """Verify AI capability links are present."""
    page.ai_capability_links_should_be_present()
