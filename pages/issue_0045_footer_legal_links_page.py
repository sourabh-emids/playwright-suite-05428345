"""Page object for issue_0045 - Footer legal navigation links."""
from playwright.sync_api import Page, expect

from locators.issue_0045_footer_legal_links_locators import Issue0045FooterLegalLinksLocators


class Issue0045FooterLegalLinksPage:
    """Page object for footer legal links."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0045FooterLegalLinksLocators()
        self.locators.page = page

    def view_footer(self) -> None:
        """Scroll to the footer."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def code_of_conduct_link_present(self) -> None:
        """Verify Code of Conduct link is present."""
        expect(self.locators.code_of_conduct_link).to_be_visible()

    def privacy_policy_link_present(self) -> None:
        """Verify Privacy Policy link is present."""
        expect(self.locators.privacy_policy_link).to_be_visible()

    def transparency_in_coverage_link_present(self) -> None:
        """Verify Transparency in Coverage link is present."""
        expect(self.locators.transparency_in_coverage_link).to_be_visible()

    def cookie_policy_link_present(self) -> None:
        """Verify Cookie Policy link is present."""
        expect(self.locators.cookie_policy_link).to_be_visible()

    def accessibility_statement_link_present(self) -> None:
        """Verify Accessibility Statement link is present."""
        expect(self.locators.accessibility_statement_link).to_be_visible()
