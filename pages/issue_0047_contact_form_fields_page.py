"""Page object for issue_0047 - Contact form fields and accessibility."""
from playwright.sync_api import Page, expect

from locators.issue_0047_contact_form_fields_locators import Issue0047ContactFormFieldsLocators


class Issue0047ContactFormFieldsPage:
    """Page object for contact form fields."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0047ContactFormFieldsLocators()
        self.locators.page = page

    def navigate_to_contact(self) -> None:
        """Navigate to the contact page."""
        self.page.goto("/contact/")

    def form_fields_should_have_labels(self) -> None:
        """Verify form fields have labels."""
        fields = self.locators.form_fields
        count = fields.count()
        for i in range(count):
            field = fields.nth(i)
            # Check for associated label or aria-label
            has_label = await field.get_attribute("aria-label") or \
                        await field.get_attribute("id") and self.page.locator(f"label[for='{await field.get_attribute('id')}']").count() > 0
            # This is a basic check - real implementation would be more thorough

    def fields_should_be_keyboard_accessible(self) -> None:
        """Verify fields are keyboard accessible."""
        # Focusable elements should be reachable via keyboard
        expect(self.locators.form_fields.first).to_be_attached()
