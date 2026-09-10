"""Stable locators for the public contact form."""


class ContactValidationLocators:
    FORM_HEADING_NAME = "Send us a message"
    SUBMIT_NAME = "Submit"
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
    FIRST_NAME_ERROR = "#ValidMsgFirstName"
