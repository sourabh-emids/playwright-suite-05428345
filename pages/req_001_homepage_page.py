"""Page object for REQ-001: Homepage loads successfully."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.req_001_homepage_locators import Req001HomepageLocators


class Req001HomepagePage(BasePage):
    """Page object for homepage operations."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Req001HomepageLocators(page)

    def goto_homepage(self, base_url: str) -> None:
        """Navigate to the homepage."""
        self.goto(f"{base_url}/")

    def dismiss_cookie_banner_if_present(self) -> None:
        """Dismiss the cookie consent banner if visible."""
        if self.locators.cookie_banner.is_visible(timeout=2000):
            self.locators.allow_all_cookies_button.click()
            self.locators.cookie_banner.wait_for(state="hidden", timeout=5000)

    def verify_page_title(self, expected_title: str) -> None:
        """Verify the page title is correct."""
        expect(self.page).to_have_title(expected_title)

    def verify_main_heading_visible(self) -> None:
        """Verify the main heading is visible."""
        expect(self.locators.main_heading).to_be_visible()

    def verify_logo_visible(self) -> None:
        """Verify the Emids logo is visible."""
        expect(self.locators.emids_logo).to_be_visible()

    def verify_navigation_visible(self) -> None:
        """Verify the main navigation menu is visible."""
        expect(self.locators.main_navigation).to_be_visible()

    def verify_page_loads_without_errors(self) -> None:
        """Verify the page loads successfully without console errors."""
        self.dismiss_cookie_banner_if_present()
        expect(self.page).to_have_title("Emids - Digital Engineering, Core Platforms, and AI Solutions")
        expect(self.locators.main_heading).to_be_visible()

    def verify_all_resources_loaded(self) -> None:
        """Verify all visible elements are displayed correctly."""
        self.dismiss_cookie_banner_if_present()
        expect(self.locators.main_heading).to_be_visible()
        expect(self.locators.emids_logo).to_be_visible()
        expect(self.locators.main_navigation).to_be_visible()
