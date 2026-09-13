"""Page object for issue_0034-0035: Final CTA combined"""

from playwright.sync_api import Page, expect

from locators.issue_0034_0035_final_cta_combined_locators import FinalCTALocators


class FinalCTAPage:
    """Page object for Final CTA section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = FinalCTALocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_final_cta_present(self) -> None:
        """Verify final CTA section is present."""
        expect(self.locators.final_cta_section).to_be_visible()

    def verify_timing_labels(self) -> None:
        """Verify timing labels are visible."""
        expect(self.locators.timing_labels).to_be_visible()

    def resize_to_mobile(self) -> None:
        """Resize to mobile viewport."""
        self.page.set_viewport_size({"width": 375, "height": 812})
