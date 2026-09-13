"""Locators for emids_lp_018-019: Partnerships section."""
from playwright.sync_api import Locator, Page


class EmidsLp018PartnershipsLocators:
    """Locators for Partnerships logo rail/marquee verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def partnerships_section(self) -> Locator:
        return self.page.locator("section").filter(has=self.page.locator("img[alt*='ServiceNow'], img[alt*='AWS']").first)

    @property
    def partner_logos(self) -> Locator:
        return self.page.locator('[class*="partner"] img, [class*="logo"] img, section img[alt]')

    @property
    def marquee_container(self) -> Locator:
        return self.page.locator('[class*="marquee"], [class*="carousel"], [class*="slider"]')
