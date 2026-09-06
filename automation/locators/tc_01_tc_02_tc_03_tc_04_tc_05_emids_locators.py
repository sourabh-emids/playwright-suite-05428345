class EmidsLocators:
    MAIN = "main"
    SITE_HEADER = "header.site-header"
    HOME_HEADING = "In Healthcare, Only Outcomes Matter"
    HERO_CTA = "See How We Deliver Outcomes"
    HEADER_LOGO = (
        'header.site-header img[alt="Emids logo"]:visible'
    )
    HEADER_CONNECT = (
        'header.site-header a.nav-contact-button[href$="/contact/"]'
    )

    MAIN_NAVIGATION = 'nav[aria-label="Main Navigation"]'
    NAV_TRIGGER = MAIN_NAVIGATION + ' [data-trigger="{menu}"]'
    NAV_MENU = '.mega-menu[data-menu="{menu}"]'
    NAV_DESTINATION_NAME = r"^{label}(?:\s|$)"

    MOBILE_MENU_BUTTON = 'button[aria-label="Toggle mobile menu"]'
    MOBILE_MENU = "#mega-menu-mobile"
    MOBILE_CONNECT = (
        '#mega-menu-mobile a.mega-mobile__cta[href$="/contact/"]'
    )

    CONTACT_FORM = "form#mktoForm_1001"
    CONTACT_SUBMIT = CONTACT_FORM + ' button[type="submit"]'
    REQUIRED_FIELDS = CONTACT_FORM + ' [aria-required="true"]'
    REQUIRED_MESSAGE = "This field is required."

    ERROR_HEADING_PATTERN = (
        r"^(404|not found|page not found|server error|service unavailable)$"
    )
