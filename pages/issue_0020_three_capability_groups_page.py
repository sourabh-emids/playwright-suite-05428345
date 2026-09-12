"""Page object for issue_0020 - Three capability groups visibility and content."""
from playwright.sync_api import Page, expect

from locators.issue_0020_three_capability_groups_locators import Issue0020ThreeCapabilityGroupsLocators


class Issue0020ThreeCapabilityGroupsPage:
    """Page object for three capability groups."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0020ThreeCapabilityGroupsLocators()
        self.locators.page = page

    def view_capabilities_section(self) -> None:
        """Scroll to the Capabilities section."""
        self.locators.capabilities_section.scroll_into_view_if_needed()

    def section_heading_should_be_correct(self) -> None:
        """Verify section heading is correct."""
        expect(self.locators.capabilities_section).to_be_visible()

    def ai_capability_should_be_visible(self) -> None:
        """Verify AI capability group is visible."""
        expect(self.locators.ai_capability).to_be_visible()

    def engineering_capability_should_be_visible(self) -> None:
        """Verify Engineering capability group is visible."""
        expect(self.locators.engineering_capability).to_be_visible()

    def platforms_capability_should_be_visible(self) -> None:
        """Verify Platforms capability group is visible."""
        expect(self.locators.platforms_capability).to_be_visible()
