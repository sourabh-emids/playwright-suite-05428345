"""Page object for issue_0001: Render global header with navigation"""

from playwright.sync_api import Page, expect

from locators.issue_0001_header_renders_on_initial_page_load_locators import Issue0001HeaderLocators


class Issue0001HeaderPage:
    """Page object for global header functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0001HeaderLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to the emids.com homepage."""
        self.page.goto("https://www.emids.com")

    def click_emids_logo(self) -> None:
        """Click the Emids logo in the header."""
        self.locators.emids_logo.click()

    def verify_header_visible(self) -> None:
        """Verify the global header is visible."""
        expect(self.locators.navigation_list).to_be_visible()

    def verify_emids_logo_visible(self) -> None:
        """Verify the Emids logo is visible."""
        expect(self.locators.emids_logo).to_be_visible()

    def verify_all_nav_items_visible(self) -> None:
        """Verify all navigation items are visible."""
        for nav_item in self.locators.get_all_nav_items():
            expect(self.page.get_by_role("button", name=nav_item)).to_be_visible()

    def verify_connect_cta_visible(self) -> None:
        """Verify the Connect CTA is visible."""
        expect(self.locators.connect_cta_header).to_be_visible()

    def click_connect_cta(self) -> None:
        """Click the Connect CTA in the header."""
        self.locators.connect_cta_header.click()

    def verify_navigated_to_url(self, url: str) -> None:
        """Verify navigation to a specific URL."""
        expect(self.page).to_have_url(url)

    def verify_focus_on_element(self, locator) -> None:
        """Verify focus is on a specific element."""
        expect(locator).to_be_focused()

    def hover_over_nav_item(self, nav_item_name: str) -> None:
        """Hover over a navigation item."""
        button = self.page.get_by_role("button", name=nav_item_name)
        button.hover()

    def count_connect_cta_elements(self) -> int:
        """Count the number of Connect CTA elements in the header."""
        return self.locators.get_connect_cta_count().count()

    def tab_through_navigation(self, count: int) -> None:
        """Press Tab key multiple times to navigate through items."""
        for _ in range(count):
            self.page.keyboard.press("Tab")

    def get_current_url(self) -> str:
        """Get the current page URL."""
        return self.page.url
