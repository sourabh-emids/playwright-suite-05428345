"""Stable selectors and accessible names used by the Emids page object."""


class EmidsLocators:
    MAIN = "main"
    HOME_HEADING = "In Healthcare, Only Outcomes Matter"
    HOME_TITLE_PATTERN = r"Emids.*Digital Engineering.*AI Solutions"
    HEADER_LOGO_NAME = "Emids logo"
    HERO_CTA_NAME = "See How We Deliver Outcomes"

    MAIN_NAVIGATION_NAME = "Main Navigation"
    COMPANY_MENU_NAME = "Company"
    ACTIVE_MEGA_MENU = ".mega-menu.is-active"
    NAVIGATION_DESTINATIONS = {
        "Solutions": "a[href$='/solutions/']",
        "Data Engineering": "a[href$='/capabilities/data-engineering/']",
        "Payer": "a[href$='/segments/payer/']",
        "Insights Hub": "a[href$='/insights/']",
        "Our Story": "a[href$='/about-us/']",
    }
    CONTACT_DESTINATION = "a[href$='/contact/']"

    PARTNERS_PATH = "/partners/"
    PARTNERS_HEADING = "Partnerships"
    PARTNER_CARD = ".news-block"
    SNOWFLAKE_HEADING = "Snowflake"
    LEARN_MORE_NAME = "Learn More"
    SNOWFLAKE_PATH = "/partners/snowflake/"

    MOBILE_VIEWPORT = {"width": 390, "height": 844}
    MOBILE_MENU_TOGGLE = "button[aria-label='Toggle mobile menu']"
    ACTIVE_MOBILE_MENU = "#mega-menu-mobile.is-active"
    MOBILE_MENU_ITEMS = ("Solutions", "Capabilities", "Industries", "Insights", "Company")
    CONNECT_NAME = "Connect"

    CONTACT_PATH = "/contact/"
    CONTACT_HEADING = "Let's Connect"
    CONTACT_FORM = "#mktoForm_1001"
    REQUIRED_FIELDS = "[aria-required='true']"
    SUBMIT_BUTTON = "button[type='submit']"
    VALIDATION_ALERT = "[role='alert'].mktoErrorMsg"
    REQUIRED_MESSAGE = "This field is required."
