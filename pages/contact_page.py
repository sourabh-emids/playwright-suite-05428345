"""Page object for the Emids contact page."""
from playwright.sync_api import Page, expect, Locator


class ContactPageLocators:
    """Locators for the Emids contact page."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def inquiry_type_dropdown(self) -> Locator:
        return self.page.get_by_label("* Inquiry Type:")

    @property
    def first_name_field(self) -> Locator:
        return self.page.get_by_label("First Name:", exact=True)

    @property
    def last_name_field(self) -> Locator:
        return self.page.get_by_label("Last Name:", exact=True)

    @property
    def business_email_field(self) -> Locator:
        return self.page.get_by_label("Business Email:", exact=True)

    @property
    def phone_field(self) -> Locator:
        return self.page.get_by_label("Phone:", exact=True)

    @property
    def company_name_field(self) -> Locator:
        return self.page.get_by_label("Company Name:", exact=True)

    @property
    def job_title_field(self) -> Locator:
        return self.page.get_by_label("Job Title:", exact=True)

    @property
    def subject_field(self) -> Locator:
        return self.page.get_by_label("Subject:", exact=True)

    @property
    def message_field(self) -> Locator:
        return self.page.get_by_label("Message:", exact=True)

    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Submit")

    @property
    def form_required_label(self) -> Locator:
        return self.page.locator("text=Required *")


class ContactPage:
    """Page object for the Emids contact page."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactPageLocators(page)

    def goto(self) -> None:
        """Navigate to the contact page."""
        self.page.goto("/contact/")

    def fill_contact_form(self, **kwargs) -> None:
        """Fill the contact form with provided values."""
        if "first_name" in kwargs:
            self.locators.first_name_field.fill(kwargs["first_name"])
        if "last_name" in kwargs:
            self.locators.last_name_field.fill(kwargs["last_name"])
        if "business_email" in kwargs:
            self.locators.business_email_field.fill(kwargs["business_email"])
        if "phone" in kwargs:
            self.locators.phone_field.fill(kwargs["phone"])
        if "company_name" in kwargs:
            self.locators.company_name_field.fill(kwargs["company_name"])
        if "job_title" in kwargs:
            self.locators.job_title_field.fill(kwargs["job_title"])
        if "subject" in kwargs:
            self.locators.subject_field.fill(kwargs["subject"])
        if "message" in kwargs:
            self.locators.message_field.fill(kwargs["message"])
        if "inquiry_type" in kwargs:
            self.locators.inquiry_type_dropdown.select_option(kwargs["inquiry_type"])

    def submit_form(self) -> None:
        """Submit the contact form."""
        self.locators.submit_button.click()

    def select_inquiry_type(self, inquiry_type: str) -> None:
        """Select inquiry type from dropdown."""
        self.locators.inquiry_type_dropdown.select_option(inquiry_type)

    def verify_form_has_required_fields(self) -> None:
        """Verify all required form fields are present."""
        expect(self.locators.first_name_field).to_be_visible()
        expect(self.locators.last_name_field).to_be_visible()
        expect(self.locators.business_email_field).to_be_visible()
        expect(self.locators.company_name_field).to_be_visible()
        expect(self.locators.inquiry_type_dropdown).to_be_visible()
        expect(self.locators.submit_button).to_be_visible()

    def get_form_labels(self) -> list[str]:
        """Get all form labels."""
        labels = self.page.locator("label").all_text_contents()
        return [l.strip() for l in labels if l.strip()]

    def verify_email_validation(self, invalid_email: str) -> None:
        """Test email field validation."""
        self.locators.business_email_field.fill(invalid_email)
        self.locators.submit_button.click()
        # Check for HTML5 validation or custom validation message
        email_field = self.locators.business_email_field
        validity = email_field.evaluate("el => el.validity.valid")
        assert not validity, f"Email field should reject invalid email: {invalid_email}"
