class Tc05ContactValidationLocators:
    COOKIE_ALLOW_NAME = "Allow all"
    FORM = "#mktoForm_1001"
    REQUIRED_FIELDS = (
        ("#FirstName", "This field is required."),
        ("#LastName", "This field is required."),
        ("#Email", "Must be valid email."),
        ("#Company", "This field is required."),
        ("#Title", "This field is required."),
        ("#Phone", "Must be a phone number."),
        ("#mkto71_Inquiry_Type__c", "This field is required."),
        ("#MktoPersonNotes", "This field is required."),
    )
    REQUIRED = '[aria-required="true"]'
    INVALID_REQUIRED = ".mktoRequired.mktoInvalid"
    SUBMIT_NAME = "Submit"
