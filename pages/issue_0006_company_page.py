"""Page object for issue_0006 - Company navigation group keyboard and touch access."""
from playwright.sync_api import Page, expect

from locators.issue_0006_company_menu_locators import Issue0006CompanyMenuLocators


class Issue0006CompanyMenuPage:
    """Page object for Company navigation group."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0006CompanyMenuLocators()
        self.locators.page = page

    def click_company_navigation(self) -> None:
        """Click the Company navigation item."""
        self.locators.company_nav_button.click()

    def mega_menu_should_appear(self) -> None:
        """Verify mega-menu appears."""
        expect(self.locators.about_us_header).to_be_visible()

    def menu_should_display_section(self, section: str) -> None:
        """Verify a section is displayed in the menu."""
        if section == "About Us":
            expect(self.locators.about_us_header).to_be_visible()
        elif section == "Connect with Us":
            expect(self.locators.connect_with_us_header).to_be_visible()
