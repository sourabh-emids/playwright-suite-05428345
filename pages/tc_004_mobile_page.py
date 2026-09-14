"""Page object for tc_004 - Mobile responsive view functionality."""
from playwright.sync_api import Page, expect, Locator

from locators.tc_004_mobile_locators import Tc004MobileLocators


class Tc004MobilePage:
    """Page object for mobile responsive functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Tc004MobileLocators(page)

    def set_mobile_viewport(self, width: int = 375, height: int = 812) -> None:
        """Set the viewport to mobile size."""
        self.page.set_viewport_size({"width": width, "height": height})

    def set_tablet_viewport(self, width: int = 768, height: int = 1024) -> None:
        """Set the viewport to tablet size."""
        self.page.set_viewport_size({"width": width, "height": height})

    def navigate_to_homepage(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def navigate_to_contact(self) -> None:
        """Navigate to the contact page."""
        self.page.goto("/contact/")

    def dismiss_cookie_banner(self) -> None:
        """Dismiss the cookie consent banner."""
        allow_button = self.page.get_by_role("button", name="Allow all")
        if allow_button.is_visible():
            allow_button.click()

    def click_hamburger_menu(self) -> None:
        """Click the hamburger menu icon."""
        self.locators.hamburger_menu.click()

    def verify_mobile_menu_opens(self) -> None:
        """Verify mobile menu opens."""
        expect(self.locators.mobile_navigation).to_be_visible(timeout=5000)

    def verify_text_is_readable(self) -> None:
        """Verify text is readable on mobile."""
        expect(self.locators.text_content).to_be_visible()

    def verify_images_scale(self) -> None:
        """Verify images scale appropriately."""
        expect(self.locators.hero_image).to_be_visible()

    def verify_buttons_are_tappable(self) -> None:
        """Verify buttons are properly sized for touch."""
        submit_button = self.locators.submit_button
        box = submit_button.bounding_box()
        expect(submit_button).to_be_visible()
        assert box is not None and box["width"] >= 44 and box["height"] >= 44, \
            "Button should be at least 44x44 pixels for touch"

    def verify_no_horizontal_scroll(self) -> None:
        """Verify no horizontal scrolling is required."""
        scroll_width = self.page.evaluate("document.body.scrollWidth")
        inner_width = self.page.evaluate("window.innerWidth")
        assert scroll_width <= inner_width + 5, "No horizontal scroll should be needed"

    def scroll_to_element(self, element: Locator) -> None:
        """Scroll to a specific element."""
        element.scroll_into_view_if_needed()

    def tap_element(self, element: Locator) -> None:
        """Tap an element (for mobile)."""
        element.tap()
