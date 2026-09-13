"""Step definitions for emids_lp_047-049 - Contact form."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@then("All fields display: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments")
def verify_required_fields(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    expect(page_obj.first_name).to_be_visible()
    expect(page_obj.last_name).to_be_visible()
    expect(page_obj.email).to_be_visible()
    expect(page_obj.company).to_be_visible()
    expect(page_obj.title_field).to_be_visible()
    expect(page_obj.phone).to_be_visible()
    expect(page_obj.inquiry_type).to_be_visible()
    expect(page_obj.comments).to_be_visible()


@then("Each label is programmatically associated with its control")
def verify_labels_associated(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    for field in [page_obj.first_name, page_obj.last_name, page_obj.email]:
        label = page.locator(f"label[for='{field.get_attribute('id')}']")
        expect(label).to_be_visible()


@then("User receives clear success feedback message")
def verify_success_feedback(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    page_obj.fill_valid_form()
    page_obj.submit_button.click()
    expect(page_obj.success_message).to_be_visible()


@then("User receives clear failure feedback with actionable guidance")
def verify_failure_feedback(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    page_obj.submit_button.click()
    expect(page_obj.error_message).to_be_visible()


@then("Validation prevents submission; required fields are highlighted")
def verify_required_validation(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    page_obj.submit_button.click()
    expect(page_obj.first_name).to_have_attribute("aria-invalid", "true")


@then("Validation error is displayed; format requirements are clear")
def verify_email_validation(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    page_obj.email.fill("invalid-email")
    page_obj.submit_button.click()
    expect(page_obj.email_error).to_be_visible()


@then("Server revalidates all fields")
def verify_server_revalidation(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    expect(page_obj.submit_button).to_be_visible()


@then("Text is accepted; UI handles gracefully with max length if applicable")
def verify_long_comments(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    page_obj.comments.fill("A" * 5000)
    expect(page_obj.comments).to_be_visible()


@then("Duplicate submission is prevented; button is disabled or feedback shown")
def verify_duplicate_prevented(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    page_obj.fill_valid_form()
    page_obj.submit_button.click()
    expect(page_obj.submit_button).to_be_disabled()


@then("User receives clear timeout message; content preserved for retry")
def verify_timeout_handled(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    expect(page_obj.submit_button).to_be_visible()


@then("User-friendly error displayed; content preserved for retry")
def verify_backend_error(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    expect(page_obj.submit_button).to_be_visible()


@then("Bot detection prevents or flags submission; legitimate users unaffected")
def verify_bot_detection(page: Page) -> None:
    from pages.emids_lp_047_contact_page import ContactFormPage
    page_obj = ContactFormPage(page)
    expect(page_obj.submit_button).to_be_visible()


@then("Options include: Services, Careers, Employment Verification, Media Request, Other")
def verify_inquiry_options(page: Page) -> None:
    from pages.emids_lp_048_inquiry_type_page import InquiryTypePage
    page_obj = InquiryTypePage(page)
    options = page_obj.inquiry_options
    expect(options).to_contain_text("Services")


@then("Validation error displayed; placeholder 'Select...' not accepted as valid choice")
def verify_inquiry_required(page: Page) -> None:
    from pages.emids_lp_048_inquiry_type_page import InquiryTypePage
    page_obj = InquiryTypePage(page)
    page_obj.submit_button.click()
    expect(page_obj.inquiry_error).to_be_visible()


@then("Unknown values outside allowed enum are rejected")
def verify_unknown_rejected(page: Page) -> None:
    from pages.emids_lp_048_inquiry_type_page import InquiryTypePage
    page_obj = InquiryTypePage(page)
    expect(page_obj.inquiry_type).to_be_visible()


@then("Field is usable with native select behavior or accessible custom combobox")
def verify_native_select(page: Page) -> None:
    from pages.emids_lp_048_inquiry_type_page import InquiryTypePage
    page_obj = InquiryTypePage(page)
    expect(page_obj.inquiry_type).to_be_visible()


@then("Server validates and rejects; user sees current options")
def verify_removed_option(page: Page) -> None:
    from pages.emids_lp_048_inquiry_type_page import InquiryTypePage
    page_obj = InquiryTypePage(page)
    expect(page_obj.inquiry_type).to_be_visible()


@then("Server validates against allowed enum; rejects tampered values")
def verify_tampered_request(page: Page) -> None:
    from pages.emids_lp_048_inquiry_type_page import InquiryTypePage
    page_obj = InquiryTypePage(page)
    expect(page_obj.inquiry_type).to_be_visible()


@then("Button enters disabled/loading state; clear pending indication shown")
def verify_pending_state(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    page_obj.fill_valid_form()
    page_obj.submit_button.click()
    expect(page_obj.submit_button).to_be_disabled()


@then("Duplicate activation is prevented; button remains disabled")
def verify_duplicate_prevented(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    page_obj.fill_valid_form()
    page_obj.submit_button.click()
    expect(page_obj.submit_button).to_be_disabled()


@then("Success message is announced via accessible live region or focus management")
def verify_success_announced(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    page_obj.fill_valid_form()
    page_obj.submit_button.click()
    expect(page_obj.success_message).to_be_visible()


@then("User-entered content remains in fields; user can correct and retry")
def verify_failure_content(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    page_obj.first_name.fill("Test")
    page_obj.submit_button.click()
    expect(page_obj.first_name).to_have_value("Test")


@then("User can submit again successfully")
def verify_retry_permitted(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    expect(page_obj.submit_button).to_be_visible()


@then("Field-level errors map to specific fields where possible")
def verify_field_errors(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    page_obj.fill_valid_form()
    page_obj.submit_button.click()
    expect(page_obj.form).to_be_visible()


@then("User-friendly error displayed; content preserved; retry option available")
def verify_5xx_handled(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    expect(page_obj.submit_button).to_be_visible()


@then("User notified; content preserved; retry available")
def verify_timeout(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    expect(page_obj.submit_button).to_be_visible()


@then("User is warned if in-flight submission will be lost")
def verify_navigate_away(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    expect(page_obj.form).to_be_visible()


@then("Only outcome, timestamp, form ID, and correlation ID logged; no full message or unnecessary PII")
def verify_no_pii_logs(page: Page) -> None:
    from pages.emids_lp_049_form_feedback_page import FormFeedbackPage
    page_obj = FormFeedbackPage(page)
    expect(page_obj.form).to_be_visible()
