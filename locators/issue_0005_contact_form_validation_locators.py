"""Locators for issue_0005: Contact form validates required fields."""
from playwright.sync_api import Page, Locator


class ContactFormValidationLocators:
    """Locators for the contact form page."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def first_name_field(self) -> Locator:
        return self.page.locator("input[id*='FirstName'], input[name*='FirstName'], input[aria-label*='First Name']")

    @property
    def last_name_field(self) -> Locator:
        return self.page.locator("input[id*='LastName'], input[name*='LastName'], input[aria-label*='Last Name']")

    @property
    def email_field(self) -> Locator:
        return self.page.locator("input[id*='Email'], input[name*='Email'], input[aria-label*='Email']")

    @property
    def company_field(self) -> Locator:
        return self.page.locator("input[id*='Company'], input[name*='Company'], input[aria-label*='Company']")

    @property
    def title_field(self) -> Locator:
        return self.page.locator("input[id*='Title'], input[name*='Title'], input[aria-label*='Title']")

    @property
    def phone_field(self) -> Locator:
        return self.page.locator("input[id*='Phone'], input[name*='Phone'], input[aria-label*='Phone']")

    @property
    def inquiry_type_field(self) -> Locator:
        return self.page.locator("select[id*='Inquiry'], select[name*='Inquiry'], [aria-label*='Inquiry Type']")

    @property
    def comments_field(self) -> Locator:
        return self.page.locator("textarea[id*='Comment'], textarea[name*='Comment'], textarea[aria-label*='Comment']")

    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Submit")

    @property
    def form_container(self) -> Locator:
        return self.page.locator("form, [class*='form'], section:has-text('Send us a message')")
