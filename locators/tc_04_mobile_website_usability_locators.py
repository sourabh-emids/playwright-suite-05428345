"""Locators inspected in the mobile Emids layout for TC-04."""


class Tc04MobileWebsiteUsabilityLocators:
    LOGO = "header a.site-logo"
    MENU_TOGGLE = "button[aria-label='Toggle mobile menu']"
    HERO_HEADING = "main h1"
    HERO_IMAGE = "main img"
    HERO_CTA = (
        "main a.button[href$='/forward-deployed-context-engineering/']"
        ":has-text('See How We Deliver Outcomes')"
    )
    MOBILE_MENU_LINK = "a.mega-mobile__link[href$='/solutions/modernization-as-a-service/']"
    MOBILE_CONNECT_CTA = "a.mega-mobile__cta--primary[href$='/contact/']"
