"""Page object for REQ-004: Website displays correctly on mobile viewport."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.req_004_mobile_locators import Req004MobileLocators


class Req004MobilePage(BasePage):
    """Page object for mobile viewport operations."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Req004MobileLocators(page)

    def set_mobile_viewport(self, width: int = 375, height: int = 667) -> None:
        """Set browser viewport to mobile dimensions."""
        self.page.set_viewport_size({"width": width, "height": height})

    def dismiss_cookie_banner_if_present(self) -> None:
        """Dismiss the cookie consent banner if visible."""
        if self.locators.cookie_banner.is_visible(timeout=2000):
            self.locators.allow_all_cookies_button.click()
            self.locators.cookie_banner.wait_for(state="hidden", timeout=5000)

    def verify_mobile_menu_toggle_visible(self) -> None:
        """Verify mobile menu toggle button is visible."""
        expect(self.locators.mobile_menu_toggle).to_be_visible()

    def verify_logo_visible(self) -> None:
        """Verify Emids logo is visible."""
        expect(self.locators.emids_logo).to_be_visible()

    def verify_main_heading_visible(self) -> None:
        """Verify main heading is visible."""
        expect(self.locators.main_heading).to_be_visible()

    def verify_page_title(self, expected_title: str) -> None:
        """Verify page title is correct."""
        expect(self.page).to_have_title(expected_title)

    def verify_no_horizontal_scroll(self) -> None:
        """Verify page renders without horizontal scrolling."""
        scroll_width = self.page.evaluate("document.documentElement.scrollWidth")
        viewport_width = self.page.evaluate("window.innerWidth")
        assert scroll_width <= viewport_width, "Page requires horizontal scrolling"

    def open_mobile_menu(self) -> None:
        """Open the mobile navigation menu."""
        self.locators.mobile_menu_toggle.click()
        self.page.wait_for_load_state("networkidle")

    def verify_contact_page_heading_visible(self) -> None:
        """Verify contact page heading is visible."""
        expect(self.locators.contact_heading).to_be_visible()

    def verify_connect_nav_visible(self) -> None:
        """Verify Connect navigation is visible."""
        expect(self.locators.connect_nav_link).to_be_visible()
