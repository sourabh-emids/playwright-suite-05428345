"""Locators inspected for desktop mega-navigation in TC-02."""


class Tc02MainNavigationRoutingLocators:
    MAIN_NAVIGATION = "nav[aria-label='Main Navigation']"
    TRIGGER_BY_MENU = {
        "Solutions": (
            MAIN_NAVIGATION
            + " a.mega-nav__trigger[data-trigger='solutions']"
        ),
        "Capabilities": (
            MAIN_NAVIGATION
            + " a.mega-nav__trigger[data-trigger='capabilities']"
        ),
        "Industries": (
            MAIN_NAVIGATION
            + " a.mega-nav__trigger[data-trigger='industries']"
        ),
        "Insights": (
            MAIN_NAVIGATION
            + " a.mega-nav__trigger[data-trigger='insights']"
        ),
        "Company": (
            MAIN_NAVIGATION
            + " a.mega-nav__trigger[data-trigger='company']"
        ),
    }
    DESTINATION_BY_MENU = {
        "Solutions": (
            "a.mega-menu__link-item"
            "[href$='/solutions/modernization-as-a-service/']"
        ),
        "Capabilities": (
            "a.mega-menu__link-item"
            "[href$='/capabilities/data-engineering/']"
        ),
        "Industries": (
            "a.mega-menu__industry-link[href$='/segments/payer/']"
        ),
        "Insights": "a.mega-menu__link-item[href$='/insights/']",
        "Company": "a.mega-menu__link-item[href$='/about-us/']",
    }
