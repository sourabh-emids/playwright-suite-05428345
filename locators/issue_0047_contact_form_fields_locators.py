"""Locators for issue_0047 - Contact form fields and accessibility."""
from playwright.sync_api import Locator


class Issue0047ContactFormFieldsLocators:
    """Locators for contact form fields."""

    @property
    def contact_form(self) -> Locator:
        """Return the contact form."""
        return self.page.locator("form")

    @property
    def form_fields(self) -> Locator:
        """Return the form fields."""
        return self.contact_form.locator("input, textarea, select")
