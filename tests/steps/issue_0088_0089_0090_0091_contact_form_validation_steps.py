"""Step definitions for contact form validation."""
from pytest_bdd import given, then
from playwright.sync_api import Page, expect


@given("I have navigated to the contact page")
def navigate_to_contact(page: Page) -> None:
    """Navigate to the contact page."""
    page.goto("/contact/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("contact form validates email syntax")
def email_validation(page: Page) -> None:
    """Verify contact form validates email syntax."""
    email_field = page.get_by_label("Business Email:")
    email_field.fill("invalid-email")
    
    validity = email_field.evaluate("el => el.validity.valid")
    assert not validity, "Email field should reject invalid email"
