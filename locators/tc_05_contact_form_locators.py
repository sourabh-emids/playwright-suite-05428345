"""Locators for TC-05 empty contact-form validation checks."""

CONTACT_PATH = "/contact/"
CONTACT_FORM = "form#mktoForm_1001"
SUBMIT_BUTTON = 'form#mktoForm_1001 button[type="submit"]'
REQUIRED_FIELDS = (
    "#FirstName",
    "#LastName",
    "#Email",
    "#Company",
    "#Title",
    "#Phone",
    "#mkto71_Inquiry_Type__c",
    "#MktoPersonNotes",
)
INVALID_REQUIRED_FIELDS = ".mktoRequired.mktoInvalid"
VALIDATION_MESSAGE = ".mktoErrorMsg"
