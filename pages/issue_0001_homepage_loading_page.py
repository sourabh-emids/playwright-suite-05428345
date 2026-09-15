"""Page object for issue_0001: Homepage loads without errors."""
from playwright.sync_api import Page, expect

from locators.issue_0001_homepage_loading_locators import HomepageLoadingLocators


class HomepageLoadingPage:
    """Page object for the emids.com homepage."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HomepageLoadingLocators(page)

    def load_homepage(self) -> None:
        self.page.goto("/")

    def dismiss_cookie_consent(self) -> None:
        if self.locators.allow_all_button.is_visible():
            self.locators.allow_all_button.click()

    def verify_logo_is_visible(self) -> None:
        expect(self.locators.logo).to_be_visible()

    def verify_main_heading_is_visible(self) -> None:
        expect(self.locators.main_heading).to_be_visible()

    def verify_page_loads_without_errors(self) -> None:
        expect(self.page).to_have_title("Emids - Digital Engineering, Core Platforms, and AI Solutions")
        expect(self.locators.main_heading).to_be_visible()
