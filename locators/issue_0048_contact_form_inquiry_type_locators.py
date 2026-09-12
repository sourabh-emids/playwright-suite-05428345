"""Locators for issue_0048 - Contact form Inquiry Type values."""
from playwright.sync_api import Locator


class Issue0048ContactFormInquiryTypeLocators:
    """Locators for contact form inquiry type."""

    @property
    def inquiry_type_field(self) -> Locator:
        """Return the Inquiry Type field."""
        return self.page.locator("select").first
