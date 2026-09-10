class Issue0005ContactFormLocators:
    COOKIE_ALLOW_BUTTON = "Allow all"
    FORM = "form.mktoForm"
    SUBMIT_BUTTON = "Submit"
    VALIDATION_ERROR = "[role='alert'].mktoErrorMsg"
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
    REQUIRED_MESSAGE = "This field is required."
