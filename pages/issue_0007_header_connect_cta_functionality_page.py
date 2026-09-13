"""Page object for issue_0007: Header Connect CTA functionality"""

from playwright.sync_api import Page, expect

from locators.issue_0007_header_connect_cta_functionality_locators import Issue0007ConnectCTALocators


class Issue0007ConnectCTAPage:
    """Page object for Header Connect CTA functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0007ConnectCTALocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def click_connect_cta(self) -> None:
        """Click the Connect CTA."""
        self.locators.connect_cta.click()

    def verify_cta_visually_distinct(self) -> None:
        """Verify the CTA is visible."""
        expect(self.locators.connect_cta).to_be_visible()

    def verify_accessible_name(self) -> None:
        """Verify the CTA has an accessible name."""
        name = self.locators.connect_cta.get_attribute("aria-label") or self.locators.connect_cta.inner_text()
        expect(name).not_to_be_blank()

    def verify_routes_to_contact(self) -> None:
        """Verify navigation to contact page."""
        expect(self.page).to_have_url("https://www.emids.com/contact/")

    def verify_https_protocol(self) -> None:
        """Verify the URL uses HTTPS."""
        href = self.locators.connect_cta.get_attribute("href")
        expect(href).to_match(r"^https://")
