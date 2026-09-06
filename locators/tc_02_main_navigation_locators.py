"""Stable main-navigation targets discovered on emids.com."""


class MainNavigationLocators:
    NAVIGATION_NAME = "Main Navigation"
    MENU_ITEM_ANCESTOR = "xpath=ancestor::li[1]"
    DESTINATION_LINK = 'a[href$="{path}"]'
    DESTINATION_PATHS = {
        "Solutions": "/solutions/",
        "Digital Engineering": "/capabilities/digital-engineering/",
        "Payer": "/segments/payer/",
        "Insights Hub": "/insights/",
        "Our Story": "/about-us/",
    }
