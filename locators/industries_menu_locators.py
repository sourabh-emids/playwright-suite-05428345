"""Locators for the Industries Mega-Menu (issue_0004)."""
from playwright.sync_api import Locator, Page


class IndustriesMenuLocators:
    """Locators for the Industries mega-menu component."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def industries_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Industries")

    @property
    def industries_menu(self) -> Locator:
        return self.page.locator('[aria-label*="Industries"], .industries-menu')

    @property
    def payer_link(self) -> Locator:
        return self.page.get_by_role("link", name="Payer").or_(self.page.locator('a[href*="/segments/payer/"]'))

    @property
    def provider_link(self) -> Locator:
        return self.page.get_by_role("link", name="Provider").or_(self.page.locator('a[href*="/segments/provider/"]'))

    @property
    def healthtech_link(self) -> Locator:
        return self.page.get_by_role("link", name="HealthTech").or_(self.page.locator('a[href*="/segments/healthtech/"]'))

    @property
    def life_sciences_link(self) -> Locator:
        return self.page.get_by_role("link", name="Life Sciences").or_(self.page.locator('a[href*="/segments/life-sciences/"]'))

    @property
    def consumer_link(self) -> Locator:
        return self.page.get_by_role("link", name="Consumer").or_(self.page.locator('a[href*="/segments/consumer/"]'))

    @property
    def industry_links(self) -> Locator:
        return self.page.locator('a[href*="/segments/"]')
