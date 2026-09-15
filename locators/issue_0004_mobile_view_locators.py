"""Locators for issue_0004: Mobile responsive layout is usable."""
from playwright.sync_api import Page, Locator


class MobileViewLocators:
    """Locators for mobile view verification."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def mobile_menu_toggle(self) -> Locator:
        return self.page.locator("button[aria-label*='mobile menu'], button[aria-label*='menu']")

    @property
    def emids_logo(self) -> Locator:
        return self.page.locator("a[href='/'] img, img[alt*='Emids']").first

    @property
    def main_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="In Healthcare, Only Outcomes Matter")

    @property
    def footer_content(self) -> Locator:
        return self.page.get_by_role("contentinfo")

    @property
    def hero_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def nav_menu_button(self) -> Locator:
        return self.page.get_by_role("link", name="Connect")
