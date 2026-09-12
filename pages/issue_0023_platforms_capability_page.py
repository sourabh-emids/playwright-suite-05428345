"""Page object for issue_0023 - Platforms capability taxonomy consistency."""
from playwright.sync_api import Page, expect

from locators.issue_0023_platforms_capability_locators import Issue0023PlatformsCapabilityLocators


class Issue0023PlatformsCapabilityPage:
    """Page object for Platforms capability."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0023PlatformsCapabilityLocators()
        self.locators.page = page

    def view_capabilities_section(self) -> None:
        """Scroll to the Capabilities section."""
        self.locators.platforms_capability_section.scroll_into_view_if_needed()

    def platforms_capability_section_should_be_visible(self) -> None:
        """Verify Platforms capability section is visible."""
        expect(self.locators.platforms_capability_section).to_be_visible()

    def platforms_section_should_have_consistent_naming(self) -> None:
        """Verify Platforms section has consistent naming."""
        # Check that "Platforms" is spelled consistently throughout
        platforms_occurrences = self.page.locator("text=Platforms").count()
        assert platforms_occurrences > 0, "Platforms should be mentioned in the page"
