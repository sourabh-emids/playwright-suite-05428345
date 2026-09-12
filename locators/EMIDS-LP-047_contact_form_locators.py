"""Locators for Contact form - EMIDS-LP-047, EMIDS-LP-048, EMIDS-LP-049"""
from playwright.sync_api import Page, Locator


class ContactFormLocators:
    """Locators for Contact form elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def form(self) -> Locator:
        return self.page.get_by_role("form")

    @property
    def first_name_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="First Name")

    @property
    def last_name_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Last Name")

    @property
    def email_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Work Email Address")

    @property
    def company_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Company Name")

    @property
    def title_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Title")

    @property
    def phone_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Phone Number")

    @property
    def inquiry_type_field(self) -> Locator:
        return self.page.get_by_role("combobox", name="Inquiry Type")

    @property
    def comments_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Comments")

    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Submit")

    @property
    def success_message(self) -> Locator:
        return self.page.get_by_text("Thank you")

    @property
    def error_message(self) -> Locator:
        return self.page.get_by_text("error", exact=False)
