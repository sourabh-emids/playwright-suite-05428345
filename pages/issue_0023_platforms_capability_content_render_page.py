"""Page object for issue_0023: Platforms capability content render"""

from playwright.sync_api import Page, expect

from locators.issue_0023_platforms_capability_content_render_locators import Issue0023PlatformsCapabilityLocators


class Issue0023PlatformsCapabilityPage:
    """Page object for Platforms capability content."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0023PlatformsCapabilityLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_platforms_content(self) -> None:
        """Verify Platforms content is visible."""
        expect(self.locators.platforms_content).to_be_visible()
