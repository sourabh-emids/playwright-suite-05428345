"""Locators for Contact form reached by Connect CTAs (issue_0047)."""
from playwright.sync_api import Locator, Page


class ContactFormLocators:
    """Locators for Contact Form elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def first_name_field(self) -> Locator:
        return self.page.get_by_label(re.compile("First Name", re.IGNORECASE))

    @property
    def last_name_field(self) -> Locator:
        return self.page.get_by_label(re.compile("Last Name", re.IGNORECASE))

    @property
    def email_field(self) -> Locator:
        return self.page.get_by_label(re.compile("Email", re.IGNORECASE))

    @property
    def company_field(self) -> Locator:
        return self.page.get_by_label(re.compile("Company", re.IGNORECASE))

    @property
    def title_field(self) -> Locator:
        return self.page.get_by_label(re.compile("Title", re.IGNORECASE))

    @property
    def phone_field(self) -> Locator:
        return self.page.get_by_label(re.compile("Phone", re.IGNORECASE))

    @property
    def inquiry_select(self) -> Locator:
        return self.page.get_by_label(re.compile("Inquiry", re.IGNORECASE))

    @property
    def comments_field(self) -> Locator:
        return self.page.get_by_label(re.compile("Comments", re.IGNORECASE))

    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Submit")
