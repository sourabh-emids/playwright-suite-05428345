"""Page object for REQ-002: Main navigation menu items navigate to correct pages."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.req_002_navigation_locators import Req002NavigationLocators


class Req002NavigationPage(BasePage):
    """Page object for navigation menu operations."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Req002NavigationLocators(page)

    def click_solutions_nav(self) -> None:
        """Click on Solutions navigation button."""
        self.locators.solutions_nav_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_capabilities_nav(self) -> None:
        """Click on Capabilities navigation button."""
        self.locators.capabilities_nav_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_industries_nav(self) -> None:
        """Click on Industries navigation button."""
        self.locators.industries_nav_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_insights_nav(self) -> None:
        """Click on Insights navigation button."""
        self.locators.insights_nav_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_company_nav(self) -> None:
        """Click on Company navigation button."""
        self.locators.company_nav_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_connect_nav(self) -> None:
        """Click on Connect navigation link."""
        self.locators.connect_nav_link.click()
        self.page.wait_for_load_state("networkidle")

    def verify_url_contains(self, text: str) -> None:
        """Verify current URL contains expected text."""
        expect(self.page).to_have_url(f"*{text}*")

    def verify_solutions_page_loaded(self) -> None:
        """Verify Solutions page loaded correctly."""
        self.verify_url_contains("solutions")

    def verify_capabilities_page_loaded(self) -> None:
        """Verify Capabilities page loaded correctly."""
        self.verify_url_contains("capabilities")

    def verify_industries_page_loaded(self) -> None:
        """Verify Industries page loaded correctly."""
        self.verify_url_contains("segments")

    def verify_insights_page_loaded(self) -> None:
        """Verify Insights page loaded correctly."""
        self.verify_url_contains("insights")

    def verify_about_us_page_loaded(self) -> None:
        """Verify About Us page loaded correctly."""
        self.verify_url_contains("about-us")

    def verify_contact_page_loaded(self) -> None:
        """Verify Contact page loaded correctly."""
        self.verify_url_contains("contact")

    def verify_navigation_menu_visible(self) -> None:
        """Verify navigation menu is visible."""
        expect(self.locators.main_navigation).to_be_visible()
