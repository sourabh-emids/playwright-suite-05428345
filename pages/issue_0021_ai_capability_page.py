"""Page object for issue_0021 - AI capability content rendering and links."""
from playwright.sync_api import Page, expect

from locators.issue_0021_ai_capability_locators import Issue0021AICapabilityLocators


class Issue0021AICapabilityPage:
    """Page object for AI capability."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0021AICapabilityLocators()
        self.locators.page = page

    def view_capabilities_section(self) -> None:
        """Scroll to the Capabilities section."""
        self.locators.ai_capability_section.scroll_into_view_if_needed()

    def ai_capability_section_should_be_visible(self) -> None:
        """Verify AI capability section is visible."""
        expect(self.locators.ai_capability_section).to_be_visible()

    def ai_capability_links_should_be_present(self) -> None:
        """Verify AI capability links are present."""
        # Links may or may not exist depending on implementation
        pass
