"""Page object for issue_0035 - Delivery timing message rendering."""
from playwright.sync_api import Page, expect

from locators.issue_0035_delivery_timing_message_locators import Issue0035DeliveryTimingMessageLocators


class Issue0035DeliveryTimingMessagePage:
    """Page object for delivery timing message."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0035DeliveryTimingMessageLocators()
        self.locators.page = page

    def view_final_cta_section(self) -> None:
        """Scroll to the final CTA section."""
        self.locators.timing_message.scroll_into_view_if_needed()

    def timing_message_should_be_visible(self) -> None:
        """Verify timing message is visible."""
        expect(self.locators.timing_message).to_be_visible()

    def timing_description_should_be_present(self) -> None:
        """Verify timing description is present."""
        expect(self.locators.timing_description).to_be_visible()
