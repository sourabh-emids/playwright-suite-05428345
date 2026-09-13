"""Page object for issue_0037-0044: Analytics and Media combined"""

from playwright.sync_api import Page, expect

from locators.issue_0037_0042_analytics_media_combined_locators import AnalyticsMediaLocators


class AnalyticsMediaPage:
    """Page object for Analytics and Media Integration."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = AnalyticsMediaLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_core_content(self) -> None:
        """Verify core page content is intact."""
        expect(self.locators.main_content).to_be_visible()

    def verify_gtm_script_present(self) -> bool:
        """Check if GTM script is present."""
        return self.page.evaluate("""
            typeof window.google_tag_manager !== 'undefined'
        """)

    def verify_analytics_present(self) -> bool:
        """Check if analytics is present."""
        return self.page.evaluate("""
            typeof window.ga !== 'undefined' || typeof window.gtag !== 'undefined'
        """)

    def check_no_wistia_script(self) -> bool:
        """Check no Wistia script is loaded."""
        return self.page.evaluate("""
            !document.querySelector('script[src*="wistia"]')
        """)

    def check_no_youtube_api(self) -> bool:
        """Check no YouTube API is loaded."""
        return self.page.evaluate("""
            !document.querySelector('script[src*="youtube.com"]')
        """)
