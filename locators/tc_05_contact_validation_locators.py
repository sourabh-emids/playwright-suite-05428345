"""Stable contact-form locators discovered on emids.com."""


class ContactValidationLocators:
    CONTACT_PATH = "/contact/"
    FORM_HEADING = "Send us a message"
    REQUIRED_FIELDS = (
        "First Name",
        "Last Name",
        "Work Email Address",
        "Company Name",
        "Title",
        "Phone Number",
        "Inquiry Type",
        "Comments",
    )
    SUBMIT_BUTTON = "Submit"
    VALIDATION_MESSAGE = "This field is required."
