"""Stable selectors and accessible names observed on the Emids website."""


class EmidsSiteLocators:
    COOKIE_ALLOW_ALL_NAME = "Allow all"
    MAIN_NAVIGATION_NAME = "Main Navigation"
    HOME_HERO_HEADING = "In Healthcare, Only Outcomes Matter"
    HOME_LOGO_NAME = "Emids logo"
    MOBILE_MENU_BUTTON_NAME = "Toggle mobile menu"
    PRIMARY_HOME_CTA_NAME = "See How We Deliver Outcomes"
    PRIMARY_HOME_CTA_PATH = "/forward-deployed-context-engineering/"
    PRIMARY_HOME_CTA_HEADING = "Forward Deployed Context Engineering"
    NAV_DESTINATION_SELECTOR = 'header nav a[href$="{path}"]:visible'
    VISIBLE_DESTINATION_SELECTOR = 'a[href$="{path}"]:visible'

    # Each top-level item opens a mega menu. The inventory below defines one
    # canonical destination through which that menu's routing is verified.
    NAVIGATION_INVENTORY = {
        "Solutions": "/solutions/modernization-as-a-service/",
        "Capabilities": "/capabilities/data-engineering/",
        "Industries": "/segments/payer/",
        "Insights": "/insights/",
        "Company": "/about-us/",
    }

    CONTACT_US_PATH = "/contact/"
    CONTACT_HEADING = "Let's Connect"


class ContactFormLocators:
    FORM_HEADING = "Send us a message"
    SUBMIT_BUTTON_NAME = "Submit"
    REQUIRED_MESSAGE = "This field is required."
    REQUIRED_FIELD_SELECTORS = (
        "#FirstName",
        "#LastName",
        "#Email",
        "#Company",
        "#Title",
        "#Phone",
        "#mkto71_Inquiry_Type__c",
        "#MktoPersonNotes",
    )
