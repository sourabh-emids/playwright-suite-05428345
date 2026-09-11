"""Locators inspected for primary homepage calls to action in TC-03."""


class Tc03PrimaryCtaNavigationLocators:
    CONNECT = "a.nav-contact-button"
    OUTCOMES = (
        "main a.button[href$='/forward-deployed-context-engineering/']"
        ":has-text('See How We Deliver Outcomes')"
    )

    CTA_BY_NAME = {
        "Connect": CONNECT,
        "See How We Deliver Outcomes": OUTCOMES,
    }
