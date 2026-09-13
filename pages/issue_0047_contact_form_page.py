"""Page object for Contact form reached by Connect CTAs (issue_0047)."""
from playwright.sync_api import Page

from locators.issue_0047_contact_form_locators import ContactFormLocators


class ContactFormPage:
    """Page object for Contact Form functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactFormLocators(page)

    def goto_contact(self) -> None:
        self.page.goto("/contact/")

    def fill_form(self, data: dict) -> None:
        if "first_name" in data:
            self.locators.first_name_field.fill(data["first_name"])
        if "last_name" in data:
            self.locators.last_name_field.fill(data["last_name"])
        if "email" in data:
            self.locators.email_field.fill(data["email"])
        if "company" in data:
            self.locators.company_field.fill(data["company"])
        if "title" in data:
            self.locators.title_field.fill(data["title"])
        if "phone" in data:
            self.locators.phone_field.fill(data["phone"])
        if "comments" in data:
            self.locators.comments_field.fill(data["comments"])

    def submit(self) -> None:
        self.locators.submit_button.click()
