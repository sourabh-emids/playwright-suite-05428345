"""Locators and messages for contact form validation."""


class ContactValidationLocators:
    COOKIE_ALLOW_ALL = "Allow all"
    FORM = "#mktoForm_1001"
    SUBMIT = "Submit"
    FORM_HEADING = "Send us a message"
    REQUIRED_FIELDS = (
        ("#FirstName", "This field is required."),
        ("#LastName", "This field is required."),
        ("#Email", "Must be valid email. example@yourdomain.com"),
        ("#Company", "This field is required."),
        ("#Title", "This field is required."),
        ("#Phone", "Must be a phone number. 503-555-1212"),
        ("#mkto71_Inquiry_Type__c", "This field is required."),
        ("#MktoPersonNotes", "This field is required."),
    )
