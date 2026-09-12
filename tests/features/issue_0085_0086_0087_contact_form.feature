"""Contact form displays required fields."""
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


@then("footer corporate information readable at mobile width")
def footer_mobile_readable(page: Page) -> None:
    """Verify footer corporate information readable at mobile width."""
    page.set_viewport_size({"width": 320, "height": 568})
    footer = page.get_by_role("contentinfo")
    expect(footer).to_be_visible()


@then("contact form displays all eight required fields")
def contact_form_fields(page: Page) -> None:
    """Verify contact form displays all eight required fields."""
    required_fields = [
        "* Inquiry Type:",
        "First Name:",
        "Last Name:",
        "Business Email:",
        "Company Name:",
        "Phone:",
        "Job Title:",
        "Subject:",
        "Message:",
    ]
    
    for field in required_fields:
        field_elem = page.get_by_label(field)
        expect(field_elem).to_be_visible()


@then("contact form labels associated with controls")
def form_labels_associated(page: Page) -> None:
    """Verify contact form labels associated with controls."""
    inquiry_label = page.locator("label").filter(has=page.get_by_label("* Inquiry Type:")).first
    assert inquiry_label.is_visible(), "Labels should be associated with controls via for/id"
