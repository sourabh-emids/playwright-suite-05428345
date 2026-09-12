"""Page object for issue_0001 - Header visibility and global navigation."""
from playwright.sync_api import Page, expect

from locators.issue_0001_header_locators import Issue0001HeaderLocators


class Issue0001HeaderPage:
    """Page object for header visibility and global navigation."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0001HeaderLocators()
        # Bind locators to page
        self.locators.page = page

    def goto(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def header_banner_should_be_visible(self) -> None:
        """Verify header banner is visible."""
        expect(self.locators.header_banner).to_be_visible()

    def main_navigation_should_be_present(self) -> None:
        """Verify main navigation is present."""
        expect(self.locators.main_navigation).to_be_attached()

    def logo_link_should_navigate_to_homepage(self) -> None:
        """Verify logo link exists and has correct href."""
        expect(self.locators.logo_link).to_have_attribute("href", "https://www.emids.com/")

    def navigation_should_include_item(self, item: str) -> None:
        """Verify navigation includes specific item."""
        link = self.locators.main_navigation.get_by_role("link", name=item)
        expect(link).to_be_visible()

    def connect_cta_should_be_visible_in_header(self) -> None:
        """Verify Connect CTA is visible in header."""
        expect(self.locators.header_connect_cta).to_be_visible()
