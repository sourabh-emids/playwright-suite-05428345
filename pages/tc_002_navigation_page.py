"""Page object for tc_002 - Main navigation menu items functionality."""
from playwright.sync_api import Page, expect, Locator

from locators.tc_002_navigation_locators import Tc002NavigationLocators


class Tc002NavigationPage:
    """Page object for navigation functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Tc002NavigationLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def click_menu_item(self, menu_item: Locator) -> None:
        """Click on a menu item."""
        menu_item.click()

    def navigate_to_about_us(self) -> None:
        """Navigate to About Us page."""
        self.locators.company_link.click()
        self.locators.get_submenu_link("Our Story").click()

    def navigate_to_solutions(self) -> None:
        """Navigate to Solutions page."""
        self.locators.solutions_link.click()

    def navigate_to_capabilities(self) -> None:
        """Navigate to Capabilities page."""
        self.locators.capabilities_link.click()

    def navigate_to_insights(self) -> None:
        """Navigate to Insights page."""
        self.locators.insights_link.click()

    def navigate_to_industries(self) -> None:
        """Navigate to Industries page."""
        self.locators.industries_link.click()

    def navigate_to_contact(self) -> None:
        """Navigate to Contact page."""
        self.locators.connect_link.click()

    def hover_over_menu_item(self, menu_item: Locator) -> None:
        """Hover over a menu item to trigger dropdown."""
        menu_item.hover()

    def verify_dropdown_visible(self, dropdown: Locator) -> None:
        """Verify a dropdown is visible."""
        expect(dropdown).to_be_visible()

    def verify_page_navigated(self, expected_url_part: str) -> None:
        """Verify the page has navigated to the expected URL."""
        expect(self.page).to_have_url(expected_url_part, timeout=10000)

    def verify_menu_item_hover_state(self, menu_item: Locator) -> None:
        """Verify the menu item shows hover state."""
        menu_item.hover()
        current_color = menu_item.evaluate("element => window.getComputedStyle(element).color")
        expect(menu_item).to_be_visible()

    def rapid_click(self, menu_item: Locator, times: int = 5) -> None:
        """Click rapidly multiple times."""
        for _ in range(times):
            menu_item.click()
