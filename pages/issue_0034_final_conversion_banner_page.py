"""Page object for issue_0034 - Final conversion banner rendering and CTA."""
from playwright.sync_api import Page, expect

from locators.issue_0034_final_conversion_banner_locators import Issue0034FinalConversionBannerLocators


class Issue0034FinalConversionBannerPage:
    """Page object for Final conversion banner."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0034FinalConversionBannerLocators()
        self.locators.page = page

    def view_page(self) -> None:
        """View the page."""
        pass

    def final_cta_banner_should_be_visible(self) -> None:
        """Verify final CTA banner is visible."""
        expect(self.locators.final_cta_banner).to_be_visible()

    def timing_message_should_be_visible(self) -> None:
        """Verify timing message is visible."""
        expect(self.page.locator("text=1 Day · 2 Weeks · 3 Months")).to_be_visible()

    def connect_cta_should_be_present(self) -> None:
        """Verify Connect CTA is present."""
        expect(self.locators.connect_cta).to_be_visible()
