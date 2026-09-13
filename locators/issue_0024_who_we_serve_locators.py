"""Locators for Five audience/industry entries rendering (issue_0024)."""
from playwright.sync_api import Locator, Page


class WhoWeServeLocators:
    """Locators for Who We Serve section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def who_we_serve_section(self) -> Locator:
        return self.page.get_by_text("Every part of healthcare has its own anatomy")

    @property
    def payer_button(self) -> Locator:
        return self.page.get_by_role("button", name="Payer")

    @property
    def provider_button(self) -> Locator:
        return self.page.get_by_role("button", name="Provider")

    @property
    def healthtech_button(self) -> Locator:
        return self.page.get_by_role("button", name="HealthTech")

    @property
    def life_sciences_button(self) -> Locator:
        return self.page.get_by_role("button", name="Life Sciences")

    @property
    def consumer_button(self) -> Locator:
        return self.page.get_by_role("button", name="Consumer")
