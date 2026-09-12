"""Locators for Who We Serve section - EMIDS-LP-024"""
from playwright.sync_api import Page, Locator


class WhoWeServeLocators:
    """Locators for Who We Serve section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def section(self) -> Locator:
        return self.page.get_by_text("Every part of healthcare has its own anatomy")

    @property
    def payer_tab(self) -> Locator:
        return self.page.get_by_role("tab", name="Payer")

    @property
    def provider_tab(self) -> Locator:
        return self.page.get_by_role("tab", name="Provider")

    @property
    def healthtech_tab(self) -> Locator:
        return self.page.get_by_role("tab", name="HealthTech")

    @property
    def life_sciences_tab(self) -> Locator:
        return self.page.get_by_role("tab", name="Life Sciences")

    @property
    def consumer_tab(self) -> Locator:
        return self.page.get_by_role("tab", name="Consumer")

    @property
    def explore_ctas(self) -> Locator:
        return self.page.get_by_role("link", name="Explore")
