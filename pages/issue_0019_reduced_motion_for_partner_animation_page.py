"""Page object for issue_0019: Reduced motion for partner animation"""

from playwright.sync_api import Page, expect

from locators.issue_0019_reduced_motion_for_partner_animation_locators import Issue0019ReducedMotionLocators


class Issue0019ReducedMotionPage:
    """Page object for reduced motion functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0019ReducedMotionLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_partnerships_content_visible(self) -> None:
        """Verify partnerships content is visible."""
        expect(self.locators.partnerships_section).to_be_visible()

    def check_reduced_motion_enabled(self) -> bool:
        """Check if reduced motion is enabled."""
        return self.page.evaluate("""
            window.matchMedia('(prefers-reduced-motion: reduce)').matches
        """)
