"""Locators and destinations for TC-02 main navigation checks."""

NAVIGATION_TRIGGER = 'a[data-trigger="{menu}"]'
MEGA_MENU = 'div[data-menu="{menu}"]'
MENU_LINK = 'a[href*="{path}"]'

NAVIGATION_TARGETS = {
    "Solutions": {
        "menu": "solutions",
        "item": "Modernization",
        "path": "/solutions/modernization-as-a-service/",
    },
    "Capabilities": {
        "menu": "capabilities",
        "item": "Data Engineering",
        "path": "/capabilities/data-engineering/",
    },
    "Industries": {
        "menu": "industries",
        "item": "Payer",
        "path": "/segments/payer/",
    },
    "Insights": {
        "menu": "insights",
        "item": "Insights Hub",
        "path": "/insights/",
    },
    "Company": {
        "menu": "company",
        "item": "Our Story",
        "path": "/about-us/",
    },
}
