"""Locators for Industries mega-menu implementation (issue_0004)."""
from playwright.sync_api import Locator, Page


class IndustriesMegamenuLocators:
    """Locators for Industries mega-menu elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def industries_button(self) -> Locator:
        return self.page.get_by_role("button", name="Industries")

    @property
    def payer_link(self) -> Locator:
        return self.page.get_by_role("link", name="Payer").or_(self.page.locator("a[href*='payer']").first)

    @property
    def provider_link(self) -> Locator:
        return self.page.get_by_role("link", name="Provider").or_(self.page.locator("a[href*='provider']").first)

    @property
    def healthtech_link(self) -> Locator:
        return self.page.get_by_role("link", name="HealthTech").or_(self.page.locator("a[href*='healthtech']").first)

    @property
    def life_sciences_link(self) -> Locator:
        return self.page.get_by_role("link", name="Life Sciences").or_(self.page.locator("a[href*='life-sciences']").first)

    @property
    def consumer_link(self) -> Locator:
        return self.page.get_by_role("link", name="Consumer").or_(self.page.locator("a[href*='consumer']").first)

    @property
    def menu_visible(self) -> Locator:
        return self.consumer_link
