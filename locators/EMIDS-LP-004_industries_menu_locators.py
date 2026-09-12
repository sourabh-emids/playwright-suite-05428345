"""Locators for Industries mega-menu - EMIDS-LP-004"""
from playwright.sync_api import Page, Locator


class IndustriesMenuLocators:
    """Locators for Industries mega-menu elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def industries_nav(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation").get_by_role("link", name="Industries")

    @property
    def industries_trigger(self) -> Locator:
        return self.page.get_by_role("button", name="Industries").first

    @property
    def payer_link(self) -> Locator:
        return self.page.get_by_role("link", name="Payer")

    @property
    def provider_link(self) -> Locator:
        return self.page.get_by_role("link", name="Provider")

    @property
    def healthtech_link(self) -> Locator:
        return self.page.get_by_role("link", name="HealthTech")

    @property
    def life_sciences_link(self) -> Locator:
        return self.page.get_by_role("link", name="Life Sciences")

    @property
    def consumer_link(self) -> Locator:
        return self.page.get_by_role("link", name="Consumer")
