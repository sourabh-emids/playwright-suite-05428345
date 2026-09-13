"""Page object for issue_0006: Company navigation group"""

from playwright.sync_api import Page, expect

from locators.issue_0006_company_navigation_group_locators import Issue0006CompanyMenuLocators


class Issue0006CompanyMenuPage:
    """Page object for Company navigation group."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0006CompanyMenuLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def open_company_menu(self) -> None:
        """Open the Company menu."""
        self.locators.company_nav_button.click()

    def verify_company_menu_content(self) -> None:
        """Verify Company menu displays expected content."""
        expect(self.locators.about_us_heading).to_be_visible()
        expect(self.locators.connect_with_us_heading).to_be_visible()

    def get_company_links(self) -> list:
        """Get all company links."""
        return self.locators.get_all_company_links().all()

    def validate_links_return_200(self) -> bool:
        """Validate that all links return HTTP 200."""
        links = self.locators.get_all_company_links().all()
        for link in links:
            href = link.get_attribute("href")
            if href and not href.startswith("#"):
                response = self.page.request.get(href)
                if response.status != 200:
                    return False
        return True
