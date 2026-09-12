"""Page object for issue_0008 - Responsive navigation behavior."""
from playwright.sync_api import Page, expect

from locators.issue_0008_responsive_nav_locators import Issue0008ResponsiveNavLocators


class Issue0008ResponsiveNavPage:
    """Page object for responsive navigation."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0008ResponsiveNavLocators()
        self.locators.page = page

    def set_viewport_to_desktop(self) -> None:
        """Set viewport to desktop size."""
        self.page.set_viewport_size({"width": 1920, "height": 1080})

    def set_viewport_to_mobile(self) -> None:
        """Set viewport to mobile size."""
        self.page.set_viewport_size({"width": 375, "height": 667})

    def full_navigation_should_be_visible(self) -> None:
        """Verify full navigation menu is visible on desktop."""
        expect(self.locators.main_navigation).to_be_visible()

    def connect_cta_should_be_visible(self) -> None:
        """Verify Connect CTA is visible."""
        expect(self.locators.connect_cta).to_be_visible()

    def mobile_menu_toggle_should_be_visible(self) -> None:
        """Verify mobile menu toggle is visible."""
        # On mobile, the navigation should transform to a toggle
        expect(self.locators.mobile_menu_toggle.first).to_be_visible()

    def tapping_menu_toggle_should_reveal_navigation(self) -> None:
        """Verify tapping menu toggle reveals navigation."""
        toggle = self.locators.mobile_menu_toggle.first
        if await toggle.is_visible():
            toggle.click()
            # After clicking, navigation items should be visible
            expect(self.page.locator("nav a, nav button").first).to_be_visible()
