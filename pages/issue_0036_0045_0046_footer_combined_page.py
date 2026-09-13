"""Page object for issue_0036, 0045-0046: Footer combined"""

from playwright.sync_api import Page, expect

from locators.issue_0036_0045_0046_footer_combined_locators import FooterLocators


class FooterPage:
    """Page object for Footer section."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = FooterLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def verify_footer_visible(self) -> None:
        """Verify footer is visible."""
        expect(self.locators.footer).to_be_visible()

    def resize_to_mobile(self) -> None:
        """Resize to mobile viewport."""
        self.page.set_viewport_size({"width": 375, "height": 812})

    def click_cookie_preferences(self) -> None:
        """Click Cookie Preferences button."""
        cookie_btn = self.locators.cookie_preferences
        if cookie_btn.count() > 0:
            cookie_btn.click()
