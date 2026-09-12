"""Locators for Partnerships section - EMIDS-LP-018, EMIDS-LP-019"""
from playwright.sync_api import Page, Locator


class PartnershipsLocators:
    """Locators for Partnerships section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.get_by_text("Healthcare transformation takes a network")

    @property
    def partner_logos(self) -> Locator:
        return self.page.locator(".partners img, .partners a img, section img")

    @property
    def servicenow_logo(self) -> Locator:
        return self.page.locator('img[alt*="ServiceNow"]')

    @property
    def unity_logo(self) -> Locator:
        return self.page.locator('img[alt*="Unity"]')

    @property
    def outsystems_logo(self) -> Locator:
        return self.page.locator('img[alt*="OutSystems"]')

    @property
    def kore_ai_logo(self) -> Locator:
        return self.page.locator('img[alt*="Kore.ai"]')

    @property
    def uipath_logo(self) -> Locator:
        return self.page.locator('img[alt*="UiPath"]')
