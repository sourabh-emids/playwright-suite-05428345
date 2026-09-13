"""Locators for issue_0024: Five audience entries render"""

from playwright.sync_api import Page, Locator


class Issue0024WhoWeServeLocators:
    """Locators for Who We Serve section."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def who_we_serve_section(self) -> Locator:
        """Returns the Who We Serve section."""
        return self.page.get_by_text("We've been inside every corner of healthcare").locator("..")

    @property
    def payer_button(self) -> Locator:
        """Returns the Payer button."""
        return self.page.get_by_role("button", name="Payer")

    @property
    def provider_button(self) -> Locator:
        """Returns the Provider button."""
        return self.page.get_by_role("button", name="Provider")

    @property
    def healthtech_button(self) -> Locator:
        """Returns the HealthTech button."""
        return self.page.get_by_role("button", name="HealthTech")

    @property
    def life_sciences_button(self) -> Locator:
        """Returns the Life Sciences button."""
        return self.page.get_by_role("button", name="Life Sciences")

    @property
    def consumer_button(self) -> Locator:
        """Returns the Consumer button."""
        return self.page.get_by_role("button", name="Consumer")
