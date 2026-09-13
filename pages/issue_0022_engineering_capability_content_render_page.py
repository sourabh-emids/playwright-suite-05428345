"""Page object for issue_0022: Engineering capability content render"""

from playwright.sync_api import Page, expect

from locators.issue_0022_engineering_capability_content_render_locators import Issue0022EngineeringCapabilityLocators


class Issue0022EngineeringCapabilityPage:
    """Page object for Engineering capability content."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0022EngineeringCapabilityLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_engineering_content(self) -> None:
        """Verify Engineering content is visible."""
        expect(self.locators.engineering_content).to_be_visible()
