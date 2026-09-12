"""Page object for issue_0046 - Footer corporate contact information rendering."""
from playwright.sync_api import Page, expect

from locators.issue_0046_footer_corporate_contact_locators import Issue0046FooterCorporateContactLocators


class Issue0046FooterCorporateContactPage:
    """Page object for footer corporate contact."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0046FooterCorporateContactLocators()
        self.locators.page = page

    def view_footer(self) -> None:
        """Scroll to the footer."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def footer_logo_should_be_visible(self) -> None:
        """Verify footer logo is visible."""
        expect(self.locators.footer_logo).to_be_visible()

    def footer_connect_link_should_be_present(self) -> None:
        """Verify footer Connect link is present."""
        expect(self.locators.footer_connect_link).to_be_visible()
