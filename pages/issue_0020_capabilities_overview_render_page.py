"""Page object for issue_0020: Capabilities overview render"""

from playwright.sync_api import Page, expect

from locators.issue_0020_capabilities_overview_render_locators import Issue0020CapabilitiesLocators


class Issue0020CapabilitiesPage:
    """Page object for Capabilities overview."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0020CapabilitiesLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_all_groups_visible(self) -> None:
        """Verify all three capability groups are visible."""
        expect(self.locators.ai_group).to_be_visible()
        expect(self.locators.engineering_group).to_be_visible()
        expect(self.locators.platforms_group).to_be_visible()

    def resize_to_viewport(self, width: int, height: int) -> None:
        """Resize viewport."""
        self.page.set_viewport_size({"width": width, "height": height})

    def verify_layout_intact(self) -> None:
        """Verify layout remains intact."""
        expect(self.locators.capabilities_section).to_be_visible()
