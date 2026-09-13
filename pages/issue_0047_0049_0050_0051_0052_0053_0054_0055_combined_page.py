"""Page object for remaining issues combined"""

from playwright.sync_api import Page, expect

from locators.issue_0047_0049_0050_0051_0052_0053_0054_0055_combined_locators import CombinedLocators


class CombinedPage:
    """Page object for all remaining modules."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CombinedLocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def navigate_to_contact(self) -> None:
        """Navigate to contact page."""
        self.page.goto("https://www.emids.com/contact/")

    def verify_main_content(self) -> None:
        """Verify main content is visible."""
        expect(self.locators.main_content).to_be_visible()

    def verify_header(self) -> None:
        """Verify header is visible."""
        expect(self.locators.header).to_be_visible()

    def verify_footer(self) -> None:
        """Verify footer is visible."""
        expect(self.locators.footer).to_be_visible()

    def verify_contact_form(self) -> None:
        """Verify contact form is visible."""
        expect(self.locators.contact_form).to_be_visible()

    def resize_to_viewport(self, width: int, height: int) -> None:
        """Resize viewport."""
        self.page.set_viewport_size({"width": width, "height": height})

    def check_no_horizontal_scroll(self) -> bool:
        """Check for horizontal scroll."""
        scroll_width = self.page.evaluate("document.documentElement.scrollWidth")
        client_width = self.page.evaluate("document.documentElement.clientWidth")
        return scroll_width <= client_width

    def get_page_title(self) -> str:
        """Get page title."""
        return self.page.title()

    def get_meta_description(self) -> str:
        """Get meta description."""
        return self.page.locator("meta[name='description']").get_attribute("content") or ""
