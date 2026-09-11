"""Locators inspected on the Marketo contact form for TC-05."""


class Tc05RequiredContactFormValidationLocators:
    FORM = "form:has(#FirstName):has(#MktoPersonNotes)"
    SUBMIT = FORM + " button.mktoButton[type='submit']"
    REQUIRED_FIELD_IDS = (
        "FirstName",
        "LastName",
        "Email",
        "Company",
        "Title",
        "Phone",
        "mkto71_Inquiry_Type__c",
        "MktoPersonNotes",
    )
    ERROR_FOR_FIELD = "#ValidMsg{field_id}"
