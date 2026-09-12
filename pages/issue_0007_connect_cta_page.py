"""Page object for issue_0007 - Header Connect CTA visibility and routing."""
from playwright.sync_api import Page, expect

from locators.issue_0007_connect_cta_locators import Issue0007ConnectCTALocators


class Issue0007ConnectCTAPage:
    """Page object for Header Connect CTA."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0007ConnectCTALocators()
        self.locators.page = page

    def connect_cta_should_be_visible(self) -> None:
        """Verify Connect CTA is visible."""
        expect(self.locators.header_connect_cta).to_be_visible()

    def connect_cta_should_link_to_contact_page(self) -> None:
        """Verify Connect CTA links to the contact page."""
        expect(self.locators.header_connect_cta).to_have_attribute(
            "href", "https://www.emids.com/contact/"
        )

    def click_connect_cta(self) -> None:
        """Click the Connect CTA."""
        self.locators.header_connect_cta.click()

    def should_be_on_contact_page(self) -> None:
        """Verify user is on the contact page."""
        expect(self.page).to_have_url("**/contact/**")
