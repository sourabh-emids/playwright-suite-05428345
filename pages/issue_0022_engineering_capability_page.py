"""Page object for issue_0022 - Engineering capability content rendering."""
from playwright.sync_api import Page, expect

from locators.issue_0022_engineering_capability_locators import Issue0022EngineeringCapabilityLocators


class Issue0022EngineeringCapabilityPage:
    """Page object for Engineering capability."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0022EngineeringCapabilityLocators()
        self.locators.page = page

    def view_capabilities_section(self) -> None:
        """Scroll to the Capabilities section."""
        self.locators.engineering_capability_section.scroll_into_view_if_needed()

    def engineering_capability_section_should_be_visible(self) -> None:
        """Verify Engineering capability section is visible."""
        expect(self.locators.engineering_capability_section).to_be_visible()
