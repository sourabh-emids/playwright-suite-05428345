"""Locators for tc_001 - Website homepage loads successfully."""
from playwright.sync_api import Locator, Page


class Tc001HomepageLocators:
    """Locators for the homepage."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def logo(self) -> Locator:
        return self.page.get_by_role("link", name="Emids logo")

    @property
    def header(self) -> Locator:
        return self.page.locator("banner")

    @property
    def navigation(self) -> Locator:
        return self.page.locator("navigation")

    @property
    def hero_section(self) -> Locator:
        return self.page.get_by_role("heading", name="In Healthcare, Only Outcomes Matter")

    @property
    def main_content(self) -> Locator:
        return self.page.locator("main")

    @property
    def footer(self) -> Locator:
        return self.page.locator("contentinfo")

    @property
    def menu_items(self) -> Locator:
        return self.page.locator("navigation").get_by_role("listitem")

    @property
    def all_images(self) -> Locator:
        return self.page.locator("img").filter(has_not=self.page.locator("[alt*='placeholder']"))

    @property
    def cookie_banner(self) -> Locator:
        return self.page.locator('region:has-text("This website uses cookies")')
