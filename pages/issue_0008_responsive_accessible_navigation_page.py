"""Page object for issue_0008: Responsive accessible navigation"""

from playwright.sync_api import Page, expect

from locators.issue_0008_responsive_accessible_navigation_locators import Issue0008ResponsiveNavLocators


class Issue0008ResponsiveNavPage:
    """Page object for responsive accessible navigation."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0008ResponsiveNavLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def resize_to_viewport(self, width: int, height: int) -> None:
        """Resize to specified viewport."""
        self.page.set_viewport_size({"width": width, "height": height})

    def tap_nav_item(self) -> None:
        """Tap on a navigation item."""
        self.locators.solutions_nav_button.click()

    def press_escape_key(self) -> None:
        """Press Escape key."""
        self.page.keyboard.press("Escape")

    def open_menu(self) -> None:
        """Open a navigation menu."""
        self.locators.solutions_nav_button.click()

    def check_for_horizontal_scroll(self) -> bool:
        """Check if horizontal scrollbar is present."""
        scroll_width = self.page.evaluate("document.documentElement.scrollWidth")
        client_width = self.page.evaluate("document.documentElement.clientWidth")
        return scroll_width > client_width

    def check_reduced_motion(self) -> bool:
        """Check if prefers-reduced-motion is enabled."""
        return self.page.evaluate("""
            window.matchMedia('(prefers-reduced-motion: reduce)').matches
        """)

    def verify_focus_visible(self) -> None:
        """Verify focus is visible."""
        focused = self.page.evaluate("document.activeElement")
        expect(self.page.locator(focused)).to_be_visible()
