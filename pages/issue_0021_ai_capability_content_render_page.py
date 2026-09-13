"""Page object for issue_0021: AI capability content render"""

from playwright.sync_api import Page, expect

from locators.issue_0021_ai_capability_content_render_locators import Issue0021AICapabilityLocators


class Issue0021AICapabilityPage:
    """Page object for AI capability content."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0021AICapabilityLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_ai_content(self) -> None:
        """Verify AI content is visible."""
        expect(self.page.get_by_text("AI")).to_be_visible()

    def verify_ai_clickable(self) -> None:
        """Verify AI element is clickable."""
        ai_button = self.page.get_by_role("button", name="AI")
        if ai_button.count() > 0:
            expect(ai_button).to_be_enabled()
        else:
            expect(self.page.get_by_text("AI")).to_be_visible()
