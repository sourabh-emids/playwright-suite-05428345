"""Page object for issue_0004 - Industries mega-menu content."""
from playwright.sync_api import Page, expect

from locators.issue_0004_industries_menu_locators import Issue0004IndustriesMenuLocators


class Issue0004IndustriesMenuPage:
    """Page object for Industries mega-menu content."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0004IndustriesMenuLocators()
        self.locators.page = page

    def click_industries_navigation(self) -> None:
        """Click the Industries navigation item."""
        self.locators.industries_nav_button.click()

    def mega_menu_should_appear(self) -> None:
        """Verify mega-menu appears."""
        expect(self.locators.consumer_link).to_be_visible()

    def menu_should_display_consumer_industry(self) -> None:
        """Verify Consumer industry option is displayed."""
        expect(self.locators.consumer_link).to_be_visible()

    def industry_description_should_be_visible(self) -> None:
        """Verify industry description is visible."""
        expect(self.page.locator("text=Consumer").first).to_be_visible()
